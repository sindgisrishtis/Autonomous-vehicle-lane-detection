import csv
import os
from datetime import datetime


def log_data(fps, detected):
    os.makedirs("results", exist_ok=True)

    file_path = "results/log.csv"
    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        # Write header only if file does not exist
        if not file_exists:
            writer.writerow(["timestamp", "fps", "detected"])

        writer.writerow([datetime.now(), fps, detected])
