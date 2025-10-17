# 🌤️ Weather Notifier API

Bu proje, **FastAPI**, **OpenWeather API** ve **SlowAPI** kullanılarak geliştirilen bir hava durumu bildirim sistemidir.  
Uygulama, anlık hava durumunu alır, değişiklikleri kontrol eder, loglar oluşturur ve gerektiğinde e-posta gönderimi yapar.  
Ayrıca **scheduler** ile periyodik görevleri otomatik olarak yürütür.

---

## 🚀 Özellikler

- 🌦️ OpenWeather API üzerinden anlık hava durumu verisi alır  
- 📧 Mail servisi aracılığıyla bilgilendirme gönderir  
- 🕒 Scheduler ile periyodik görevler yürütür  
- 🧾 Loglama ve karşılaştırma servisleri ile önceki verileri takip eder  
- ⚙️ SlowAPI ile istek limiti uygular (5 istek/dakika/IP)  
- 🔐 Ortam değişkenleri ile gizli bilgileri güvenli şekilde yönetir  

---

## 🧩 Proje Yapısı

```bash
WEATHER-NOTIFIER/
├── .env                        # Ortam değişkenleri (API key, e-posta bilgileri)
├── .gitignore                  # .env, __pycache__, .venv gibi dosyaları hariç tutar
├── .venv/                      # Sanal ortam klasörü
├── config.py                   # Ortam değişkenlerini ve yapılandırmayı yükler
├── data/
│   ├── last_weather.json       # Son hava durumu verisi
│   └── weather.log             # Log kayıtları
├── main.py                     # FastAPI uygulaması
├── requirements.txt            # Gerekli bağımlılıklar
├── scheduler.py                # Zamanlayıcı görevleri
├── services/                   # Servis katmanı
│   ├── compare_service.py      # Hava durumu değişikliklerini karşılaştırır
│   ├── log_service.py          # Log işlemlerini yürütür
│   ├── mail_service.py         # E-posta gönderim servisi
│   └── weather_service.py      # OpenWeather API’den veri çeker
└── test.py                     # Test veya debug amaçlı yardımcı dosya
⚙️ Kurulum Adımları
1️⃣ Depoyu klonla
bash
Kodu kopyala
git clone https://github.com/<kullanıcı_adın>/<repo_adın>.git
cd WEATHER-NOTIFIER
2️⃣ Sanal ortam oluştur ve etkinleştir
bash
Kodu kopyala
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
3️⃣ Bağımlılıkları yükle
bash
Kodu kopyala
pip install -r requirements.txt
🔐 Ortam Değişkenleri (.env)
.env dosyasında şu bilgileri bulundurmalısın:

env
Kodu kopyala
OPENWEATHER_API_KEY=YOUR_API_KEY
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
TO_EMAIL=target_email@gmail.com
CITY=Hatay
COUNTRY=TR
.env dosyasını .gitignore içine mutlaka ekle, repoya gönderme.

🧠 API Endpoint’leri
GET /
Basit sağlık kontrolü:

json
Kodu kopyala
{
  "message": "Weather Notifier çalışıyor!"
}
GET /current-weather?city=Istanbul
Belirtilen şehir için OpenWeather API’den hava durumu döner.

Rate limit: 5 istek / dakika / IP

Örnek:

sql
Kodu kopyala
GET http://127.0.0.1:8000/current-weather?city=Hatay
Yanıt:

json
Kodu kopyala
{
  "coord": {"lon": 36.2, "lat": 36.1},
  "weather": [{"description": "açık hava"}],
  "main": {"temp": 22.5, "humidity": 48},
  "name": "Hatay"
}
🧾 Örnek requirements.txt
txt
Kodu kopyala
fastapi==0.115.0
uvicorn==0.30.6
slowapi==0.1.9
requests==2.32.3
python-dotenv==1.0.1
apscheduler==3.10.4
🕒 Scheduler (Zamanlayıcı)
scheduler.py dosyası, uygulama başlarken otomatik olarak devreye girer.
Belirli aralıklarla compare_service ve mail_service fonksiyonlarını tetikleyebilir.

Scheduler, main.py içindeki lifespan context manager’ı tarafından başlatılır:

python
Kodu kopyala
@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield
⚠️ Hata Yönetimi
RateLimitExceeded → 429 kodu döner (çok fazla istek)

HTTPError → OpenWeather API isteği başarısız olursa raise_for_status() yakalar

requests.exceptions.RequestException yakalanarak hata mesajı döndürülür

Loglama servisi hata durumlarını weather.log dosyasına yazar

🧑‍💻 Geliştirici
Mehmet Karadana
📧 karadanam519@gmail.com
🌍 Proje: GlobalTour / Weather Notifier API

🪄 Lisans
Bu proje MIT lisansı ile lisanslanmıştır.