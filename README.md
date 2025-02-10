<h1 align="center">Security Log Parser</h1> 

This project is a Python-based security log parser designed to analyze system log files and detect failed login attempts. The script extracts and counts IP addresses associated with failed authentication attempts, helping system administrators identify potential security threats.

## Features
- Parses log files for security-related events
- Identifies multiple failed login attempts from the same IP
- Flags suspicious IPs (e.g., based on abuse databases)
- Generates a report of potential threats

## Tech Stack
- Python (Regex, File Handling, Collections)
- Regular Expressions (re) for pattern matching
- Counter (collections module) for aggregating results

## How It Works
1. Reads a log file (e.g., /var/log/auth.log)
2. Searches for failed login attempts using a regular expression
3. Extracts and counts the IP addresses associated with those failures
4. Outputs a summary of failed login attempts per IP
 
## UI
![Screenshot Capture - 2025-01-31 - 17-20-40](https://github.com/user-attachments/assets/abab9aa8-47f1-4bb8-b041-d029e6b9a928)

## Future Enhancements
- Add IP geolocation lookup to determine attack origins
- Integrate with a database for tracking login attempts over time
- Implement real-time monitoring with a simple web dashboard



