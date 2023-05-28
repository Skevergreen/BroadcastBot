import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5784419367:AAHahvpKTqaPvws-f7ZT7wNGDJrOq8MYdLY")
API_ID = int(os.environ.get("API_ID", "23937617"))
API_HASH = os.environ.get("API_HASH", "cdc408c8bf00c9c2219fee9cd585bbda")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001637312289"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1412758888").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://NewETY:NewETY@cluster0.lcrsgl0.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
