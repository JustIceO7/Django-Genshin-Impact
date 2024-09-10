import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Genshin_Impact.settings") 

django.setup()

from Characters.models import Character, CharacterImages

character_image_data = {
    "albedo": ["None", "albedo_icon.png"],
    "aloy": ["None", "aloy_icon.png"],
    "amber": ["None", "amber_icon.png"],
    "arataki-itto": ["None", "arataki-itto_icon.png"],
    "ayaka": ["Ayaka.mp4", "ayaka_icon.png"],
    "ayato": ["None", "ayato_icon.png"],
    "barbara": ["None", "barbara_icon.png"],
    "beidou": ["None", "beidou_icon.png"],
    "bennett": ["None", "bennett_icon.png"],
    "chongyun": ["None", "chongyun_icon.png"],
    "collei": ["None", "collei_icon.png"],
    "diluc": ["None", "diluc_icon.png"],
    "diona": ["None", "diona_icon.png"],
    "eula": ["None", "eula_icon.png"],
    "fischl": ["None", "fischl_icon.png"],
    "ganyu": ["None", "ganyu_icon.png"],
    "gorou": ["None", "gorou_icon.png"],
    "hu-tao": ["None", "hu-tao_icon.png"],
    "jean": ["None", "jean_icon.png"],
    "kaeya": ["None", "kaeya_icon.png"],
    "kazuha": ["None", "kazuha_icon.png"],
    "keqing": ["None", "keqing_icon.png"],
    "klee": ["None", "klee_icon.png"],
    "kokomi": ["None", "kokomi_icon.png"],
    "kuki-shinobu": ["None", "kuki-shinobu_icon.png"],
    "lisa": ["None", "lisa_icon.png"],
    "mona": ["None", "mona_icon.png"],
    "ningguang": ["None", "ningguang_icon.png"],
    "noelle": ["None", "noelle_icon.png"],
    "qiqi": ["None", "qiqi_icon.png"],
    "raiden-shogun": ["Raiden-Shogun.mp4", "raiden-shogun_icon.png"],
    "razor": ["None", "razor_icon.png"],
    "rosaria": ["None", "rosaria_icon.png"],
    "sara": ["None", "sara_icon.png"],
    "sayu": ["None", "sayu_icon.png"],
    "shenhe": ["Shenhe.mp4", "shenhe_icon.png"],
    "shikanoin-heizou": ["None", "shikanoin-heizou_icon.png"],
    "sucrose": ["None", "sucrose_icon.png"],
    "tartaglia": ["None", "tartaglia_icon.png"],
    "thoma": ["None", "thoma_icon.png"],
    "tighnari": ["None", "tighnari_icon.png"],
    "traveler-anemo": ["None", "traveler-anemo_icon.png"],
    "traveler-dendro": ["None", "traveler-dendro_icon.png"],
    "traveler-electro": ["None", "traveler-electro_icon.png"],
    "traveler-geo": ["None", "traveler-geo_icon.png"],
    "venti": ["None", "venti_icon.png"],
    "xiangling": ["None", "xiangling_icon.png"],
    "xiao": ["None", "xiao_icon.png"],
    "xingqiu": ["None", "xingqiu_icon.png"],
    "xinyan": ["None", "xinyan_icon.png"],
    "yae-miko": ["Yae-Miko.mp4", "yae-miko_icon.png"],
    "yanfei": ["None", "yanfei_icon.png"],
    "yelan": ["None", "yelan_icon.png"],
    "yoimiya": ["None", "yoimiya_icon.png"],
    "yun-jin": ["None", "yun-jin_icon.png"],
    "zhongli": ["None", "zhongli_icon.png"],
}

def add_character_data(name, background, icon):
    existing_character = Character.objects.filter(name=name).first()

    if existing_character:
        # If the character exists, update the associated images
        existing_character.images.character_background = background
        existing_character.images.character_icon = icon
        existing_character.images.save()
    else:
        # If the character doesn't exist, create a new one
        character = Character.objects.create(name=name)
        CharacterImages.objects.create(
            character=character,
            character_background=background,
            character_icon=icon
        )

if __name__ == "__main__":
    for character in character_image_data:
        add_character_data(character,character_image_data[character][0],character_image_data[character][1])