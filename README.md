# tlk-news

A Python-based script that scrapes the [tlknewsua Telegram channel](https://t.me/s/tlknewsua) for raid alerts in Ukraine and converts them into speech using Google Text-to-Speech (gTTS).  
This tool is designed for automated monitoring and audio notification of air raid alerts.

---

## Features
- Scrapes Telegram channel posts directly from `https://t.me/s/tlknewsua`.
- Detects whether a message was posted silently or with sound.
- Auto-detects message language for correct speech synthesis.
- Converts selected messages into `.mp3` audio using gTTS.
- Includes simple shell script for quick execution.

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/a-vodka/tlk-news.git
   cd tlk-news
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Requirements include:
   - `requests`
   - `beautifulsoup4`
   - `gtts`

3. **Run the script**
   ```bash
   python tlk_main.py
   ```

   Or use the provided shell wrapper:
   ```bash
   ./run_script.sh
   ```

---

## Usage

- The script fetches the latest messages from the channel and checks if they arrived with sound notification.  
- Messages with sound are processed, converted to `.mp3`, and saved as `message.mp3`.  
- Language is automatically detected for correct TTS output.

---

## Example Output

After running the script, you will get an audio file like:

```
message.mp3
```

- This file contains the spoken version of the latest alert.
- Example transcript of an alert:  
  ```
  "Тревога по баллистике с КуНР"
  ```
- The audio will be automatically generated in the detected language (Ukrainian, English, etc.).

---

## File Structure

- `tlk_main.py` — main script for scraping and TTS conversion.
- `requirements.txt` — Python dependencies.
- `run_script.sh` — convenience script for running.
- `message.mp3` — generated sample audio output.

---

## Disclaimer
This project is for educational and informational purposes only.  
It is not affiliated with Telegram, the `tlknewsua` channel, or any official alert system.  
Use at your own risk.