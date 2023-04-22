import instaloader
import os
os.system('cls')

# Create an Instaloader instance
L = instaloader.Instaloader()

# Load a profile
profile = instaloader.Profile.from_id(L.context, 44237574073)

# Get the number of followers
followers = profile.get_followees()

# Print the number of followers
print("followers:", followers)