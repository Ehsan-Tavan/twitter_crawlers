import os
import twint


class CrawlUserTweets:
    def __init__(self, args):
        self.args = args
        self.config = None
        self.crawled_data = None

    def set_config(self, user_name: str):
        """

        :param user_name:
        :return:
        """
        config = twint.Config()
        config.Username = user_name
        config.Lang = "fa"
        config.Search = ""
        config.Stats = False
        config.Links = "exclude"
        config.Hide_output = True
        config.Pandas = True
        config.Since = self.args.start_date
        config.Until = self.args.end_date
        self.config = config

    def crawl_user_tweets(self):
        """

        :return:
        """
        twint.run.Search(self.config)
        out_df = twint.output.panda.Tweets_df[["tweet", "hashtags", "retweet", "reply_to"]]
        return out_df

    def save_tweets(self, out_df, user_name):
        """

        :param out_df:
        :param user_name:
        :return:
        """
        remove_indexes = [index for index, row in out_df.iterrows() if len(row["reply_to"]) != 1]
        out_df = out_df.drop(remove_indexes)
        out_df = out_df.drop(columns=["reply_to"])
        out_df.to_csv(os.path.join(self.args.data_dir, self.args.users_tweets_dir, f"{user_name}.pkl"))

    def work_flow(self, user: str) -> None:
        """

        :param user:
        :return: None
        """
        self.set_config(user)
        self.crawled_data = self.crawl_user_tweets()
        if self.args.save_users_tweets:
            self.save_tweets(self.crawled_data, user)
