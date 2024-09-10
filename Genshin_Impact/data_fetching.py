import requests
import os
import shutil

api_root = "https://api.genshin.dev/"
static_path = "Genshin Impact/static/assets/"
images_folder = static_path + "character_cards" # folder name
icons_folder = static_path + "character_icons"
response = requests.get(api_root)
os.makedirs(images_folder, exist_ok=True) # create folder

if response.status_code == 200:
    data = response.json()
    characters = requests.get("https://api.genshin.dev/characters").json() # list of characters
    
    if not os.path.exists("Characters/character_data/characters.txt"):
        with open("characters.txt", "a") as f:
                for character in characters:
                    f.write(character + "\n")
        source = "characters.txt"
        target = "Characters"
        shutil.move(source,target)

    if not os.path.exists(images_folder):
        os.mkdir(images_folder)
    
    if not os.path.exists(icons_folder):
        os.mkdir(icons_folder)

         

    for character in characters:
        character_image = requests.get("https://api.genshin.dev/characters/" + character + "/card").content # binary values
        character_icon = requests.get("https://api.genshin.dev/characters/" + character + "/icon").content

        image_path = os.path.join(images_folder, f"{character}_card")
        if not os.path.exists(f"{image_path}.png"):
            with open(f"{image_path}.png","wb") as f:
                f.write(character_image)
        
        icon_path = os.path.join(icons_folder, f"{character}_icon")
        if not os.path.exists(f"{icon_path}.png"):
             with open(f"{icon_path}.png", "wb") as f:
                f.write(character_icon)
        
else:
    print("Failed")