from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict, List
import json
import os
from datetime import datetime

app = FastAPI()

DATA_FILE = "data.json"

# מודל לקבלת JSON
class Payload(BaseModel):
    data: Dict[str, Any]

# פונקציה לקריאת נתונים
def read_data() -> List[Dict[str, Any]]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# פונקציה לכתיבת נתונים
def write_data(data: List[Dict[str, Any]]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Endpoint 1: POST
@app.post("/append")
def append_payload(payload: Payload):
    data = read_data()
    # מוסיפים תאריך ושעה אוטומטית
    entry = {
        "timestamp": datetime.now().isoformat(),
        "data": payload.data
    }
    data.append(entry)
    write_data(data)
    return {"status": "success", "entry": entry}

# Endpoint 2: GET
@app.get("/last")
def get_last_entries():
    data = read_data()
    return data[-10:]  # מחזיר את 10 הרשומות האחרונות
