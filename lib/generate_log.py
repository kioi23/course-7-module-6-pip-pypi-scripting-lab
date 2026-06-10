from datetime import datetime


def generate_log(log_data):
    # Validate input
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")

    # Create filename in required format
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write to file
    with open(filename, "w") as file:
        for item in log_data:
            file.write(str(item) + "\n")

    # Confirmation message (tests may check this)
    print(f"Log file created: {filename}")

    return filename


if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)