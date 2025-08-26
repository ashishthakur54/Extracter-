"""
from os import getenv


API_ID = int(getenv("API_ID", "23480065"))
API_HASH = getenv("API_HASH", "32edb7d7fc1523b436109bff8ea061fc")
BOT_TOKEN = getenv("BOT_TOKEN", "8172684751:AAFrKOePs4i_8Zbo3OciESAnP40EVT9cQlQ")
OWNER_ID = int(getenv("OWNER_ID", "8489271683"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8489271683,7760196814").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://savebot:RxxBfvkv1xnGsbPL@cluster0.9zpw7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003057558296"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002887465160"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "23480065"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "32edb7d7fc1523b436109bff8ea061fc")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8172684751:AAFrKOePs4i_8Zbo3OciESAnP40EVT9cQlQ")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("Nooneknowswhoknows_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "8489271683"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8489271683,7760196814").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003057558296"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://savebot:RxxBfvkv1xnGsbPL@cluster0.9zpw7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002887465160"))

