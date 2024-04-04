import requests
import environ

env = environ.Env()

# using the http endpoint to send sms
def send_sms(recipients: list, message: str):
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
        "to": recipients[0],
        "message": message,
        "from": env('AFT_SHORT_CODE')
    }
    response = requests.post(url, headers=headers, data=data)