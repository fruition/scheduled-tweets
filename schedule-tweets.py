import tweepy
import time
import datetime

# Set up Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# List of tweets to schedule
tweets = [
    {'text': 'Hello, world!', 'time': '2023-03-17 10:00:00'},
    {'text': 'Happy Friday!', 'time': '2023-03-17 14:00:00'},
    {'text': 'Have a great weekend!', 'time': '2023-03-17 18:00:00'},
]

# Schedule tweets
for tweet in tweets:
    tweet_time = datetime.datetime.strptime(tweet['time'], '%Y-%m-%d %H:%M:%S')
    current_time = datetime.datetime.now()

    if tweet_time > current_time:
        delay = (tweet_time - current_time).total_seconds()
        time.sleep(delay)
        api.update_status(tweet['text'])
        print(f'Tweet sent: {tweet["text"]}')
    else:
        print(f'Tweet not sent: {tweet["text"]} - Scheduled time has passed')
