from django.urls import path, include
from chat import views

urlpatterns = [
    path("chat", views.chatPage, name="chat-page"),
]