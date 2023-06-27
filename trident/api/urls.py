from django.urls import path
from .views import CreateRoomView, RoomView

urlpatterns = [
    path('', RoomView.as_view()),
    path('join', RoomView.as_view()),
    path('create', CreateRoomView.as_view()),
    path('room/<str:roomCode>', RoomView.as_view()),
]