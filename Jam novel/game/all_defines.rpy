init:
    #Define characters 
    define player_base = Character("Антон", color="#5efbba", image='', callback=name_callback, cb_name='anton')
    define narrator_base = Character(name=None, kind=nvl)
    define elis_base = Character("Элис", color="#5efbba", image='', callback=name_callback, cb_name='elis')
    # Image персонажей
    #image hoshi_normal = "images/characters/hoshi upset.png"
    #image hoshi_smile = "images/characters/hoshi smile.png"
    #image agustina_normal = "images/characters/agustina hmm.png"
    #image agustina_shock = "images/characters/agustina shock.png"

    # AutoHightLight
    image player = At('image_base', sprite_highlight('anton'))
    image elis = At('image_base', sprite_highlight('elis'))

    # Music
    define audio.myambient = "music/ambient.mp3"

    # Parcicles
    #image dust1 = Fixed(SnowBlossom("images/dust1_p.png", 5, xspeed=20, yspeed=-10, start=50, horizontal=True, fast=True))
    #image dust2 = Fixed(SnowBlossom("images/dust1_p.png", 5, xspeed=-50, yspeed=-10, start=50, horizontal=False, fast=True))
    image dust_right = Fixed(SnowBlossom("images/particles/dust_white.png", 120, xspeed=10, yspeed=-10, start=50, horizontal=True, fast=True))
    image dust_left = Fixed(SnowBlossom("images/particles/dust_white.png", 120, xspeed=-10, yspeed=-10, start=50, horizontal=True, fast=True))

    image jelly animated:
        "jelly1"
        pause 0.5
        "jelly2"
        pause 0.5
        "jelly3"
        pause 0.5
        repeat

    layeredimage hand:
        always:
            "hand ticket_light_on"
        attribute jelly:
            "jelly animated"