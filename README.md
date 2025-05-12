HackerNews Scraper
A Python script to scrape articles from The Hacker News published on the current day and send them to a Telegram channel.
📖 About the Script
This script automates the process of:

Fetching articles from The Hacker News for the current date.
Saving articles to a JSON file (hackernews_today_archive.json) to prevent duplicates.
Sending new articles to a Telegram channel with their title and link.
Running on a schedule at 06:00, 10:00, 14:00, 18:00, and 22:00 UTC.

It uses BeautifulSoup for web scraping, requests for HTTP requests, schedule for task scheduling, and python-telegram-bot for Telegram integration.
📋 Requirements

Python 3.6 or higher
A Telegram bot token and channel ID (see Setup)

Python Dependencies
Install the required libraries listed in requirements.txt:
requests==2.32.3
beautifulsoup4==4.12.3
python-telegram-bot==21.5
schedule==1.2.2

🛠️ Installation
Follow these steps to set up the project:

Clone the Repository:
git clone https://github.com/your-username/HackerNewsScraper.git
cd HackerNewsScraper


Set Up a Virtual Environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Create a Telegram Bot:

Open Telegram and start a chat with @BotFather.
Send /newbot to create a bot and follow the instructions to get your Telegram Bot Token.
Add the bot to your Telegram channel and get the Channel ID (use @username_to_id_bot to find it).


Configure Environment Variables:

Create a .env file in the project root or set environment variables.

Add your Telegram credentials:
TELEGRAM_TOKEN=your-telegram-bot-token
TELEGRAM_CHANNEL=your-telegram-channel-id


Alternatively, modify scraper.py to include these values (not recommended for security).




🚀 Usage

Run the Script:
python scraper.py


What Happens:

The script checks for new articles on The Hacker News for the current date.
Articles are saved to hackernews_today_archive.json.
New articles are sent to your Telegram channel with the title and link.
The script runs daily at 06:00, 10:00, 14:00, 18:00, and 22:00 UTC.


Stop the Script:

Press Ctrl+C to stop the script.



🔧 Example Code Snippet
Here’s a snippet from scraper.py showing how articles are sent to Telegram:
async def send_to_telegram(title, link):
    bot = Bot(token=TELEGRAM_TOKEN)
    message = f"📰 *New Article (Today)*\n\n*Title*: {title}\n*Link*: {link}"
    await bot.send_message(chat_id=TELEGRAM_CHANNEL, text=message, parse_mode="Markdown")

⚠️ Notes

Security: Do not commit TELEGRAM_TOKEN or TELEGRAM_CHANNEL to the repository. Use environment variables or a .env file (ignored by .gitignore).
Scheduling: The script uses the schedule library. Ensure your system clock is set to UTC or adjust the schedule times.
Deployment: For continuous execution, deploy on a server (e.g., Heroku, AWS) or use cron/systemd for scheduling.
Error Handling: The script logs errors to the console for network or parsing issues.

🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add new feature").
Push to the branch (git push origin feature-branch).
Open a pull request.

For bugs or feature requests, please open an issue.
📜 License
This project is licensed under the MIT License. See Guiding Principles (see LICENSE file for details).
