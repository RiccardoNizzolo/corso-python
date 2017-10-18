import urllib3
import requests
import json
import datetime

def post2Slack(message):
    encoded_body =json.dumps({'text': message})
    http = urllib3.PoolManager()
    req = http.request('POST','https://hooks.slack.com/services/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', headers={'Content-Type': 'application/json'}, body=encoded_body)





cookies = {
    '_omappvp': 'M65brz1O27IRzL7Lz3AnE5Nr2UGRnkhqN54GFU0XBgJsoVjqRYAq0p9eEQ2gzyd43eKzbPwGCbuzHxFU4tBmWk9tGyzSLBWA',
    '_omappvs': 'true',
    '__qca': 'P0-88211328-1508158675094',
    'om-402790': 'true',
    'om-402803': 'true',
    'om-402805': 'true',
    'om-interaction-cookie': 'true',
    '_ga': 'GA1.2.1343128863.1508158673',
    '_gid': 'GA1.2.1268069622.1508158674',
    '_gat': '1',
    'oilprice_ci': '48588f2cb137b9ba6d0fab2261d058ef48fe7ab8',
    'mp_f7dc39645bd7dd6a17ccd5e827d4317e_mixpanel': '^%^7B^%^22distinct_id^%^22^%^3A^%^20^%^2215f2543150940-0f9045a1797db2-3b3e5906-1fa400-15f2543150a9f8^%^22^%^2C^%^22^%^24search_engine^%^22^%^3A^%^20^%^22google^%^22^%^2C^%^22^%^24initial_referrer^%^22^%^3A^%^20^%^22https^%^3A^%^2F^%^2Fwww.google.it^%^2F^%^22^%^2C^%^22^%^24initial_referring_domain^%^22^%^3A^%^20^%^22www.google.it^%^22^%^7D',
    'mp_mixpanel__c': '0',
}

headers = {
    'Origin': 'https://oilprice.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4,es;q=0.2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://oilprice.com//freewidgets/get_oilprices_chart/45',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

data = [
  ('blend_id', '45^'),
  ('period', '4^'),
  ('ci_csrf_token', ''),
]
rqst=requests.post('https://oilprice.com/freewidgets/json_get_oilprices', headers=headers, cookies=cookies, data=data)
data=json.loads(rqst.text[rqst.text.find('{'):])


print(data['last_price'])
print(data['blend']['last_price_timestamp'])
print(datetime.datetime.utcfromtimestamp(int(data['blend']['last_price_timestamp'])))
#post2Slack('test')

'''

'''