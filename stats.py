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


    def write_stats(processes: int, time: float, file_name: str) -> None:
        """Writes statistic to the file

        Args:
            processes(int): number of processes
            time(float): executing time
            file_name(str): name of the file
        """
        try:
            with open(file_name, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([processes, time])
            logging.info("Stats successfully written")
        except OSError as err:
            logging.info("Stats writing is failed")
            raise err