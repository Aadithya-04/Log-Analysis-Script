import re
import csv
from collections import defaultdict, Counter

# File paths
LOG_FILE = "sample.log"
OUTPUT_CSV = "log_analysis_results.csv"

# Configurable threshold - suspicious activity
FAILED_LOGIN_THRESHOLD = 10

# Regex patterns for parsing logs
IP_PATTERN = r'^(\d+\.\d+\.\d+\.\d+)'
ENDPOINT_PATTERN = r'"(?:GET|POST|PUT|DELETE) ([^ ]+)'
FAILED_LOGIN_PATTERN = r'"POST /login HTTP/1\.1" 401'

def parse_log_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def count_requests_per_ip(log_lines):
    ip_counts = Counter(re.match(IP_PATTERN, line).group(1) for line in log_lines if re.match(IP_PATTERN, line))
    return ip_counts.most_common()

def find_most_accessed_endpoint(log_lines):
    endpoints = [re.search(ENDPOINT_PATTERN, line).group(1) for line in log_lines if re.search(ENDPOINT_PATTERN, line)]
    endpoint_counts = Counter(endpoints)
    return endpoint_counts.most_common(1)[0] if endpoint_counts else ("None", 0)

def detect_suspicious_activity(log_lines):
    failed_login_attempts = defaultdict(int)
    for line in log_lines:
        if re.search(FAILED_LOGIN_PATTERN, line):
            ip = re.match(IP_PATTERN, line).group(1)
            failed_login_attempts[ip] += 1
    return {ip: count for ip, count in failed_login_attempts.items() if count > FAILED_LOGIN_THRESHOLD}

def save_to_csv(ip_requests, most_accessed_endpoint, suspicious_activity):
    with open(OUTPUT_CSV, 'w', newline='') as file:
        writer = csv.writer(file)

        # Requests per IP
        writer.writerow(["Requests per IP"])
        writer.writerow(["IP Address", "Request Count"])
        writer.writerows(ip_requests)
        writer.writerow([])

        #Most Accessed Endpoint
        writer.writerow(["Most Accessed Endpoint"])
        writer.writerow(["Endpoint", "Access Count"])
        writer.writerow(most_accessed_endpoint)
        writer.writerow([])

        #Suspicious Activity
        writer.writerow(["Suspicious Activity"])
        writer.writerow(["IP Address", "Failed Login Count"])
        writer.writerows(suspicious_activity.items())

def main():
    log_lines = parse_log_file(LOG_FILE)

    # Count requests per IP address
    ip_requests = count_requests_per_ip(log_lines)
    print("IP Address           Request Count")
    for ip, count in ip_requests:
        print(f"{ip:<20}{count}")

    print()

    #Most accessed endpoint
    endpoint, access_count = find_most_accessed_endpoint(log_lines)
    print(f"Most Frequently Accessed Endpoint:\n{endpoint} (Accessed {access_count} times)")

    print()

    # Detect suspicious activity
    suspicious_activity = detect_suspicious_activity(log_lines)
    print("Suspicious Activity Detected:")
    print("IP Address           Failed Login Attempts")
    for ip, count in suspicious_activity.items():
        print(f"{ip:<20}{count}")

    #results to CSV
    save_to_csv(ip_requests, (endpoint, access_count), suspicious_activity)
    print(f"\nResults saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
