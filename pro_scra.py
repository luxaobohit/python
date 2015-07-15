
import requests
from bs4 import BeautifulSoup
import csv

urlhead = 'http://www.inateck.com/products/'
urltail = ['USB-3-0-hdd-docking-station', 'usb-hub',\
           'bluetooth-product', 'wireless-product',\
           'accessories', 'USB-3-0-hdd-enclosure', 'pcie-to-usb-3-0-card', \
           'usb-chargers', 'protection', 'USB-cables']

info = 'Information'
path = ''
with open(path + r'proFile.csv', 'wb') as proFile:
    for tail in urltail:
        url = urlhead + tail + '.html/'
        res = requests.post(url)
        soup = BeautifulSoup(res.text, 'html5lib')
        spamwrite = csv.writer(proFile, dialect = 'excel')
        spamwrite.writerow([tail.upper(), info.upper()])
        for item in soup.select('.cat_pro_pic'):
            spamwrite.writerow([item.select('.title')[0].text,\
                                item.select('.des')[0].text])
        spamwrite.writerow('\n')

