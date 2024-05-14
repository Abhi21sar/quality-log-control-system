Quality Log Control System
Overview
The Quality Log Control System is designed to capture and analyze logs from multiple APIs. It consists of two main components:

Log Ingestor: Integrates with multiple APIs to capture and store logs in designated log files.
Query Interface: Provides a command-line interface (CLI) for querying and analyzing the logs based on various filters.
Features
API Log Ingestion: Capture logs from multiple APIs and store them in different log files.
Configurable Log Levels and Paths: Configure logging levels and file paths for each API using a JSON configuration file.
Standardized Log Format: Ensure logs are formatted consistently, including timestamp, log level, log message, and metadata.
Robust Error Handling: Implement error handling to ensure logging does not disrupt API functionality.
Scalable Logging: Utilize asynchronous logging and log rotation to handle high volumes of log data.
Query Interface: Provide a CLI for querying logs based on log level, log string, timestamp, and source file.
Advanced Querying: Support for date range searches and regex-based log string searches.
System Design
Log Ingestor
API Integration: Captures logs from multiple APIs.
Log Formatting: Standardizes log format and handles errors robustly.
Configuration: Configurable via a JSON file.
Scalability: Utilizes asynchronous logging and log rotation for high-volume log handling.
Query Interface
Filters: Allows filtering logs based on log level, log string, timestamp, and source.
Advanced Features: Includes date range search and regex-based log string searches.
User Interface: Provides a CLI for querying logs.
Installation
Prerequisites
Python 3.x
pip (Python package installer)
Steps
Clone the repository:

sh
Copy code
git clone https://github.com/your-username/quality-log-control-system.git
cd quality-log-control-system
Install dependencies:

sh
Copy code
pip install -r requirements.txt
Set up the directory structure:
Create the logs directory if it does not exist:

sh
Copy code
mkdir logs
Configure the system:
Modify config.json to set the logging levels and file paths for each API.

Running the Project
Log Ingestor
Run the Log Ingestor:

sh
Copy code
python log_ingestor.py
Check the logs:
Log files will be created in the logs directory (e.g., log1.log, log2.log, log3.log).

Query Interface
Run the Query Interface:

sh
Copy code
python query_interface.py
Query logs:
Follow the prompts to enter the query criteria:

Log level: Enter info, error, or success.
Log string: Enter a substring to search within the log messages.
Start date: Enter a start date in the format YYYY-MM-DD (optional).
End date: Enter an end date in the format YYYY-MM-DD (optional).
Source file: Enter the source log file (e.g., logs/log1.log).
Future Enhancements
Implement a web-based query interface for better usability.
Add real-time log ingestion and querying capabilities.
Implement role-based access control (RBAC) for the query interface.
Identified Issues
The current implementation uses a CLI for querying logs. A web-based UI could enhance usability.
Real-time log ingestion and querying capabilities are not implemented.
Role-based access control (RBAC) for the query interface is not included.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

