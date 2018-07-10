import tweepy

"""
Goes through your following list and unfollows everyone who doesn't follow you back
Written purposely for slay queens.
"""

consumer_key = 	""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    userAccount = api.me()
    for friend in userAccount.friends():
        if friend not in userAccount.followers():
            api.destroy_friendship(friend.screen_name)
            print("Unfollowed",friend.screen_name)
except Exception as e:
    print(e)
