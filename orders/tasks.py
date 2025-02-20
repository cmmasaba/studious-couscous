import requests
import environ
from celery import shared_task

env = environ.Env()

# using the http endpoint to send sms
@shared_task
def send_sms(recipient: str, message: str):
    """
    Args:
        recipient (list): A list of phone number(s) to send the message to.
        message (str): The message to send.
    """
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
    response = requests.post(url, headers=headers, data=data)