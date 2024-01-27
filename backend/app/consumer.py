# This is equal to the views.py in django
"""
Whenever the app will recieve a message or alert from the
ASGI regarding an event, what function is need to be performed
will be handled by the functions written in the consumer.
"""

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

