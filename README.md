# apptrana-siem-log-collector
A Python-based automation toolkit to fetch attack logs from the Indusface AppTrana WAF portal using its REST API and store them locally for SIEM integration or analysis.

📌 Overview

This project consists of two scripts that work together:

[1] Generate_AuthToken.py: Authenticates with the AppTrana API and saves the Bearer token locally.

[2] Fetch_AttackLogs.py: Uses the saved token to fetch attack logs for the last 5 minutes and writes them to daily log files
  
These scripts are designed to be scheduled (e.g., via Windows Task Scheduler or cron) to continuously pull WAF attack data into a local SIEM pipeline.

🗂️ Project Structure
     
    apptrana-siem-log-collector
    
    ├── Generate_AuthToken.py     # Step 1: Generate and store auth token
    ├── Fetch_AttackLogs.py       # Step 2: Fetch and log attack data
    ├── README.md
    └── logs/                     # Auto-created folder for output logs
    ├── Indusface.ini             # Stores the active Bearer token
    ├── indusface-YYYY-MM-DD.log  # Daily attack log files
    └── Error.log                 # Error tracking

⚙️ Prerequisites

    Python 3.7+
    requests library

Install dependencies:

    pip install requests

🔧 Configuration

Before running, update the following variables in "Generate_AuthToken.py":

    pythonLog_Folder = r'path\to\your\log\folder'   # Where logs and token will be stored
    API_ID     = 'your_api_id'
    API_Key    = 'your_api_key'
    And update Log_Folder in Fetch_AttackLogs.py to match the same path.

⚠️ Important: Never commit your actual API_ID or API_Key to a public repository. Use environment variables or a .env file for production use.


🚀 Usage

  Step 1 — Generate Auth Token
  
  Run this first to authenticate and save the token:
  
    python Generate_AuthToken.py
    
  This will create/update Indusface.ini with a fresh Bearer token.
  
  Step 2 — Fetch Attack Logs
  
  Run this to pull the latest attack data from AppTrana:
  
    python Fetch_AttackLogs.py
  Logs will be saved to indusface-YYYY-MM-DD.log in your configured log folder.

🕐 Automating with Task Scheduler (Windows)

To run both scripts every 24 hour & 5 minutes:

    Open Task Scheduler → Create Basic Task
    Set trigger: Every 24 hour & 5 minutes
    Action: Run python Generate_AuthToken.py for every 24 hour & Fetch_AttackLogs.py for every 5 mins.

Make sure the working directory is set to the project folder


📄 Log Format

Each line in the daily log file represents one attack entry returned by the AppTrana API:

    {'attack_type': 'SQLi', 'src_ip': '1.2.3.4', 'timestamp': ..., ...}
Errors are logged to Error.log with timestamps:

    14:32:01   ConnectionError: ...

🔒 Security Note

This project uses API key-based authentication. For better security in production:

    Store credentials in environment variables
    Add Indusface.ini and *.log to .gitignore

👤 Author

Meet Pandya

MSS Engineer — Indusface Private Limited

[LinkedIn](https://www.linkedin.com/in/meet-pandya-soc/)

📃 License

This project is for internal/personal use. Not affiliated with or officially endorsed by Indusface Pvt. Ltd.
