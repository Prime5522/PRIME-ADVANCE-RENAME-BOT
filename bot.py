from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

bot = Client(
    "Renamer",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

try:
    if STRING:
        apps = [Client2, bot]
        for app in apps:
            app.start()
            logging.info(f"{app} started successfully.")
        idle()
    else:
        bot.run()
except Exception as e:
    logging.error(f"An error occurred: {e}")
finally:
    for app in apps:
        app.stop()
        logging.info(f"{app} stopped successfully.")
