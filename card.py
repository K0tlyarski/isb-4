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


def get_card_number(hash: str, bins: list, last_numbs: str, core_number: int = mp.cpu_count()) -> int:
    """Selects the card number

    Args:
        hash (str): hash in the task
        bins (list): bins of the cards
        last_numbs (str): last 4 numbers of the card
        core_number (int): number of processor cores

    Returns:
        int: card number or 0 if failed
    """
    args = []
    for i in range(100000,1000000):
        for j in bins:
            args.append((hash, f"{j}{i}{last_numbs}"))
    with mp.Pool(processes=core_number) as p:
        for result in p.starmap(check_hash, tqdm(args, ncols=120, colour="green")):
            if result:
                p.terminate()
                logging.info("Card number got successfully")
                return result
    logging.info("Card number not got")
    return 0