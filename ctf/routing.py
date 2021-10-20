from django.urls import re_path
from .consumer import CastConsumer

websocket_urlpatterns = [
    re_path(r'ws/', CastConsumer.as_asgi())
]