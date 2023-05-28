import hashlib
from tqdm import tqdm
import logging
import multiprocessing as mp


def check_hash(hash: str, card_number: str) -> bool:
    """Compares hash in the task with the hash of the card number

    Args:
        hash (str): hash in the task
        card_number (str): number of the bank card

    Returns:
        bool: result of comparison of two hashes
    """
    logging.info("Checking the hash")
    card_hash = hashlib.sha256(card_number.encode()).hexdigest()
    if hash == card_hash:
        return int(card_number)
    return 0