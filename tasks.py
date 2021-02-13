from celery import Celery
from celery.schedules import crontab
from main import main

app = Celery('tasks', broker='redis://127.0.0.1:6379/0')

app.conf.timezone = 'Asia/Jakarta'
app.conf.beat_schedule = {
    # Executes every Week
    'add-every-week': {
        'task': 'tasks.run_main',
        'schedule': crontab(minute=0, hour='8-17'),
    },
}


@app.task
def run_main():
	main()
