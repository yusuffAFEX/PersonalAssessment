web: gunicorn WeatherApp.wsgi
celery: celery -A WeatherApp worker -l info --pool-solo
celery-beat: celery -A WeatherApp beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler