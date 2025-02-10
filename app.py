import re
from collections import Counter

# Sample log file (Replace with actual path)
log_file_path = "sample_log.txt"

# Regular expression pattern to match failed login attempts and extract IP addresses
failed_login_pattern = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"

def parse_log(file_path):
    with open(file_path, "r") as file:
        log_data = file.readlines()

    failed_attempts = [re.search(failed_login_pattern, line) for line in log_data]
    failed_ips = [match.group(1) for match in failed_attempts if match]

    ip_counts = Counter(failed_ips)
    
    print("\nFailed Login Attempts by IP:")
    for ip, count in ip_counts.items():
        print(f"{ip}: {count} times")

# Run the parser
parse_log(log_file_path)

