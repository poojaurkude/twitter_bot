import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
           yield cursor.next()
    except tweepy.RateLimitError:
       time.sleep(300)  



#Genrous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.followers_count > 100 'Ajeasmith':
        follower.follow()
        break
    
