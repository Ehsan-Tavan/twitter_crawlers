import pandas as pd
from data_loader import is_file_exist


def load_data(path: str):
    """

    :param path: str
    :return: DataFrame
    """
    is_file_exist(path)
    data = pd.read_csv(path)
    return data
