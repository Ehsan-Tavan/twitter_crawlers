def is_header_exist(data, headers: list):
    """

    :param data:
    :param headers:
    :return:
    """
    for header in headers:
        if header not in data.columns:
            raise Exception(f"Headers not exist\n"
                            f"\t\t\tDataFrame headers is {list(data.columns)}\n"
                            f"\t\t\tInput headers is {list(headers)}")