import datetime


def calculate_date(days: int) -> [str, str]:
    """

    :param days:
    :return:
    """
    # get today date
    end_date = datetime.datetime.now()

    day_past = datetime.timedelta(days=days)
    start_date = end_date - day_past
    end_date = end_date.strftime("%Y-%m-%d")
    start_date = start_date.strftime("%Y-%m-%d")
    return start_date, end_date


def process_time(start_time: float, end_time: float) -> [int, int]:
    """

    :param start_time:
    :param end_time:
    :return:
    """
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time // 60)
    elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
    return elapsed_mins, elapsed_secs


def is_item_exist(data, item) -> bool:
    """

    :param data:
    :param item:
    :return:
    """
    if item in data:
        return True
    return False


def is_tweet_valid(tweet: str, key_words: list) -> bool:
    """

    :param tweet: str
    :param key_words: list
    :return: bool
    """
    for key_word in key_words:
        if key_word in tweet:
            return True
    return False


def filter_tweets(tweets: list, key_words: list) -> list:
    """

    :param tweets: list
    :param key_words: list
    :return:
    """
    filtered_tweets = list()
    for tweet in tweets:
        if is_tweet_valid(tweet, key_words):
            filtered_tweets.append(tweet)
    return filtered_tweets
