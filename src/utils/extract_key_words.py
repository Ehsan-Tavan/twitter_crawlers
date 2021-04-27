from utils import is_header_exist


def extract_key_words(data, header_name: str) -> list:
    """

    :param data: DataFrame
    :param header_name: str
    :return: list
    """
    is_header_exist(data, [header_name])
    return list(data[header_name])
