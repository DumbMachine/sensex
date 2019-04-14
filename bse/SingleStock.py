import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from multiprocessing.pool import ThreadPool

class SingleStock:
    def __init__(self, stock_name, url=None, time_period= 0):
        '''
        Initializing the required vbariables and settings
        options = {
            'stock_name': "NAME_OF_STOCK" // not the url
            'threads': None,
            more to added....
                    }
        '''
        self.stock_name = stock_name
        self.urls  = urls
        self.time_period  = time_period
        self.threads = threads if threads else 1
        self.frame = {}
        if not instance_time:
            self.instance_time = time.time()
        if not frame:
            for url in self.urls:
                self.frame[url] = pd.DataFrame({'time': time.time(), 'volume': '0','price': '0','percentage': '0','PREV_CLOSE': '0','OPEN_PRICE': '0'},index=[0])
        self.volume = "#bse_volume > strong"
        self.price = "#Bse_Prc_tick > strong"
        self.percentage = "#b_changetext > span > strong"
        self.PREV_CLOSE = "#b_prevclose > strong"
        self.OPEN_PRICE = "#b_open > strong"


    def get_data(self):
        '''
        Getting Data in the respective frame for the Stock
        '''
        for url in self.urls:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
            req = requests.get(url, headers)

            soup = BeautifulSoup(req.text,'lxml')
            #  TODO: use od.append()
            self.frame[url] = pd.DataFrame({"time":time.time(),
                                                            "volume": str(soup.select(self.volume)[0]).strip("<strong>").strip("</strong>"),
                                                            "price": str(soup.select(self.price)[0]).strip("<strong>").strip("</strong>"),
                                                            "percentage": str(soup.select(self.percentage)[0]).strip("<strong>").strip("</strong>"),
                                                            "PREV_CLOSE": str(soup.select(self.PREV_CLOSE)[0]).strip("<strong>").strip("</strong>"),
                                                            "OPEN_PRICE": str(soup.select(self.OPEN_PRICE)[0]).strip("<strong>").strip("</strong>")
                                                }, index = [0])
            self.frame[url].to_csv("{}.csv".format(url.split('/')[-2]))

    def bulk_get_data(self):
        pool = ThreadPool(self.threads)
        finale = pool.map(self.update, np.array_split(self.urls,self.threads))
        

    def update(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
        for url in self.urls:
            req = requests.get(url, headers)
            soup = BeautifulSoup(req.text,'lxml')
            self.frame[url] = pd.concat([self.frame[url], pd.DataFrame({"time":time.time(),"volume": str(soup.select(self.volume)[0]).strip("<strong>").strip("</strong>"),
                                                    "price": str(soup.select(self.price)[0]).strip("<strong>").strip("</strong>"),
                                                    "percentage": str(soup.select(self.percentage)[0]).strip("<strong>").strip("</strong>"),
                                                    "PREV_CLOSE": str(soup.select(self.PREV_CLOSE)[0]).strip("<strong>").strip("</strong>"),
                                                    "OPEN_PRICE": str(soup.select(self.OPEN_PRICE)[0]).strip("<strong>").strip("</strong>")
                                                    },index = [0])])  # Use APPEND
            self.frame[url].to_csv("{}.csv".format(url.split('/')[-2]))

    # TODO: Instead of using get_data use stream and set the interval to one for the minute
    def stream(self):
        if (self.time_period<1):
            '''
            Minutes case
            '''
            starttime = time.time()
            print("1")
            minute = 0
            while(minute<self.time_period):
                self.update()
                
                minute+=0.5
                time.sleep(60.0)
        else:
            from datetime import datetime
            '''
            HOURS
            '''
            starttime = datetime.now()
            minute = 0
            # TODO: Call UPDATE for the following action
            while(minute<self.time_period):
                self.update()
                print(1)
                minute+=1/360
                time.sleep(60.0)

    def csv_write(self):
        if self.options == None:
            self.frame.to_csv("SOMETHING.csv") #adding path here
        else:
            self.frame.to_csv("SOMETHING.csv")


    def get_stats(self):
        '''
        import matplotlib.pyplot as plt
        plt.plot()
        plt.scatter()
        '''
        # Thsi is the placeholder ffunction where the implementation for statistics will take place.
        pass

    def custom_columns(self):
        # This is the holder function where CUSTOM_COLUMNS will be implemented
        pass

    
class SingleStock:
    def __init__(stock_name, time_period, instance_time, full_day, )