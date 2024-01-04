import os

# Pyrogram API credentials
API_ID = int(os.environ.get("API_ID", 9149961))
API_HASH = os.environ.get("API_HASH", "de667e7f26d7c58df684bfeb6189f1fd")

# Bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6631133057:AAHIgGeyAQK-E8mxFMYwK3z6qfquzPWUHhg")

# Pyrogram session name
SESSION_NAME = os.environ.get("SESSION_NAME")

# MongoDB URI (if you're using MongoDB)
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://adv:adv@cluster0.txud8.mongodb.net/?retryWrites=true&w=majority")
