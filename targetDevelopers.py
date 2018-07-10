import tweepy

"""
This script goes through the followers of a particular user(preferrably someone influential in the tech community)
and finds people who are also developers. It basically is a way to connect with other developers on twitter.
It returns their user names so you can decide who to follow.
Unfortunately, tweepy has a limit on the number of users that can be returned so tough luck.
But hey, at least you'll get a few people to follow. I used it to find developers. You could use it to find graphic
designers and stuff. Enjoy!
"""

consumer_key = 	""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
searchParams = ["rogrammer", "eveloper", "oder", "oftware", "echnologist", "omputer", "ience","ngineer"]
targetUsername = ''

try:
    targetAccount = api.get_user(targetUsername)
    print("User Id", str(targetAccount.id))
    # print("Screen Name:", str(targetAccount.screen_name))
    # print("Bio:",str(targetAccount.description))
    # print("Follower count", str(targetAccount.followers_count))
    # print("Following count", str(targetAccount.friends_count))
    # print("Location", str(targetAccount.location))

    for follower in targetAccount.followers():
        for term in searchParams:
            if term in follower.description:
                print(follower.screen_name +"\n"+follower.description)

except Exception as e:
    print(e)
