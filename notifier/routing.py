from django.urls import path

from .consumers import EchoConsumer, StatusConsumer

ws_urlpatterns = [
    path('ws/', EchoConsumer.as_asgi()),
    path('ws/status/', StatusConsumer.as_asgi())
]
