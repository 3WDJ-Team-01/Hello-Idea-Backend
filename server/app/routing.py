from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<chat_id>/', consumers.ChatConsumer),
    path('ws/test/<notify_id>/', consumers.NotificationConsumer),
]