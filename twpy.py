import tweepy
import os
import csv
import pandas as pd

if __name__ == '__main__':
    try:
        auth = tweepy.OAuthHandler(os.environ["CONSUMER_TOKEN"],os.environ["CONSUMER_TOKEN_SECRET"])
        auth.set_access_token(os.environ["ACCESS_TOKEN"],os.environ["ACCESS_TOKEN_SECRET"])

        api = tweepy.API(auth,wait_on_rate_limit=True)

        #####Dover
        # Open/Create a file to append data
        csvFile = open('dover.csv', 'a')
        #Use csv Writer
        csvWriter = csv.writer(csvFile)

        for tweet in tweepy.Cursor(api.search_tweets,q='安倍晋三',count=1500,tweet_mode='extended', result_type="mixed",include_entities=True).items():
            if(tweet.user.screen_name == "_Nikohl"):
                print(tweet.created_at, tweet.user.screen_name, tweet.full_text)
                csvWriter.writerow([tweet.created_at, tweet.full_text])

                #####
                print('＝＝＝＝＝＝＝＝＝＝')
                print('twid : ',tweet.id)
                print('user : ',tweet.user.screen_name)
                print('date : ', tweet.created_at)
                print(tweet.full_text)
                print('favo : ', tweet.favorite_count)
                print('retw : ', tweet.retweet_count)
                print('lang : ', tweet.lang)

    except tweepy.TweepError as e:
        print(e.reason)