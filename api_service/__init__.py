# Initialize the Celery app whenever Django starts-up
from .celery import app as celery_app