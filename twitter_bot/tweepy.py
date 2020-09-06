import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)




api = tweepy.API(auth)
user = api.me()

print(user.screen_name)
# print(user.name)
# print(user.followers_count)