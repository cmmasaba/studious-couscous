import requests
import environ
from celery import shared_task

env = environ.Env()

# using the http endpoint to send sms
@shared_task(bind=True, max_retries=3, default_retry_interval=5*60)
def send_sms(self, recipient: str, message: str):
    """
    Args:
        recipient (list): A list of phone number(s) to send the message to.
        message (str): The message to send.
    """
    try:
        url = "https://api.sandbox.africastalking.com/version1/messaging"
        headers = {
            "apiKey": env('AFT_API_KEY'),
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }


        data = {
            "username": env('AFT_USERNAME'),
            "to": recipient,
            "message": message,
            "from": env('AFT_SHORT_CODE')
        }
        requests.post(url, headers=headers, data=data)
    except requests.exceptions.RequestException as exc:
        raise self.retry(exc=exc)