# Codexbotz # @mrismanaziz

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8153820960:AAFZn_kT-QhK_l-lyESmdPTCSWZBdFJ7Z6Q")

API_ID = int(os.environ.get("API_ID", "27074717"))
API_HASH = os.environ.get("API_HASH", "c91443b748be68477d9ee4995d30fd27")

CHANNEL_DB = int(os.environ.get("CHANNEL_DB", "-1002783872261"))
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://pakeya2:userbot@cluster0.vva0b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

RESTRICT = strtobool(os.environ.get("RESTRICT", "True"))

FORCE_SUB_1 = int(os.environ.get("FORCE_SUB_1", "-1002841696910"))
FORCE_SUB_2 = int(os.environ.get("FORCE_SUB_2", "-1002528277069"))
FORCE_SUB_3 = int(os.environ.get("FORCE_SUB_3", "0"))
FORCE_SUB_4 = int(os.environ.get("FORCE_SUB_4", "0"))

WORKERS = int(os.environ.get("WORKERS", "4"))

START_MESSAGE = os.environ.get(
    "START_MESSAGE",
    "Nape lu {mention}!"
    "\n\n"
    "Jangan spam yee 😹",
)
FORCE_MESSAGE = os.environ.get(
    "FORCE_MESSAGE",
    "Alooo {mention}!"
    "\n\n"
    "Lu harus masuk Channel/Group dulu ya "
    "\n\n"
    "Silhkan masuk dulu",
)

try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")
    
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
DISABLE_BUTTON = strtobool(os.environ.get("DISABLE_BUTTON", "False"))


LOGS_FILE = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOGS_FILE, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)