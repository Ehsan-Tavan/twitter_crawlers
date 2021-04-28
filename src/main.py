from data_loader import load_data
from configuration import get_config
from crawler import CrawlKeyWords, CrawlUserTweets
from utils import extract_key_words, filter_tweets, save_tweets

ARGS = get_config()


def main():
    data = load_data(ARGS.key_words_extract_users)
    key_words = extract_key_words(data, ARGS.key_words_headers)
    crawl_key_words = CrawlKeyWords(ARGS)
    crawl_key_words.work_flow(key_words)
    user_names = crawl_key_words.user_names

    crawl_user_tweets = CrawlUserTweets(ARGS)
    filtered_data = load_data(ARGS.filter_key_words)
    filtered_key_words = extract_key_words(filtered_data, ARGS.filter_key_words_headers)

    filtered_tweets = list()
    for users in user_names:
        for user in users:
            try:
                crawl_user_tweets.work_flow(user)
                tweets = crawl_user_tweets.crawled_data["tweet"]
                filtered_tweets.append(filter_tweets(tweets, filtered_key_words))
            except Exception as e:
                print(e)
    final_tweets = [tweet for tweet in [tweets for tweets in filtered_tweets]]
    save_tweets(final_tweets, ARGS.final_tweets)


if __name__ == "__main__":
    main()
