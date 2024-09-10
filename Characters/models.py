from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class CharacterImages(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE, related_name='images')
    character_background = models.CharField(max_length=100)
    character_icon = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.character}, {self.character_background}, {self.character_icon}"