import os

# Pyrogram API credentials
API_ID = int(os.environ.get("API_ID", 20781152))
API_HASH = os.environ.get("API_HASH", "0781163b5caac00db3268444e688d9e7")

# Bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6799627176:AAEb7ITggFCsQw47YEMt2l5e66Lrgq-BASQ")

# Pyrogram session name
SESSION_NAME = os.environ.get("SESSION_NAME")

# MongoDB URI (if you're using MongoDB)
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://adv:adv@cluster0.txud8.mongodb.net/?retryWrites=true&w=majority")
