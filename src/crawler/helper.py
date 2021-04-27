import os
import pandas as pd
from utils import is_item_exist


def extract_tweets(crawled_tweets):
    return [tweet.text for tweet in crawled_tweets]


def extract_users_id(crawled_tweets):
    return [tweet.id_str for tweet in crawled_tweets]


def get_username(crawled_tweets):
    return [tweet.user.screen_name for tweet in crawled_tweets]


def create_folder(root_dir, start_date, end_date):
    path = os.path.join(root_dir, f"start_date_{start_date}_end_date_{end_date}")
    try:
        os.mkdir(path)
        print("Successfully created the directory %s " % path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    return path


def save_data(data, key_words, root_dir, start_date, end_date, data_name):
    """

    :param data:
    :param key_words:
    :param root_dir:
    :param start_date:
    :param end_date:
    :param data_name:
    :return:
    """
    path = create_folder(root_dir, start_date, end_date)
    for extracted_data, key_word in zip(data, key_words):
        data_frame = pd.DataFrame({data_name: extracted_data})
        data_frame.to_csv(os.path.join(path, f"{data_name}_{key_word}.csv"), index=False)