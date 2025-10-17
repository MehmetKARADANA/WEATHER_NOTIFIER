import json
import os

DATA_PATH = "data/last_weather.json"

def check_for_changes(new_data: dict):
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as f:
            json.dump(new_data, f, indent=4)
        return "İlk veri kaydedildi."

    with open(DATA_PATH, "r") as f:
        old_data = json.load(f)

    changes = []
    fields = ["temp", "humidity", "description"]

    old_main = old_data.get("main", {})
    new_main = new_data.get("main", {})
    old_desc = old_data["weather"][0]["description"]
    new_desc = new_data["weather"][0]["description"]

    if old_main.get("temp") != new_main.get("temp"):
        changes.append(f"Sıcaklık değişti: {old_main.get('temp')}°C → {new_main.get('temp')}°C")

    if old_main.get("humidity") != new_main.get("humidity"):
        changes.append(f"Nem değişti: {old_main.get('humidity')}% → {new_main.get('humidity')}%")

    if old_desc != new_desc:
        changes.append(f"Hava durumu değişti: {old_desc} → {new_desc}")

    if changes:
        with open(DATA_PATH, "w") as f:
            json.dump(new_data, f, indent=4)
        return "\n".join(changes)

    return None
