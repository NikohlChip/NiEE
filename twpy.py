import tweepy
import csv
import pandas as pd

auth = tweepy.OAuthHandler("2j8k9RRpvzJjsv52KkF3bor23", "ElEWe0wxBkJY80cRoyeiAMl8dExtZFvcchT56u4Isid4pWUy5q")
auth.set_access_token("999693022014013440-4jsVX9nHSLYPWozxkn75rOs4cZtTTPQ", "ZYwNOodgzWI1T8dlCCyZJA9r7eYy3f0kZY6106NlpPi2X")

api = tweepy.API(auth,wait_on_rate_limit=True)

#####Dover
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search_tweets,q="#MeToo",count=100,lang="en",tweet_mode='extended').items():
    print (tweet.created_at, tweet.user.screen_name, tweet.full_text)
    csvWriter.writerow([tweet.created_at, tweet.full_text.encode('utf-8')])
    print('＝＝＝＝＝＝＝＝＝＝')
    print('twid : ',tweet.id)
    print('user : ',tweet.user.screen_name)
    print('date : ', tweet.created_at)
    print(tweet.full_text)
    print('favo : ', tweet.favorite_count)
    print('retw : ', tweet.retweet_count)