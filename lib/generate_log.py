from datetime import datetime
import os

def generate_log(data):
    """Generate a log file with timestamped entries."""
    
    # STEP 1: Validate input
    # Hint: Check if data is a list
    if not isinstance(data, list):
        raise ValueError("Input data must be a list")
    
    # STEP 2: Generate a filename with today's date (e.g., "log_20250608.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")
    try:
        with open(filename, "w") as file:
            for entry in data:
                file.write(f"{entry}\n")
    except IOError as e:
        print(f"Error writing to file: {e}")
        raise
    
    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")
    return filename


def fetch_data():
    """Fetch data from a public API using requests."""
    try:
        import requests
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: API returned status code {response.status_code}")
            return {}
    except ImportError:
        print("Error: requests library not installed. Install with: pip install requests")
        return {}
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}


if __name__ == "__main__":
    # Log entries to write
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]
    
    # Generate the log file
    log_file = generate_log(log_data)
    print(f"Created: {log_file}")
    
    # Fetch and display data from public API
    print("\nFetching data from API...")
    post = fetch_data()
    if post:
        print("Fetched Post Title:", post.get("title", "No title found"))
        print("Post ID:", post.get("id", "No ID found"))