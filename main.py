from fastapi import FastAPI, Request
from scheduler import start_scheduler
from contextlib import asynccontextmanager
from scheduler import start_scheduler
from services.weather_service import get_weather
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


#to do: hata yönetimi eksik mi ? ve comparei review et

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield

app = FastAPI(title="Weather Notifier API",lifespan=lifespan)
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/")
async def root():
    return {"message": "Weather Notifier çalışıyor!"}

@app.get("/current-weather")
@limiter.limit("5/minute")
async def current_weather(request : Request,city: str = "Istanbul"):
    data = get_weather(str(city))
    return data