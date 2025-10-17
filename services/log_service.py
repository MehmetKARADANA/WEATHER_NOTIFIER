from datetime import datetime
import json

#Note json.dumps(data,ensure_ascii=False,indent=2)

def log_result(data):
    with open("data/weather.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] Veri kontrol edildi: weather : {data['weather'][0]}\n")
        

