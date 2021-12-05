import tweepy

auth = tweepy.OAuthHandler("2j8k9RRpvzJjsv52KkF3bor23", "ElEWe0wxBkJY80cRoyeiAMl8dExtZFvcchT56u4Isid4pWUy5q")
auth.set_access_token("999693022014013440-4jsVX9nHSLYPWozxkn75rOs4cZtTTPQ", "ZYwNOodgzWI1T8dlCCyZJA9r7eYy3f0kZY6106NlpPi2X")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)