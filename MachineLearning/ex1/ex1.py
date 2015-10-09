from celery import Celery


# redis://:password@hostname:port/db_number
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
app = Celery('tasks', broker='redis://localhost:6379/0',
             backend=CELERY_RESULT_BACKEND)

app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Europe/Oslo',
    CELERY_ENABLE_UTC=True,
)

@app.task
def add(x, y):
    return x + y