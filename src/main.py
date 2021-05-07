import os
from data_loader import load_data
from configuration import get_config
from crawler import CrawlKeyWords, CrawlUserTweets, load_saved_users
from utils import extract_key_words, filter_tweets, save_tweets

ARGS = get_config()


def main():
    data = load_data(os.path.join(ARGS.data_dir, ARGS.key_words_path))
    key_words = extract_key_words(data, ARGS.key_words_header)
    crawl_key_words = CrawlKeyWords(ARGS)
    crawl_key_words.work_flow(key_words)
    user_names = crawl_key_words.user_names

    crawl_user_tweets = CrawlUserTweets(ARGS)
    filtered_data = load_data(os.path.join(ARGS.data_dir, ARGS.filter_key_words_path))
    filtered_key_words = extract_key_words(filtered_data, ARGS.filter_key_words_header)

    crawled_users = load_saved_users(ARGS)

    filtered_tweets = list()
    for users in user_names:
        for user in users:
            if user not in crawled_users:
                try:
                    crawl_user_tweets.work_flow(user)
                    tweets = crawl_user_tweets.crawled_data["tweet"]
                    filtered_tweets.append(filter_tweets(tweets, filtered_key_words))
                except Exception as e:
                    print(e)

    save_tweets(filtered_tweets, os.path.join(ARGS.data_dir, ARGS.final_tweets_path))


if __name__ == "__main__":
    main()
