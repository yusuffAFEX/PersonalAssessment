import os
from django.conf import settings

from celery import Celery

# Set the default Django settings module for the 'celery' program.
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeatherApp.settings')

app = Celery('WeatherApp')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'send_every_6am': {
        'task': 'weather.tasks.my_scheduled_job',
        'schedule': crontab(minute='*/1')
    }
}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
