from apscheduler.schedulers.background import BackgroundScheduler
from services.weather_service import get_weather
from services.compare_service import check_for_changes
from services.mail_service import send_email
from services.log_service import log_result
from config import DEFAULT_CITY, TO_EMAIL
import json

def weather_job():
    print("🌤️ Hava durumu kontrol ediliyor...")
    try:
        data = get_weather(DEFAULT_CITY)
        changes = check_for_changes(data)
        print("✅ Veri kontrol edildi. "+data['weather'][0]['description']+" "+str(data['main']['temp'])+" "+str(data['weather'][0]['icon']))
        if changes:
            msg = f"Hava durumu değişti!\n\n{changes}"
            send_email("🌤️ Hava Durumu Güncellemesi", msg, TO_EMAIL)
            print("📨 Değişiklik tespit edildi, mail gönderildi.")

        log_result(data)
    except Exception as e:
        print(f" Error: {e}")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(weather_job, "interval", minutes=1)
    scheduler.start()
    print(" Zamanlayıcı başlatıldı (1 dakika aralıkla).")
