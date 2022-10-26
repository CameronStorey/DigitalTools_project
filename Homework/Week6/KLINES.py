import requests
import datetime

def KLINES(symbol,date)

    date = .....(date)
    
    url = "https://api.binance.com/api/v3/klines" 
    params = {
            'symbol' = symbol
            'interval' = '1h'
            }


return requests.get(url,params = params)
