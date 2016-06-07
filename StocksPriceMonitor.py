'''
This Python code will acquire the prices of stocks of Petrobras (PBR) every 60
seconds and save to a database (update path to save). It is useful when
you would like to monitor the price of a stock in order to take action 
in case it go up or down. If you would like to monitor a different stock
than PBR, just update the link (it has to be from the stockstwits' website)

Goals for the next versions:
- Create alarms to send to the email address of the user

'''

import requests
import time
import pandas as pd
from time import gmtime, strftime

path_save = 'E:/pbr_buy.csv' # update to where you would like to save

session = requests.Session()
PBR_buy = list()
ts = list()
k = 0

while True:      
    page = session.get('http://stocktwits.com/symbol/PBR')
    c = page.content
    
    for char in range(0,len(c)):
        if (c[char:char+14] == "class='price'>"):
            PBR_buy.append(c[char+14:char+18])
            ts.append(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
            break
    k +=1
    print "data adquired " + str(k) + " time, saving & sleeping..."
    out = pd.Series(ts, PBR_buy)
    out.to_csv(path_save)
    time.sleep(60)
