import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Genshin_Impact.settings")  
django.setup()

from Characters.models import Character, CharacterImages

# Query all characters and their associated images
characters_with_images = Character.objects.select_related('images').all()

# Print character details with associated images
for character in characters_with_images:
    print(f"Character: {character}")
    print(f"Images: {character.images.character_background}, {character.images.character_icon}")

