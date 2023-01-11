from django.urls import path, include
from chat.consumers import ChatConsumer

websocker_tuelpatterns = [
    path('', ChatConsumer.as_asgi())
]