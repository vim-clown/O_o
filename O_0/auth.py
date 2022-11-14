import twitter, os

api = twitter.Api(
    consumer_key=os.environ["api_key"],
    consumer_secret=os.environ["api_secret_key"],
    access_token_key=os.environ["access_token"],
    access_token_secret=os.environ["access_token_secret"],
    sleep_on_rate_limit=True,)


