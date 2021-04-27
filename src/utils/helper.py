import datetime


def calculate_date(days: int) -> [str, str]:
    """

    :param days:
    :return:
    """
    # get today date
    end_date = datetime.datetime.now()

    day_past = datetime.timedelta(days=days)
    start_date = end_date - day_past
    end_date = end_date.strftime("%Y-%m-%d")
    start_date = start_date.strftime("%Y-%m-%d")
    return start_date, end_date


def process_time(start_time: float, end_time: float) -> [int, int]:
    """

    :param start_time:
    :param end_time:
    :return:
    """
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time // 60)
    elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
    return elapsed_mins, elapsed_secs
