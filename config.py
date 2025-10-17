import os
from dotenv import load_dotenv

load_dotenv()


OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")
TO_EMAIL = os.getenv("TO_EMAIL")


SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
DEFAULT_CITY = os.getenv("CITY", "Istanbul")


if not OPENWEATHER_API_KEY:
    raise ValueError(" OPENWEATHER_API_KEY bulunamadı. Lütfen .env dosyasını kontrol et.")
