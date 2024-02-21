import africastalking
import environ
import requests

env = environ.Env()

africastalking.initialize(
    username=env('AFT_USERNAME'),
    api_key=env('AFT_API_KEY'),
)

class send():
    sms = africastalking.SMS
    def sending(self, recipients: list, message: str):
        """Send an SMS to the recipient(s) with the message and sender name provided.
        
        Args:
            recipient (list): A list of phone number(s) to send the message to.
            message (str): The message to send.
        """
        
        try:
            # my Africa's Talking short code is 17117
            response = self.sms.send(message, recipients, env('AFT_SHORT_CODE'))
            status = response['SMSMessageData']['Recipients'][0]['status']
            if status == 'Success':
                print("Message sent successfully.")
            else:
                print(f"Message failed with error: {response}")
        except Exception as e:
            print(f"Encountered an error while sending: {e}")


def send_sms(recipients: list, message: str):
    """
    Args:
        recipient (list): A list of phone number(s) to send the message to.
        message (str): The message to send.
    """
    # send().sending(recipients, message)
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
    with open ('smsresponse.txt', 'w') as file:
        file.write(response.text)