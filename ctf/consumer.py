import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from foresight_web.settings import *
from .generator import generator

class CastConsumer(WebsocketConsumer):
    def connect(self):

        self.group_name = GROUP_NAME
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_jason = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'cast',
                'message': generator(text_data_jason['message']),
            }
        )

    def cast(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
