import instaloader

# create instance of Instaloader class
L = instaloader.Instaloader()



# obtain your profile and your followers' profiles
profile = instaloader.Profile.from_username(L.context, "tah3in")
followers = profile.get_followers()

# obtain profiles of people you follow
following = []
for followee in profile.get_followees():
    following.append(followee.username)

# create list of people who do not follow you back
not_following_back = [follower.username for follower in followers if follower.username not in following]

# print list of people who do not follow you back
print(not_following_back)