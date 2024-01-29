# This is equal to the views.py in django
"""
Whenever the app will recieve a message or alert from the
ASGI regarding an event, what function is need to be performed
will be handled by the functions written in the consumer.
"""

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

class MyJsonConsumer(JsonWebsocketConsumer):
    """
    Using jsonwebsocket as our message will be json decoded and encoded
    by them automatically
    """
    pass

