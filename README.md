# Log-Analysis-Script
 A Python script that processes log files to extract and analyze key information.

## Overview

This Python script parses a log file to analyze and extract meaningful insights, such as:
- The number of requests per IP address.
- The most frequently accessed endpoint.
- Suspicious activity based on failed login attempts.

The results are printed to the console and saved in a CSV file for further analysis.

---

## Features

1. **Request Count Per IP**: Counts the number of requests made by each IP address.
2. **Most Accessed Endpoint**: Identifies the most frequently accessed endpoint.
3. **Suspicious Activity Detection**: Detects IP addresses with failed login attempts exceeding a configurable threshold (`FAILED_LOGIN_THRESHOLD`).
4. **CSV Export**: Outputs the analysis results into a CSV file.

---

## File Structure

- **Script**: `log_analysis.py`
- **Input Log File**: `sample.log`
- **Output CSV File**: `log_analysis_results.csv`

---

## Input File Format (`sample.log`)

The log file is expected to be in a standard format where each line contains:
- IP address
- Request details (method, endpoint, protocol, and status code)

### Example Log Entries:
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:36 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:12:37 +0000] "GET /contact HTTP/1.1" 200 312
198.51.100.23 - - [03/Dec/2024:10:12:38 +0000] "POST /register HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:12:39 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:40 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:41 +0000] "GET /dashboard HTTP/1.1" 200 1024
198.51.100.23 - - [03/Dec/2024:10:12:42 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:12:43 +0000] "GET /dashboard HTTP/1.1" 200 1024
203.0.113.5 - - [03/Dec/2024:10:12:44 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
203.0.113.5 - - [03/Dec/2024:10:12:45 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:46 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:47 +0000] "GET /profile HTTP/1.1" 200 768
192.168.1.1 - - [03/Dec/2024:10:12:48 +0000] "GET /home HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:12:49 +0000] "POST /feedback HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:12:50 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.1 - - [03/Dec/2024:10:12:51 +0000] "GET /home HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:12:52 +0000] "GET /about HTTP/1.1" 200 256
203.0.113.5 - - [03/Dec/2024:10:12:53 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:54 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:55 +0000] "GET /contact HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:12:56 +0000] "GET /home HTTP/1.1" 200 512
192.168.1.100 - - [03/Dec/2024:10:12:57 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
203.0.113.5 - - [03/Dec/2024:10:12:58 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:59 +0000] "GET /dashboard HTTP/1.1" 200 1024
192.168.1.1 - - [03/Dec/2024:10:13:00 +0000] "GET /about HTTP/1.1" 200 256
198.51.100.23 - - [03/Dec/2024:10:13:01 +0000] "POST /register HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:13:02 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:13:03 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:13:04 +0000] "GET /profile HTTP/1.1" 200 768
198.51.100.23 - - [03/Dec/2024:10:13:05 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:13:06 +0000] "GET /home HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:13:07 +0000] "POST /feedback HTTP/1.1" 200 128


---

## Installation and Setup

1. Clone or download the repository.
2. Place the log file (`sample.log`) in the same directory as the script.
3. Install Python (version 3.6 or higher).
4. Ensure you have the required libraries (no external libraries are required).

---

## Usage

1. **Run the Script**:
   ```bash
   python script.py

2. **View the Output**:
    The results are displayed on the console.
    A CSV file (log_analysis_results.csv) is generated with the results.


**Configuration**
Modify Suspicious Activity Threshold
The threshold for failed login attempts can be adjusted by changing the value of FAILED_LOGIN_THRESHOLD in the script:
FAILED_LOGIN_THRESHOLD = 10  # Default is 10

**Output Details**

Console Output
Example : 
IP Address           Request Count
192.168.1.1          5
203.0.113.5          12
10.0.0.2             6
...

Most Frequently Accessed Endpoint:
/home (Accessed 7 times)

Suspicious Activity Detected:
IP Address           Failed Login Attempts
203.0.113.5          11
192.168.1.100        7

**CSV File**
The output CSV contains three sections:

Requests Per IP: Each IP with its request count.
Most Accessed Endpoint: The endpoint with the highest access count.
Suspicious Activity: IP addresses and their corresponding failed login attempts.

**Sample Data**
Sample log entries used in this script are included in sample.log.

**License**
This project is open-source and free to use for educational and analytical purposes.

Copy and save this content in a `README.md` file.
