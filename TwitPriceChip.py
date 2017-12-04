# pip install twitter
# pip install requests

import twitter
import requests
import json

# twitter_API
auth = twitter.OAuth(consumer_key="",
consumer_secret="",
token="",
token_secret="")

# twitter_Auth
t = twitter.Twitter(auth=auth)

# ticker_URL
tickerURL_Ccex_bitzeny = "https://c-cex.com/t/zny-btc.json"
tickerURL_Zaif_jpy = "https://api.zaif.jp/api/1/ticker/btc_jpy"
tickerURL_Zaif_mona = "https://api.zaif.jp/api/1/ticker/mona_jpy"

# requests
request_bitzeny = requests.get(tickerURL_Ccex_bitzeny)
request_jpy = requests.get(tickerURL_Zaif_jpy)
request_mona = requests.get(tickerURL_Zaif_mona)

# json_str
json_str_bitzeny = request_bitzeny.json()
json_str_jpy = request_jpy.json()
json_str_mona = request_mona.json()

# Price
price_bitzeny = json_str_bitzeny['ticker']['lastprice'] * json_str_jpy['last']
price_mona = json_str_mona['last']

# twitText
twitText = ""
twitText = twitText + "-BitZeny-\n"
twitText = twitText + "  39[zny] = " + str(int(price_bitzeny * 39)) + "[jpy]" + "\n"
twitText = twitText + " 114[zny] = " + str(int(price_bitzeny * 114)) + "[jpy]" + "\n"
twitText = twitText + "-Mona-\n"
twitText = twitText + "  39[mona] = " + str(int(price_mona * 39)) + "[jpy]" + "\n"
twitText = twitText + " 114[mona] = " + str(int(price_mona * 114)) + "[jpy]" + "\n"
twitText = twitText + "\n"
twitText = twitText + " 1[mona] = " + str(int(price_mona / price_bitzeny)) + "[zny]" + "\n"
twitText = twitText + "\n"


# twit push
t.statuses.update(status=twitText)