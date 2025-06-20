## Federal Register RSS Alert Monitor
This project monitors the Federal Register via its RSS feed and automatically triggers alerts when new entries are published.

It includes:

✅ A scraper to check for the latest policy entries

✅ SQLite database to store and track what's already been seen

✅ Email notifications for new entries

✅ Optional test mode with alert_tripper to simulate entries

⚙️ Technologies Used
Python 3

SQLite

APScheduler (for scheduled checks)

smtplib (for email alerts)

RSS feed from federalregister.gov

🚀 Quick Start
bash
Copy
Edit
git clone https://github.com/yourusername/federal-rss-alert.git
cd federal-rss-alert
pip install -r requirements.txt
python app.py
You can also run test_main.py to simulate an alert and verify the full pipeline.

🛠️ Todo
Add frontend dashboard to display current alerts

Support for additional policy sources

Refine email formatting / batching


