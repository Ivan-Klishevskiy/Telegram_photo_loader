# Telegram Media Downloader
## Overview
**Telegram Media Downloader** is a Python-based utility that allows users to automatically download all photos and videos from a specified Telegram group. Whether you're an admin looking to backup media from your group or a member wanting to save memories, this tool makes the process seamless and efficient.

## Installation
1. Clone the Repository:
```
git clone https://github.com/Ivan-Klishevskiy/Telegram_photo_loader.git
cd Telegram_photo_loader
```


2. Install the Dependencies:
```
pip install telethon
```

3. Set up your "api_id" and "api_hash" (you can get that from my.telegram.org.)

## Usage
1. Run the script:
```
python main.py
```

2. Add your user to the Telegram group from which you want to download media.
3. Send the '/download_media' command in the group.
4. The script will start downloading all photos and videos from the group to the 'downloaded_media' directory.
