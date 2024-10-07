from django.shortcuts import render, HttpResponse
from Characters.models import Character  
import json

def characters(request):
    character_data = Character.objects.select_related('images').all()
    characters = {character.name.strip().replace("-"," ").title(): {"icon":character.images.character_icon,"link_name":character.name} for character in character_data}
    return render(request, "characters.html", {"characters":characters})

def character(request,character):
    character_data = Character.objects.filter(name=character).first()

    if character_data is not None:
        background = character_data.images.character_background
    else:
        return render(request, "error.html")
    character_name = tidy_string(character)
    
    return render(request, "character.html", {"character_name":character_name, "background":background})

def tidy_string(string: str) -> str:
    return string.replace("-", " ").title()