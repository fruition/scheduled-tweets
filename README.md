# Scheduled Tweets Python Workbook

Using Python and the Tweepy library to interact with the Twitter API. You will need to have a Twitter Developer account, and access to the required API keys and tokens.

Before you begin, make sure to install the Tweepy library:

Copy code
pip install tweepy
Here's a sample Python script that schedules tweets:

python
Copy code
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
        
Replace the placeholders in the script with your actual API keys and tokens. The script creates a list of tweets with the desired text and time in the 'tweets' variable. The script then iterates through each tweet, waiting for the appropriate time before posting it on Twitter.

Make sure to run the script at a time that is earlier than the earliest scheduled tweet, otherwise, the script will skip tweets with scheduled times that have already passed.

Remember that the time in the script should be in your local time zone.
