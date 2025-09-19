import os
from celery import Celery
from crewai_client import call_crewai
from task import DEFAULT_PROMPT

broker = os.getenv("REDIS_URL", "redis://localhost:6379/0")
backend = os.getenv("CELERY_RESULT_BACKEND", broker)
celery = Celery("tasks", broker=broker, backend=backend)

@celery.task
def analyze_task(filename, file_bytes, prompt=DEFAULT_PROMPT):
    return call_crewai(file_bytes, filename, prompt)
