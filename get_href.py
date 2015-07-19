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

pat = re.compile(r'href="([^"]*)"')
11     pat2 = re.compile(r'http')
12     for item in content:
13    h = pat.search(str(item))
14         href = h.group(1)
15         if pat2.search(href):
16             ans = href
17         else:
18             ans = url+href
