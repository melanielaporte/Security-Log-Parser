<h1 align="center">Security Log Parser</h1> 

Analyze system logs (e.g., Linux auth logs, web server logs) and detect common security threats like failed SSH login attempts, brute-force attacks, and unusual access patterns.

## Features:
- Parses log files for security-related events
- Identifies multiple failed login attempts from the same IP
- Flags suspicious IPs (e.g., based on abuse databases)
- Generates a report of potential threats

## Tech Stack:
- Python (for parsing and analysis)
- Pandas (optional, for data handling)
- Regex (to extract key information)
- IP Geolocation API (to get the origin of suspicious IPs)
 
## UI:
![Screenshot Capture - 2025-01-31 - 17-20-40](https://github.com/user-attachments/assets/abab9aa8-47f1-4bb8-b041-d029e6b9a928)




