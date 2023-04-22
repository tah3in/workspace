import instaloader

# Create an Instaloader instance
L = instaloader.Instaloader()

# Login to instagram account
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
try:
    L.load_session_from_file(username)
except FileNotFoundError:
    L.context.log("Session file does not exist yet - Logging in.")
    L.context.log("If you don't have a session file yet, "
                  "you need to login at least once.")
    L.interactive_login(username)
    L.save_session_to_file()

# Print the number of followers
# profile = instaloader.Profile.from_username(L.context, username)
# print("Number of followers:", profile.followers)
