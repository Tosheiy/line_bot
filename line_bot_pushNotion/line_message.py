from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout
import json
import os
from dotenv import load_dotenv

load_dotenv()

REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"
ACCESSTOKEN = os.environ['API_KEY_LINE']
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ACCESSTOKEN
}

class LineMessage():
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token):
        body = {
            'replyToken': reply_token,
            'messages': self.messages
        }
        try:
            response = requests.request("POST", REPLY_ENDPOINT_URL, data=json.dumps(body).encode(), headers=HEADER)
            print(response.text)
            return "success"
        except ConnectionError as CE:
            print("Connection Error:", CE)
        except HTTPError as HE:
            print("HTTP Error:",HE)
        except Timeout as TO:
            print("Timeout Error:", TO)
        except RequestException as RE:
            print("Request Exception:", RE)
