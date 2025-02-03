"""
from os import getenv


API_ID = int(getenv("API_ID", "21049061"))
API_HASH = getenv("API_HASH", "24c5b0eac6f1217b7fce9d90f8edb4ea")
BOT_TOKEN = getenv("BOT_TOKEN", "7274169562:AAGXKlTt6gXz9no8Noq7iNwDd9FN38H7fGs")
OWNER_ID = int(getenv("OWNER_ID", "2055358158"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2055358158 2112898623").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://aashish:34ybMaMgrkMa3Jmd@cluster0.8mooi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002248941888"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002484191547"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

