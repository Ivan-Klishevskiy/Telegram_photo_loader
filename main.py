import os
from telethon import TelegramClient, events
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterVideo

#credentials from my.telegram.org
api_id = ''
api_hash = ''

# Connect to Telegram as a regular user
client = TelegramClient('anon', api_id, api_hash)
client.start()

# Directory to save media
SAVE_PATH = "downloaded_media"

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

@client.on(events.NewMessage(pattern='/download_media'))
async def download_media(event):
    chat_id = event.chat_id

    # Downloading photos
    async for message in client.iter_messages(chat_id, filter=InputMessagesFilterPhotos()):
        print("Downloading photo...")
        await message.download_media(SAVE_PATH)
        print("Photo successfully downloaded!")

    # Downloading videos
    async for message in client.iter_messages(chat_id, filter=InputMessagesFilterVideo()):
        print("Downloading video...")
        await message.download_media(SAVE_PATH)
        print("Video successfully downloaded!")

    await event.respond(f'Media from this group have been successfully downloaded!')

client.run_until_disconnected()
