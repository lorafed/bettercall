from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

def scheduled_task():
    print("This task runs every minute")

scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_task, 'interval', minutes=1)
scheduler.start()

@app.route('/')
def index():
    return "Welcome to the fundraising app!"

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
