from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from utils import message_creater
from line_bot_pushNotion.line_message import LineMessage

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        message = data['message']
        reply_token = data['replyToken']
        createMessage = message_creater.create_single_text_message(message['text'])
        line_message = LineMessage(createMessage)
        line_message.reply(reply_token)
        return HttpResponse("ok")
