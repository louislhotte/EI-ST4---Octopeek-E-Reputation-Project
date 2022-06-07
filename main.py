# Import Libraries
from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import time
import datetime

# Authentication Keys
consumerKey = "rP1N2eAUuLP3zmGkTj166zwgs"
consumerSecret = "050RMsIfrigsRaI1Od454ScbQAGxAvWGRcgBGOrP50uFkiuxvc"
accessToken = "1457688577790337029-UNccZXBzmiwXIqHqguknLvxMivu1zB"
accessTokenSecret = "WShy6U4B1vU5JyooAnxcbLGzfzVhRvOwvzjolOPTywKDG"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth,wait_on_rate_limit=True)
username = "CerveraRomain"

# Sentiment Analysis

def percentage(part, whole):
     return 100 * float(part) / float(whole)


keyword = "#Elon Musk"
noOfTweet = int(input("Please enter how many tweets to analyze: "))
# start_date = datetime.datetime(2022, 1, 6, 12, 00, 00)
# end_date = datetime.datetime(2022, 3, 6, 12, 00, 00)

tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(noOfTweet)

k = 0
positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
     k = k + 1
     # print(tweet.text)
     analysis = TextBlob(tweet.text)
     polarity += analysis.sentiment.polarity

     if (analysis.sentiment.polarity == 0):
          neutral += 1
          # print(analysis)

     elif (analysis.sentiment.polarity < 0.00):
          negative += 1
          print(analysis)

     elif (analysis.sentiment.polarity > 0.00):
          positive += 1
          # print(analysis)

positive = percentage(positive, k)
negative = percentage(negative, k)
neutral = percentage(neutral, k)
polarity = percentage(polarity, k)

positive = format(positive, '.1f')
negative = format(negative, '.1f')
neutral = format(neutral, '.1f')


#Creating PieCart

labels = ['Positive ['+str(positive)+'%]' , 'Neutral ['+str(neutral)+'%]','Negative ['+str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold','red']

patches, texts = plt.pie(sizes,colors=colors, startangle=90)
plt.style.use('default')
plt.legend(patches, labels, loc='best')
plt.title("Sentiment Analysis Result for keyword = "+keyword+" and "+str(k)+" tweets" )
plt.axis('equal')
# plt.savefig(str(k)+' tweets.png',dpi = 600)
plt.show()

