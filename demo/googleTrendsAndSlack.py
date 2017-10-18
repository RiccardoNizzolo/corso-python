from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import datetime
import pandas_datareader.data as web
from trigger import *

#reperisco i dati
word='volkswagen'
symbol='VOW.DE'
start = datetime.datetime(2015, 8, 1)
end = datetime.datetime(2015, 10, 30)
f = web.DataReader(symbol, 'yahoo', start, end)
pytrend = TrendReq()
pytrend.build_payload(kw_list=[word],timeframe='2015-09-01 2015-09-30')
interest_over_time_df = pytrend.interest_over_time()


#calcola il trigger
triggerDate=trigger(interest_over_time_df[word])

#invia allarme su slack
post2Slack(str(triggerDate)+'ALARM: check google trend of '+word )

#plot dei risultati
plt.plot(interest_over_time_df[word],'.')
plt.plot(f['Open'])
plt.axvline(triggerDate)
plt.legend()
plt.show()

