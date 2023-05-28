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


def write_file(data: str, file_name: str) -> None:
    """Writes the data in the file

    Args:
        data(str): data for writting
        file_name(str): name of the file where to write
    """
    try:
        with open(file_name, "w") as f:
            f.write(data)
        logging.info("Write the data successfully")
    except OSError as err:
        logging.info("Write the data is failed")
        raise err