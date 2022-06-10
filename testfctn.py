from best_algo import *
import tweepy
import csv
import time
api_key2 = "EXL2lRypDlKy7Q60VM62cuav0"
api_secrets2 = "q59O7bIXhwTZkMHA9KTUK4BD2eZKeZ4I1bCHmpz9mqnwU5hjjd"
access_token2 = "1532632598421331968-UIjb84VIhBCNmAtFFBsCnpwi2VdiXD"
access_secret2 = "xhuL0CPTxAUbElAFnDe3i1ThnipE9ZQsHceyiKHCDfcWg"

Client2 = tweepy.Client(consumer_key=api_key2,
                        consumer_secret=api_secrets2,
                        access_token=access_token2,
                        access_token_secret=access_secret2)

User_Test = {"ParyLuvsU": 1,
             "artingkrusca": -1,
             "WetAssPattycake": -1,
             "jiifrizzle": -1,
             "DennisCEarl": -1,
             "JaviTweetedHere": -1,
             "slUtf0rABBA": -1,
             "danieljbillo": -1,
             "Shizzzaa_": 1,
             "jnthwallets": 1,
             "wy_pierdalaj": 1,
             "eastcallie2012": 1,
             "Mosta_Pi": -1,
             "MindCap": 1,
             "Hedikoenig": 1,
             "Qu3n71nHur13y": 1,
             "Chikatala1": 1,
             "AwakeyJakey": 1}

data = {}
user = "ParyLuvsU"
# for user in User_Test:
fetch = Client2.get_user(id=None, username=user, expansions=None,
                         tweet_fields=None, user_fields=None, user_auth=True)
if fetch != None:
    response = Client2.get_users_following(fetch.data.id, expansions=None, max_results=1000,
                                           pagination_token=None, tweet_fields=None, user_fields=None, user_auth=True)
    if response.data != None:
        for following in response.data:
            if user in data:
                data[user] += [following.id]
            else:
                data[user] = [following.id]
print(data)
