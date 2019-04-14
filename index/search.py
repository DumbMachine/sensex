# AIM OF THIS FILE IS TO ACT AS THE INDEX FOR STACOKS AND THIER REPECTIVE URLS

import requests
from bs4 import BeautifulSoup
import time



class Search:

    def __init__(self,query=None, return_limit = 5):
        '''
        {
            query: search string,
            return_limit: the number of resutls to be returned for the query
        }
        '''
        self.return_limit = return_limit
        self.select = "#mc_mainWrapper > div.PA10 > div.PA10 > div > table > tbody > tr:nth-child({}) > td:nth-child(1) > p > a"
        self.url = "http://www.moneycontrol.com/stocks/cptmarket/compsearchnew.php?search_data=&cid=&mbsearch_str=&topsearch_type=1&search_str={}".format("+".join(query.split()))
        self.thing = []

    def get_query(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
        req = requests.get(self.url, headers)
        soup = BeautifulSoup(req.text,'lxml')
        for i in range(1,self.return_limit):
            try:
                result = str(soup.select(select.format(i))[0])
                url = result.split()[2].split("<strong>")[0].strip('href=')[:-2][1:]
                name = result.split()[2].split("<strong>")[1].strip("</strong>")+" "+result.split()[3].strip("</a>")
                self.thing.append({
                    "id": url.split("/")[-1],
                    'url': url,
                    'name': name
                })
            except Exception as e:
                print(e)
        return self.thing