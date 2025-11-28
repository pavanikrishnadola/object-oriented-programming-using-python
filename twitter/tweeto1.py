import tweepy

api_key = "kPLRyTu5V7MuYrnUat0RM0suR"
api_key_secret = "avzoqucuHhQkhDEQsIF177buONrBZ1cgmpwVLbUHfxp1nR3yK1"
access_token = "1993916464936701953-gOjw4SpxRCirsQh8vBQSu7x6GRwCdZ"
access_token_secret = "3tiHQBvxfAXZbCSvTTnvyinxEHtz0tWvp6Mhg6Bex2i92"
bearer_token = "AAAAAAAAAAAAAAAAAAAAADai5gEAAAAAwJKwAL41KXd5gfzKbalQ3%2Fyq9qk%3DOQvWEKPaXy5FYWDUH0HCt68VbGts7nJFd0Ki6wEOzbMzg5IgP2"

client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

text = "Hello everyone! Posting my first automated tweet using Python 😊🚀 #Python #Tweepy"

try:
    response = client.create_tweet(text=text)
    print("Tweet posted!")
    print("URL: https://x.com/your_username/status/" + response.data["id"])
except Exception as e:
    print("Error:", e)
