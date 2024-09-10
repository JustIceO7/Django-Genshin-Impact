from django.urls import path
from . import character_views

urlpatterns = [
    path("", character_views.characters, name='characters'),
    path("<str:character>/", character_views.character, name='character'),
]