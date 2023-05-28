import logging
import argparse
import time
import load_write
from card import get_card_number, luhn_algorithm
import stats


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        filename="prog_logs.log", filemode="w")
    settings = load_write.load_settings("settings.json")
    parser = argparse.ArgumentParser()
    parser.add_argument("-card", "--get_card_numb", type=int,
                        help="Gets card number, input the number of processors")
    parser.add_argument("-luhn_algorithm", "--luhn_algorithm",
                        help="Checking the card number using the Luhn algorithm")
    parser.add_argument("-stat", "--statistics",
                        help="Gets stats about executing time with different number of processors")
    args = parser.parse_args()