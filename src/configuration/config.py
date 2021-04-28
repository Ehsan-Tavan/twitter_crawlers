import argparse
from pathlib import Path


def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str,
                        default=Path(__file__).parents[2].__str__() + "/data/",
                        help="Path of root data directory")

    parser.add_argument("--crawl_data_dir", type=str,
                        default="crawl_data",
                        help="Directory name for save tweets and user for each key words")

    parser.add_argument("--key_words_path", type=str,
                        default="key_words/key_words_extract_users.csv",
                        help="Path of key words for crawling tweets and extract users.")

    parser.add_argument("--filter_key_words_path", type=str,
                        default="key_words/filter_key_words.csv",
                        help="Path of key words to filter crawled tweets")

    parser.add_argument("--users_tweets_dir", type=str,
                        default="users_tweets",
                        help="Directory name for save each user's tweets")

    parser.add_argument("--final_tweets_path", type=str,
                        default="final_tweets/final_tweets.csv",
                        help="Path of csv file to save final filtered tweets")

    parser.add_argument("--key_words_header", type=str, default="key_words",
                        help="Header name of key words")

    parser.add_argument("--filter_key_words_header", type=str, default="key_words",
                        help="Header name of filter key words")

    parser.add_argument("--consumer_key", type=str,
                        default="")

    parser.add_argument("--consumer_secret", type=str,
                        default="")

    parser.add_argument("--access_token", type=str,
                        default="")

    parser.add_argument("--access_token_secret", type=str,
                        default="")

    parser.add_argument("--days", type=int, default=7,
                        help="The number of days you want to crawl from now.")

    parser.add_argument("--num_tweets", type=int, default=10,
                        help="The number of tweets you want to crawl for each key word")

    parser.add_argument("--extract_text", type=bool, default=True,
                        help="If true text extract from crawled tweets.")

    parser.add_argument("--save_text", type=bool, default=True,
                        help="If true extracted texts are saved")

    parser.add_argument("--extract_users", type=bool, default=True,
                        help="If true extract user from crawled tweets.")

    parser.add_argument("--save_users", type=bool, default=True,
                        help="If true extracted users are saved")

    parser.add_argument("--save_users_tweets", type=bool, default=True,
                        help="If true each user's tweets are saved.")

    parser.add_argument("--start_date", type=str, default="2019-12-22",
                        help="Start date of crawl by username")

    parser.add_argument("--end_date", type=str, default="2020-07-22",
                        help="End date of crawl by username")

    args = parser.parse_args()
    return args
