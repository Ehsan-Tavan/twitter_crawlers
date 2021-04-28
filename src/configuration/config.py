import argparse
from pathlib import Path


def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str,
                        default=Path(__file__).parents[2].__str__() + "/data")
    parser.add_argument("--key_words_path", type=str,
                        default="/key_words/key_words_extract_users.csv")
    parser.add_argument("--filter_key_words_path", type=str,
                        default="/key_words/filter_key_words.csv")
    parser.add_argument("--users_tweets_dir", type=str,
                        default="/users_tweets")
    parser.add_argument("--final_tweets_path", type=str,
                        default="/final_tweets/final_tweets.csv")

    parser.add_argument("--key_words_headers", type=str, default="key_words")
    parser.add_argument("--filter_key_words_headers", type=str, default="key_words")

    parser.add_argument("--consumer_key", type=str,
                        default="")
    parser.add_argument("--consumer_secret", type=str,
                        default="")
    parser.add_argument("--access_token", type=str,
                        default="")
    parser.add_argument("--access_token_secret", type=str,
                        default="")

    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--num_tweets", type=int, default=10)

    parser.add_argument("--extract_text", type=bool, default=True)
    parser.add_argument("--save_text", type=bool, default=True)
    parser.add_argument("--extract_users", type=bool, default=True)
    parser.add_argument("--save_users", type=bool, default=True)
    parser.add_argument("--save_users_tweets", type=bool, default=True)

    parser.add_argument("--start_date", type=str, default="2019-12-22")
    parser.add_argument("--end_date", type=str, default="2020-07-22")

    args = parser.parse_args()
    return args
