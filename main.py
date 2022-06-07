# Import Libraries
from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import time

# Authentication Keys
consumerKey = "rP1N2eAUuLP3zmGkTj166zwgs"
consumerSecret = "050RMsIfrigsRaI1Od454ScbQAGxAvWGRcgBGOrP50uFkiuxvc"
accessToken = "1457688577790337029-UNccZXBzmiwXIqHqguknLvxMivu1zB"
accessTokenSecret = "WShy6U4B1vU5JyooAnxcbLGzfzVhRvOwvzjolOPTywKDG"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth,wait_on_rate_limit=True)


# Sentiment Analysis

def percentage(part, whole):
     return 100 * float(part) / float(whole)


keyword = "Elon Musk"
noOfTweet = int(input("Please enter how many tweets to analyze: "))

tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(noOfTweet)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
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

positive = percentage(positive, noOfTweet)
negative = percentage(negative, noOfTweet)
neutral = percentage(neutral, noOfTweet)
polarity = percentage(polarity, noOfTweet)

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
plt.title("Sentiment Analysis Result for keyword = "+keyword+" and "+str(noOfTweet)+" tweets" )
plt.axis('equal')
plt.show()

