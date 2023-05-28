import logging
import csv
import matplotlib.pyplot as plt


def create_stats(statistics: dict, file_name: str) -> None:
    """Draws and saves the plot based on the statistic

    Args:
        statistic(dict): data for the plot
        file_name(str): path for saving
    """
    fig = plt.figure(figsize=(30, 5))
    plt.ylabel("Time")
    plt.xlabel("Processes")
    plt.title("Stats")
    x = statistics.keys()
    y = statistics.values()
    plt.bar(x, y, color="blue", width=0.5)
    plt.savefig(file_name)
    logging.info("Create and save statistics")