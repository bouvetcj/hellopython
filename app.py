#!/usr/bin/python3
import socket
import sys
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
start_time = datetime.now()  # Capture app start time

def get_time_of_day():
    hour = datetime.now().hour
    if hour < 6:
        return "night", "🌙 Good night!"
    elif hour < 12:
        return "morning", "☀️ Good morning!"
    elif hour < 18:
        return "afternoon", "🌤 Good afternoon!"
    else:
        return "evening", "🌆 Good evening!"

@app.route('/')
def home():
    time_of_day, greeting = get_time_of_day()
    stats = {
        "hostname": socket.gethostname(),
        "python_version": sys.version.split()[0],
        "app_start_time": start_time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return render_template('index.html', greeting=greeting, time_of_day=time_of_day, stats=stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
