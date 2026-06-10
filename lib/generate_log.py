import os
from datetime import datetime

def generate_log(log_data):
    """Write log entries to a dated file and return the filename."""
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list.")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for item in log_data:
            file.write(f"{item}\n")
    print(f"Log written to {filename}")
    return filename