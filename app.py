from flask import Flask
from flask_apscheduler import APScheduler
import requests

app = Flask(__name__)

class Config:
    SCHEDULER_API_ENABLED = True

app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)

@scheduler.task("interval", id="hit_api", seconds=14)
def hit_api():
    try:
        res = requests.get("https://example.com/api/health", timeout=5)
        print("API hit:", res.status_code)
    except Exception as e:
        print("API error:", e)

scheduler.start()

@app.route("/")
def home():
    return "Flask app running"
