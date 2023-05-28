import logging
import json


def read_file(file_name: str) -> str:
    """Reads the file

    Args:
        file_name(str): name of the file

    Returns:
        str: data in the file
    """
    try:
        with open(file_name, "r") as f:
            data = f.read()
        logging.info("Read the data successfully")
    except OSError as err:
        logging.info("Read the data is failed")
        raise err
    return data