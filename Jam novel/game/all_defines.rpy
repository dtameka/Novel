init:
    #Define characters 
    define player_base = Character("Кир", color="#5efbba", image='', callback=name_callback, cb_name='kir')
    define narrator_base = Character(name=None, kind=nvl)
    define alice_base = Character("Элис", color="#5efbba", image='vivian_base', callback=name_callback, cb_name='alice')
    # Image персонажей
    #image hoshi_normal = "images/characters/hoshi upset.png"
    #image hoshi_smile = "images/characters/hoshi smile.png"
    #image agustina_normal = "images/characters/agustina hmm.png"
    #image agustina_shock = "images/characters/agustina shock.png"

    # AutoHightLight
    image player = At('image_base', sprite_highlight('kir'))
    image alice = At('vivian_base', sprite_highlight('alice'))

    # Music
    define audio.myambient = "music/ambient_down.ogg"

    # Parcicles
    image dust_right = Fixed(SnowBlossom("images/particles/dust_white.png", 120, xspeed=10, yspeed=-10, start=50, horizontal=True, fast=True))
    image dust_left = Fixed(SnowBlossom("images/particles/dust_white.png", 120, xspeed=-10, yspeed=-10, start=50, horizontal=True, fast=True))

    # Ticket animation
    image jelly animated:
        "jelly1"
        pause 0.5
        "jelly2"
        pause 0.5
        "jelly3"
        pause 0.5
        repeat
    
    # Ticket animation with hand
    layeredimage hand:
        always:
            "hand ticket_light_on"
        attribute jelly:
            "jelly animated"

    image scalpel_blink animated:
        "scalpel blink"
        pause 0.5

        repeat

    layeredimage katalka_with_blink_scalpel:
        always:
            "bg katalka_with_scalpel"
        attribute blink:
            "scalpel_blink animated"
        
    # Transoforms
    transform offscreendown:
        ypos 0.8
        xpos 0

    transform offscreendown_end:
        ypos 0.9
        xpos 0

    transform default_hand_sposition:
        ypos -0.4 rotate 0.0