"""
from os import getenv


API_ID = int(getenv("API_ID", "22475741"))
API_HASH = getenv("API_HASH", "1a217be71a0225e0a678af286c211f8a")
BOT_TOKEN = getenv("BOT_TOKEN", "7347353498:AAGgNzcVVGcEUoZSYAhghggmKpgX8_XUYvs")
OWNER_ID = int(getenv("OWNER_ID", "6562642609"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6050277919 2112898623").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002409732732"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002175698132"))

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

