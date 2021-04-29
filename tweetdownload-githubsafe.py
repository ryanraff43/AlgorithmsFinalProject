import pandas as pd
import tweepy
from textblob import TextBlob

auth = tweepy.OAuthHandler('API KEY', 'API SECRET KEY')
auth.set_access_token('ACCESS TOKEN', 'ACCESS TOKEN SECRET')
api = tweepy.API(auth)


def get_tweets(hashtags, date, numtweets):

    tagged_tweets = tweepy.Cursor(api.search, q=hashtags, lang="en",since=date, tweet_mode="extended").items(numtweets)

    tweets_df = pd.DataFrame(columns=('Date and Time', 'id', 'source', 'Geo', 'Place', 'Retweets', 'tweet', 'Sentiment Polarity'))

    i = 1
    for tweet in tagged_tweets:

        tweets_df.at[i, 'id'] = tweet.id
        tweets_df.at[i, 'source'] = tweet.source
        tweets_df.at[i, 'tweet'] = tweet.full_text
        tweets_df.at[i, 'Geo'] = tweet.geo
        tweets_df.at[i, 'Place'] = tweet.place
        tweets_df.at[i, 'Favorites'] = tweet.favorite_count
        tweets_df.at[i, 'Retweets'] = tweet.retweet_count
        tweets_df.at[i, 'Date and Time'] = tweet.created_at
        analysis = TextBlob(tweet.full_text)
        tweets_df.at[i, 'Sentiment Polarity'] = analysis.sentiment.polarity
        i = i + 1

    tweets_df.to_csv(hashtags+'tweets.csv', encoding='utf-8')
    print(tweets_df.head())


get_tweets('bostoncollege', '2020-04-01', 100)
print(api.rate_limit_status())

