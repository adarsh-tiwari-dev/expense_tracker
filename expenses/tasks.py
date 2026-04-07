from celery import shared_task

@shared_task
def send_weekly_summary():
    print("Sending weekly expense summary...")