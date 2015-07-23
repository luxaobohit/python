# usr/bin/env python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
from urllib import urlretrieve

#tieba.baidu.com  users rank page
urlsrc = 'http://tieba.baidu.com/f/like/furank?kw=%B9%FE%B6%FB%B1%F5%B9%A4%D2%B5%B4%F3%D1%A7&pn='

payload = {'kw': '%B9%FE%B6%FB%B1%F5%B9%A4%D2%B5%B4%F3%D1%A7',
           'pn': '1',
           }

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36 QQBrowser/9.0.2229.400',
           'Referer': 'http://tieba.baidu.com/f/like/furank?',
           }

urlhead = r'http://tieba.baidu.com'

beginpage, endpage = 1, 5
savepath = r'C:/Users/lu/Desktop/tieba/'

for page in range(beginpage, endpage + 1):
    res = requests.get(urlsrc + str(page), data = None, headers = headers)
    soup = BeautifulSoup(res.text, 'html5lib')
    users = soup.select('.drl_item_card ')

    for usr in users:
        #get the homepage of a certain user
        url = urlhead + re.search('\/home(.)+furank', str(usr)).group()
        usrres = requests.get(url, headers = headers)
        usrsoup = BeautifulSoup(usrres.text, 'html5lib')
        headinfo = usrsoup.select('.userinfo_left_head')[0]
        #get the image url of the user's head img
        imgurl = re.search('http(.)+"', str(headinfo)).group()[:-1]
        #urlretrieve function to download 
        urlretrieve(imgurl, savepath + str(page) \
                    + '_' + str(users.index(usr)) + '.jpg')
    

