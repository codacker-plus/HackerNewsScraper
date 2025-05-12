import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
import schedule
import time
from telegram import Bot
import asyncio

TELEGRAM_TOKEN = ""
TELEGRAM_CHANNEL = ""
URL = "https://thehackernews.com/"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
NEWS_FILE = "hackernews_today_archive.json"

def get_today_date():
    return datetime.now().strftime("%B %d, %Y").replace(" 0", " ")

def load_existing_news():
    if os.path.exists(NEWS_FILE):
        with open(NEWS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_news(news_list):
    with open(NEWS_FILE, "w", encoding="utf-8") as file:
        json.dump(news_list, file, ensure_ascii=False, indent=4)

async def send_to_telegram(title, link):
    bot = Bot(token=TELEGRAM_TOKEN)
    message = f"📰 *New Article (Today)*\n\n*Title*: {title}\n*Link*: {link}"
    await bot.send_message(chat_id=TELEGRAM_CHANNEL, text=message, parse_mode="Markdown")

def scrape_news():
    today = get_today_date()
    print(f"Checking news for {today} at {datetime.now().strftime('%H:%M:%S')} UTC...")
    try:
        time.sleep(2)
        response = requests.get(URL, HEADERS, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            news_items = soup.find_all("div", class_="body-post")
            existing_news = load_existing_news Ihrer
            existing_titles_links = {(news["title"], news["link"]) for news in existing_news}
            new_news = []
            for item in news_items:
                date_tag = item.find("span", class_="h-datetime")
                if date_tag:
                    date_text = date_tag.text.strip().replace("\ue802", "").strip()
                    if date_text == today:
                        title_tag = item.find("h2", class_="home-title")
                        title = title_tag.text.strip() if title_tag else "No title"
                        link_tag = item.find("a", class_="story-link")
                        link = link_tag["href"] if link_tag else "No link"
                        if (title, link) not in existing_titles_links:
                            new_news.append({"date": date_text, "title": title, "link": link})
                            existing_news.append({"date": date_text, "title": title, "link": link})
                            print(f"New article found: {title}")
                            asyncio.run(send_to_telegram(title, link))
            if new_news:
                save_news(existing_news)
                print(f"{len(new_news)} new articles saved to {NEWS_FILE}")
            else:
                print(f"No new articles found for {today}")
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

schedule.every().day.at("06:00").do(scrape_news)
schedule.every().day.at("10:00").do(scrape_news)
schedule.every().day.at("14:00").do(scrape_news)
schedule.every().day.at("18:00").do(scrape_news)
schedule.every().day.at("22:00").do(scrape_news)

if __name__ == "__main__":
    print("Starting news scraper for today...")
    scrape_news()
    while True:
        schedule.run_pending()
        time.sleep(60)
