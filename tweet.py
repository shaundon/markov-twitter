import json
import tweepy
import markov

def main(foo, bar):
    config = json.load(open('config.json'))
    twitterConfig = config['twitter']['credentials']
    consumerKey = twitterConfig['consumer_key']
    consumerSecret = twitterConfig['consumer_secret']
    accessTokenKey = twitterConfig['access_token_key']
    accessTokenSecret = twitterConfig['access_token_secret']

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessTokenKey, accessTokenSecret)
    twitterClient = tweepy.API(auth)

    tweet_to_send = markov.get_tweet()
    print "tweeting " + tweet_to_send
    twitterClient.update_status(status=tweet_to_send)



