#get the href in <a> tags
#using the re, and the key code
#...

import re
import requests
from bs4 import BeautifulSoup

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html5lib')
hrefs = soup.select('a[href]') #get the href list
pat = re.compile(r'href="([^"]*)"')
pat2 = re.compile(r'http')
for item in hrefs:
    h = pat.search(str(item))
    href = h.group(1)
    if pat2.search(str(item)):
        link = href
    else:
        link = url + href

