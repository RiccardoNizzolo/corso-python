from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import datetime
import pandas_datareader.data as web
import time

#config
word='volkswagen'
symbol='VOW.DE'
start = datetime.datetime(2013, 1, 1)
end = datetime.datetime.now()

#load data
f = web.DataReader(symbol, 'yahoo', start, end)
pytrend = TrendReq()
pytrend.build_payload(kw_list=[word])
interest_over_time_df = pytrend.interest_over_time()

#plot
plt.plot(interest_over_time_df[word])
plt.plot(f['Open'])
plt.legend(['trend of word'+word,'open price of '+symbol])
plt.show()

'''
word='volkswagen'
symbol='VOW.DE'
'''