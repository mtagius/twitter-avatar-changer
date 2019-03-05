from random import randint
from tweepy import OAuthHandler
from tweepy import API
import keys #python file containing secret API keys

#Twitter API athentication through tweepy
auth = OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
twitterApi = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

filepath = "/home/matt/twitter-avatar-changer/"
dice = [
    "Twitter-Dice-1.png",
    "Twitter-Dice-2.png",
    "Twitter-Dice-3.png",
    "Twitter-Dice-4.png",
    "Twitter-Dice-5.png",
    "Twitter-Dice-6.png",
]

try:
    file = open(filepath + "previousPick.txt", 'r')
except FileNotFoundError:
    file = open(filepath + "previousPick.txt", 'w')

previousPick = 0

for line in open(filepath + "previousPick.txt"):
    previousPick = int(line)

choice = randint(0,5)

while choice == previousPick:
    choice = randint(0,5)

wr = open(filepath + "previousPick.txt", 'w')
wr.write(str(choice))

choice = dice[choice]

print(choice)

twitterApi.update_profile_image(filepath + choice)