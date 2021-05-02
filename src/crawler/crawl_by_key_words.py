from crawler import extract_tweets, get_username, save_data
import tweepy as tw
from utils import calculate_date
import copy


class CrawlKeyWords:
    def __init__(self, args):
        self.args = args
        self.user_names = list()

    def set_twitter_api(self):
        """

        :return:
        """
        auth = tw.OAuthHandler(self.args.consumer_key, self.args.consumer_secret)
        auth.set_access_token(self.args.access_token, self.args.access_token_secret)
        api = tw.API(auth, wait_on_rate_limit=True)
        return api

    def crawl_key_word(self, key_word, api, start_date, end_date):
        """

        :param key_word:
        :param api:
        :param start_date:
        :param end_date:
        :return:
        """
        tweets = tw.Cursor(api.search,
                           q=key_word,  # key word
                           lang="fa",  # just farsi tweets should crawl
                           since=start_date,
                           until=end_date).items(self.args.num_tweets)
        return tweets

    def work_flow(self, key_words: list) -> None:
        """

        :param key_words: list
        :return: None
        """
        twitter_api = self.set_twitter_api()
        start_date, end_date = calculate_date(days=self.args.days)
        data = [self.crawl_key_word(key_word, twitter_api, start_date, end_date) for key_word in key_words]
        data2 = copy.deepcopy(data)
        if self.args.extract_text:
            tweets = [extract_tweets(key_word_data) for key_word_data in data]
            if self.args.save_text:
                save_data(tweets, key_words, self.args.data_dir, self.args.crawl_data_dir,
                          start_date, end_date, data_name="tweets")

        if self.args.extract_users:
            user_names = [set(get_username(key_word_data)) for key_word_data in data2]
            self.user_names = user_names
            if self.args.save_users:
                save_data(user_names, key_words, self.args.data_dir, self.args.crawl_data_dir,
                          start_date, end_date, data_name="users")
