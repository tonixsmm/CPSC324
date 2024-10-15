import tweepy
import key

# Twitter API credentials
API_KEY = key.TWITTER_KEY['API_KEY']
API_SECRET_KEY = key.TWITTER_KEY['API_SECRET_KEY']
ACCESS_TOKEN = key.TWITTER_KEY['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = key.TWITTER_KEY['ACCESS_TOKEN_SECRET']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def search_tweets(query, max_tweets):
    try:
        # Call the Twitter API to fetch tweets
        tweets = api.search_tweets(q=query, count=max_tweets, tweet_mode='extended')

        for tweet in tweets:
            print(f"{tweet.user.screen_name} said: {tweet.full_text}\n")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    hashtag_query = "#JoeBiden"
    max_tweets = 1 
    search_tweets(hashtag_query, max_tweets)

if __name__ == "__main__":
    main()
