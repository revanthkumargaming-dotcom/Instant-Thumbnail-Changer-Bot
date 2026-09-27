# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
import os
import random
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
# Bot Configuration
API_TOKEN = os.environ.get("API_TOKEN", "8814211584:AAEHgp1JJaBHmKYvI9EcnmbN3QRnlaFIFfM")
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
# MongoDB
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://rupamedical:dQv9oKG7QK93BkIh@james.oufkybu.mongodb.net/?appName=james")
DB_NAME = "thumbnail_bot"
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
# Owner/Admin
OWNER_ID = int(os.environ.get("OWNER_ID", "6334669810"))
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
# UI URLs - Multiple images that rotate randomly
# Use DIRECT image URLs (https://i.ibb.co/...) not page URLs (https://ibb.co/...)
START_PICS = [
    imgbb:
"https://ibb.co/WSVrn3p"
"https://ibb.co/YSTGnsR"
"https://ibb.co/SX5qMMdM"
"https://ibb.co/0jx7rCRD"
"https://ibb.co/KjSRWFqw"
"https://ibb.co/dw9rrNsz"
"https://ibb.co/B5dK7gkm"
"https://ibb.co/TD8BXzTS"
"https://ibb.co/G4LwBrXr"
"https://ibb.co/NdYHX7D4"
"https://ibb.co/TxWkpRTw"
"https://ibb.co/DDGBGqRg"
"https://ibb.co/k6HvSxBD"
"https://ibb.co/rf5vNWMh"
"https://ibb.co/NgFZ5rkY"
"https://ibb.co/fGP1RjH2"
"https://ibb.co/WpV0WR6S"
"https://ibb.co/hRxsFhJT"
"https://ibb.co/RTCdQ4Lp"
"https://ibb.co/YFhtypkH"
"https://ibb.co/93ts3Mp6"
"https://ibb.co/hF0GtXYn"
"https://ibb.co/pBdphMnJ"
"https://ibb.co/C3Y9w0KH"
"https://ibb.co/PzswTb1Z"
"https://ibb.co/20kFGVLT"
"https://ibb.co/MDyT6cZQ"
"https://ibb.co/1YSJc4pd"
"https://ibb.co/1GXhs2fD"
"https://ibb.co/8447HnWs"
"https://ibb.co/dw0KYZDS"
    # Add more direct image URLs here
]
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
CHANNEL_URL = os.environ.get("CHANNEL_URL", "https://t.me/BUSTERS_OFCL")
DEV_URL = os.environ.get("DEV_URL", "https://t.me/legendof1st")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))  # e.g., -100xxxxxxxxxxxx
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat

def get_random_pic() -> str:
    """Get a random image from START_PICS."""
    if START_PICS:
        return random.choice(START_PICS)
    return None
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
