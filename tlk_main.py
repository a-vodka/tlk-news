import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os
import time
from langdetect import detect

# Telegram channel URL (replace with your target channel)
CHANNEL_URL = "https://t.me/s/tlknewsua"

def get_latest_messages():
    """Scrape latest messages from Telegram web version"""
    try:
        # set short timeouts to prevent freezing
        response = requests.get(CHANNEL_URL, timeout=(5, 10))
        response.raise_for_status()

    except requests.exceptions.Timeout:
        print("⚠️ Request timed out.")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Connection error: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all message elements
    messages = soup.find_all("div", class_="tgme_widget_message_text")

    if not messages:
        print("No messages found.")
        return None

    for tag in messages[-1].find_all(["i", "a", "tg-emoji"]):
        tag.decompose()

    latest_message = messages[-1].get_text("\n", strip=True)
    return latest_message

def text_to_speech(text):
    """Convert text to speech and play it"""
    try:
        lang = detect(text)  # autodetect language
        print(f"Detected language: {lang}")
    except Exception:
        lang = "ru"

    if (lang not in ["ru", "uk", "en"]):
        lang = "ru"

    text = "🔔 🚨. " + text # add attention sound 
    #Convert text to speech and play it
    tts = gTTS(text=text, lang=lang)  # Change 'uk' to 'en' for English, 'ru' for Russian, etc.
    filename = "message.mp3"
    tts.save(filename)

    # Play the generated audio file (works on Windows/macOS/Linux)
    os.system(f"start {filename}" if os.name == "nt" else f"mpv --volume=135 {filename}")

    return filename

if __name__ == "__main__":
    print("Fetching messages...")
    
    last_text = ""
    
    while True:
        latest_message = get_latest_messages()
        
        if latest_message and latest_message != last_text:
            print(f"New message:\n{latest_message}")
            text_to_speech(latest_message)
            last_text = latest_message
        
        time.sleep(30)  # Check for new messages every 60 seconds
