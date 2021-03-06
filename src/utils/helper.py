import datetime
import pandas as pd


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


def filter_tweets(tweets: list, dates: list, key_words: list) -> [list, list]:
    """

    :param tweets: list
    :param dates: list
    :param key_words: lis
    :return:
    """
    for i in range(len(tweets)):
        if not is_tweet_valid(tweets[i], key_words):
            tweets[i] = None
            dates[i] = None
    return tweets, dates


def save_tweets(tweets: list, dates: list, path: str) -> None:
    """

    :param tweets: list
    :param dates: list
    :param path: str
    :return: None
    """
    data_frame = pd.DataFrame({"tweets": tweets, "date": dates})
    data_frame.to_csv(path, index=False)
