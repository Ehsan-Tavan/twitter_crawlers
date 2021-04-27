import os


def is_file_exist(path: str) -> None:
    """

    :param path: str
    """
    if not os.path.exists(path):
        raise Exception(f"File is not exist.\n"
                        f"Path : {path}")
