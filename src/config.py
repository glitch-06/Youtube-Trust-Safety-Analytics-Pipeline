import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "youtube_trustshield",
    "user": "postgres",
    "password": "Dumbo#2409"
}

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
print(YOUTUBE_API_KEY)