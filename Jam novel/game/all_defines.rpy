init:
    #Define characters 
    define player_base = Character("Антон", color="#5efbba", image='', callback=name_callback, cb_name='anton')
    define narrator_base = Character(name=None, callback=name_callback, cb_name="narrator")
    define elis_base = Character("Элис", color="#5efbba", image='', callback=name_callback, cb_name='elis')
    # Image персонажей
    #image hoshi_normal = "images/characters/hoshi upset.png"
    #image hoshi_smile = "images/characters/hoshi smile.png"
    #image agustina_normal = "images/characters/agustina hmm.png"
    #image agustina_shock = "images/characters/agustina shock.png"

    # AutoHightLight
    image player = At('image_base', sprite_highlight('anton'))
    image narrator = At('image_base', sprite_highlight('narrator'))
    image elis = At('image_base', sprite_highlight('elis'))

    # Music
    define audio.myambient = "music/ambient.mp3"