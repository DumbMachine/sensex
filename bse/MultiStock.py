import logging
import os
import time
from datetime import datetime
from multiprocessing.pool import ThreadPool

import numpy as np
import pandas as pd
import requests

from bs4 import BeautifulSoup

# Setting the Logger
if not (os.path.exists(os.getcwd()+"/logging")):
    os.mkdir(os.getcwd()+"/logging/")
logging.basicConfig(filename='./logging/something.log', filemode='w',
                    format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('LOGGER inintialized')


class MultiStock:
    def __init__(self, stock_name, urls, instance_time=False, frame=False, threads=None, full_day=False, time_period=0, logger=False):
        '''
        Initializing the required vbariables and settings
        options = {
            'threads': None,
             'time_period': 1,
             'full_day'; False,
             'logging': True
            more to added....
                    }
        '''
        self.stock_name = stock_name
        self.urls = urls
        self.threads = threads if threads else 1
        self.time_period = time_period
        if full_day:
            self._time_period = 0
            self.full_day = full_day
        self.instance_time = datetime.now()
        self.frame = {}
        if not frame:
            for url in self.urls:
                self.frame[url] = pd.DataFrame({'time': time.time()
                , 'volume': '0', 'price': '0', 'percentage': '0', '_PREV_CLOSE': '0', '_OPEN_PRICE': '0'}, index=[0])

        # PATHS for extracting the Stock information
        self._VOLUME = "#bse_volume > strong"
        self._PRICE = "#Bse_Prc_tick > strong"
        self._PERCENTAGE = "#b_changetext > span > strong"
        self._PREV_CLOSE = "#b_prevclose > strong"
        self._OPEN_PRICE = "#b_open > strong"
        self._MARKET_CLOSE = "12:00"
        logging.info("VARABLES initialized")


    def get_data(self):
        lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
        logging.info("Cycle Started!!!")
        pool = ThreadPool(self.threads)
        # urls = [[url,True] for url in self.urls]
        finale = pool.map(self.update, lol(self.urls, self.threads)[0])
        logging.info("Cycle Completed!!!\n")

    def update(self, link, threaded=False):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
        try:
            req = requests.get(link, headers)
            soup = BeautifulSoup(req.text, 'lxml')
            self.frame[link] = pd.concat([self.frame[link], pd.DataFrame({"time": time.time(), "volume": str(soup.select(self._VOLUME)[0]).strip("<strong>").strip("</strong>"),
                                                                        "price": str(soup.select(self._PRICE)[0]).strip("<strong>").strip("</strong>"),
                                                                        "percentage": str(soup.select(self._PERCENTAGE)[0]).strip("<strong>").strip("</strong>"),
                                                                        "_PREV_CLOSE": str(soup.select(self._PREV_CLOSE)[0]).strip("<strong>").strip("</strong>"),
                                                                        "_OPEN_PRICE": str(soup.select(self._OPEN_PRICE)[0]).strip("<strong>").strip("</strong>")
                                                                        }, index=[0])])  # Use APPEND
            
            if not os.path.exists(os.getcwd()+"/data"):
                os.mkdir(os.getcwd()+'/data')
            self.frame[link].to_csv(
                "./data/{}.csv".format(link.split('/')[-2]))
            logging.info(f"SUCCESSFULLY grabbed {link.split('/')[-2]} Stock")
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)


    # TODO: Instead of using get_data use stream and set the interval to one for the minute
    def stream(self):
        if (self.time_period):
            '''
            time_period = time_period min
            Run the stream for time_period minutes
            '''
            starttime = time.time()
            minute = 0
            while(minute < self.time_period):
                for url in self.urls:
                    self.update(url)
                minute += 1
                time.sleep(60.0)
        else:
            print(1)
            '''
                full_day: True
                stream for the whole trade day
            '''
            while(str(datetime.now().hour)+":"+str(datetime.now().minute) < self._MARKET_CLOSE):
                print("Makret is open")

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
