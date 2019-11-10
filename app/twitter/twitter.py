import os

import tweepy
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), encoding='utf-8')


def get_env_variable(var_name, default=None):
    try:
        return os.environ[var_name]

    except KeyError:
        if default is None:
            error_msg = '필수 환경 변수 {}가 설정되지 않았습니다.'.format(var_name)
            raise ImproperlyConfigured(error_msg)

        return default


consumer_key = get_env_variable('CONSUMER_KEY')
consumer_secret = get_env_variable('CONSUMER_SECRET')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = get_env_variable('ACCESS_TOKEN')
access_token_secret = get_env_variable('ACCESS_TOKEN_SECRET')
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

location = "%s,%s,%s" % ("35.95", "128.25", "1000km")
keyword = "방탄소년단 OR bts"
wfile = open(os.getcwd() + "twitter.txt", mode='w')

cursor = tweepy.Cursor(api.search, q=keyword, since='2015-01-01',
                       count=100, geocode=location, include_entitles=True)

for i, tweet in enumerate(cursor.items()):
    print('{}: {}'.format(i, tweet.text))
    wfile.write(tweet.text + '\n')

wfile.close()
