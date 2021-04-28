import argparse
from pathlib import Path


def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root_dir", default=Path(__file__).parents[2].__str__() +
                                              "/data/crawl_data", type=str)
    parser.add_argument("--key_words_extract_users", default=Path(__file__).parents[2].__str__() +
                                                             "/data/key_words/key_words_extract_users.csv", type=str)
    parser.add_argument("--filter_key_words", default=Path(__file__).parents[2].__str__() +
                                                             "/data/key_words/filter_key_words.csv", type=str)
    parser.add_argument("--users_tweets", default=Path(__file__).parents[2].__str__() +
                                                             "/data/users_tweets", type=str)

    parser.add_argument("--final_tweets", default=Path(__file__).parents[2].__str__() +
                                                             "/data/final_tweets/final_tweets.csv", type=str)

    parser.add_argument("--key_words_headers", default="key_words", type=str)
    parser.add_argument("--filter_key_words_headers", default="key_words", type=str)

    parser.add_argument("--consumer_key", default="2HDll0TMxCjWjhm7QAVihCRvq", type=str)
    parser.add_argument("--consumer_secret", default="gctVK1YRJK4TMIuURtMAS6NhOqlkcbPkVzEoU5PuZMVhf9NYSc",
                        type=str)
    parser.add_argument("--access_token", default="1008098850958176257-XboDX2szcJT94pXyUw9kwRym6CwsFr",
                        type=str)
    parser.add_argument("--access_token_secret", default="nEaa91mWTE58PaxlsmlOK0g7dam7vjdPJYHpDQm4A9xoJ",
                        type=str)

    parser.add_argument("--days", default=7,
                        type=int)
    parser.add_argument("--num_tweets", default=20,
                        type=int)

    parser.add_argument("--extract_text", default=True,
                        type=bool)
    parser.add_argument("--save_text", default=True,
                        type=bool)
    parser.add_argument("--extract_users", default=True,
                        type=bool)
    parser.add_argument("--save_users", default=True,
                        type=bool)
    parser.add_argument("--save_users_tweets", default=True,
                        type=bool)

    parser.add_argument("--start_date", default="2019-12-22",
                        type=str)
    parser.add_argument("--end_date", default="2020-07-22",
                        type=str)

    args = parser.parse_args()
    return args
