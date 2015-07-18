#! usr/bin/python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json

url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2015-07-29&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CSQ&purpose_codes=ADULT'
#url_1 = 'https://kyfw.12306.cn/otn/leftTicket/query'

"""
headers = {'leftTicketDTO.train_date': '2015-07-29',
             'leftTicketDTO.from_station': 'BJP',
             'leftTicketDTO.to_station': 'CSQ',
             'purpose_codes': 'ADULT'
             }
"""

res = requests.get(url, params = None, verify = False)
soup = BeautifulSoup(res.text, 'html5lib')
#response returns a json content, using json module to convert json to dict
hjson = json.loads(soup.text)

#get the tickets' information
for item in hjson["data"]:
    print item["queryLeftNewDTO"]["station_train_code"],\
          item["queryLeftNewDTO"]["start_station_name"],\
          item["queryLeftNewDTO"]["end_station_name"],\
          item["queryLeftNewDTO"]["from_station_name"],\
          item["queryLeftNewDTO"]["to_station_name"],\
          item["queryLeftNewDTO"]["start_time"],\
          item["queryLeftNewDTO"]["arrive_time"], \
          item["queryLeftNewDTO"]["lishi"], \
          item["queryLeftNewDTO"]["yw_num"]

"""
A problem: dict has no order and the 12306.cn's url paramteters need a certain order!
So we can't pass a dict to requests.get() method.
"""
