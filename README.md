HackerNews Scraper
This Python script scrapes the latest articles from The Hacker News published on the current day and sends them to a specified Telegram channel. The script runs on a schedule to check for new articles at specific times daily.
About the Script
The HackerNewsScraper script is designed to:

Fetch articles from The Hacker News website for the current date.
Store the articles in a JSON file (hackernews_today_archive.json) to avoid duplicates.
Send new articles to a Telegram channel using a Telegram bot.
Run automatically on a daily schedule at 06:00, 10:00, 14:00, 18:00, and 22:00 UTC.

The script uses web scraping with BeautifulSoup and requests, schedules tasks with schedule, and communicates with Telegram via the python-telegram-bot library.
Requirements

Python 3.6 or higher
A Telegram bot token and channel ID (see Setup for details)

Python Dependencies
The following Python libraries are required:
requests
beautifulsoup4
python-telegram-bot
schedule

Installation

Clone the Repository:
git clone https://github.com/your-username/HackerNewsScraper.git
cd HackerNewsScraper


Set Up a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Create a Telegram Bot:

Open Telegram and search for @BotFather.
Start a chat and send /newbot to create a new bot.
Follow the instructions to name your bot and get the Telegram Bot Token.
Add the bot to your Telegram channel and get the Channel ID (you can use @username_to_id_bot to find the channel ID).


Set Environment Variables:

Create a .env file in the project directory or set environment variables directly.
Add your Telegram bot token and channel ID:TELEGRAM_TOKEN=your-telegram-bot-token
TELEGRAM_CHANNEL=your-telegram-channel-id


Alternatively, modify the scraper.py file to include these values directly (not recommended for security reasons).



Usage

Run the Script:
python scraper.py


What Happens:

The script immediately checks for new articles on The Hacker News for the current date.
It saves the articles to hackernews_today_archive.json.
New articles are sent to the specified Telegram channel with the article title and link.
The script continues running and checks for new articles daily at 06:00, 10:00, 14:00, 18:00, and 22:00 UTC.


Stop the Script:

Press Ctrl+C to stop the script.



Notes

Security: Never commit your TELEGRAM_TOKEN or TELEGRAM_CHANNEL to the repository. Use environment variables or a .env file (which is ignored by .gitignore).
Scheduling: The script uses the schedule library to run at specified times. Ensure your system clock is set to UTC or adjust the schedule times accordingly.
Deployment: To run the script continuously (e.g., on a server), consider using a cloud platform like Heroku, AWS, or a VPS with cron or systemd for scheduling.
Error Handling: The script includes basic error handling for network issues. Check the console output for logs.

Contributing
Feel free to fork this repository, make improvements, and submit pull requests. For bug reports or feature requests, please open an issue.
License
This project is licensed under the MIT License. See the LICENSE file for details.
