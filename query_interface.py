import json
import os
import re
from datetime import datetime

# Load log files
def load_logs(log_files):
    logs = []
    for file in log_files:
        if os.path.exists(file):
            with open(file, 'r') as f:
                for line in f:
                    try:
                        logs.append(json.loads(line.strip()))
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON from line: {line}")
    return logs

def query_logs(logs, level=None, log_string=None, start_date=None, end_date=None, source=None):
    results = []
    for log in logs:
        try:
            if level and log['level'] != level:
                continue
            if log_string and not re.search(log_string, log['log_string']):
                continue
            if start_date and datetime.fromisoformat(log['timestamp'][:-1]) < start_date:
                continue
            if end_date and datetime.fromisoformat(log['timestamp'][:-1]) > end_date:
                continue
            if source and log['metadata']['source'] != source:
                continue
            results.append(log)
        except KeyError as e:
            print(f"Missing key in log entry: {e}")
        except Exception as e:
            print(f"Error processing log entry: {e}")
    return results

# Example query function
def run_query():
    log_files = ['logs/log1.log', 'logs/log2.log', 'logs/log3.log']
    logs = load_logs(log_files)
    
    level = input("Enter log level (info, error, success): ").lower()
    log_string = input("Enter log string to search: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    source = input("Enter source file: ")

    start_date = datetime.fromisoformat(start_date) if start_date else None
    end_date = datetime.fromisoformat(end_date) if end_date else None

    results = query_logs(logs, level, log_string, start_date, end_date, source)
    for result in results:
        print(json.dumps(result, indent=4))

# Run the query interface
if __name__ == '__main__':
    run_query()
