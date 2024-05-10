label brief: # Бриф
    with Fade(0.5, 0.5, 0.5)

    $ mouse_parallax.set((-10, -5, "l0"), (-20, -5, "l1"), (-40, -10, "l2"))
    $ showp("bg stars_l0", "bg stars_l1", "bg stars_l2") 
    with eyeopen
    #play music myambient fadein 1.0

    '''

    {fi=[0]-[2]-[0]}С выходом первого человека в космос был проделан \nогромный путь в попытке покорить звёзды.{/fi}

    {fi=[0]-[2]-[0]}Мы шли семимильными шагами, но космос оставался непостижим, \nвсё также холоден и далёк.{/fi}

    {fi=[0]-[2]-[0]}Каждый запуск нашего космического корабля это \nогромная подготовка.{/fi}

    {fi=[0]-[2]-[0]}При этом же{/fi} {bt=h1-p0.5-s0.5}прыжок в неизвестность{/bt}, {fi=[0]-[0.7]-[0]}ведь космос слишком огромен...{/fi}

    {fi=[0]-[2]-[0]}В каждой миссии мы изучали не космос, мы изучали себя \nв попытке осмыслить, навсегда ли наше одиночество \nво вселенной.{/fi}

    {fi=[0]-[2]-[0]}Увы...{/fi} 

    {fi=[0]-[2]-[0]}Наши корабли были слишком отсталыми, чтобы \nвылететь за пределы внешнего кольца планет.{/fi} 

    '''

    $ scenep()
    show bg antenna_l0
    $ showp("bg antenna_l1", "bg antenna_l2", "bg antenna_l3", "bg antenna_l4") 
    with ImageDissolve("transitions/wet.webp", 4.0, 80)
    
    '''
    {fi=[0]-[2]-[0]}И мы стали отправлять сигналы в надежде быть услышанными.{/fi} 

    {fi=[0]-[2]-[0]}В надежде, что кто-то поможет нам преодолеть звёздные \nрубежи в этом огромном пространстве пустоты.{/fi}

    {fi=[0]-[2]-[0]}И нас услышали…{/fi}
    '''
    $ scenep()
    $ showp("bg ship_jellyfish") 
    with ImageDissolve("transitions/wet.webp", 4.0, 80)
    
    '''
    {fi=[0]-[2]-[0]}Раньше все хотели в космос...{/fi}
    
    {fi=[0]-[2]-[0]}Но космос...{/fi}

    {fi=[0]-[2]-[0]}Пришёл к нам сам...{/fi}
    '''
    #stop music fadeout 2.0
    $ scenep()


label prologue_01: # Пробуждение
    with ImageDissolve("transitions/01.webp", 4.0, 50)
    show bg black
    pause(1.5)
    hide bg black
    with Fade(0.5, 0.5, 0.5)
    
    show bg morgue_black with eyeopen
    player_base '''
    {fi=[20]-[3]-[20]}Мг-мм-мм...{/fi}

    {fi=[20]-[3]-[20]}А-а-а…?{/fi}
    
    {fi=[20]-[3]-[20]}Где я? 
    {fi=[0]-[1]-[0]}Как же... болит голова!{/fi} 
    
    {fi=[0]-[1]-[0]}Ничего не помню. Как я сюда попал?{/fi}
    ''' with dissolve

    $ light_on = False
    $ check_ticket = False
    $ exit = False
    $ mouse_parallax.set((-20, -10, "l0"))
    while not exit:
        menu:
            "Проверить карманы" if not check_ticket:
                $ renpy.block_rollback()
                if light_on:                  
                    "Вы достаете какой-то билет"
                    $ scenep()
                    $ showp(("hand jelly", offscreendown))

                    window auto hide
                    show hand jelly onlayer l0:
                        subpixel True 
                        ypos 0.8 rotate -90.0
                        ease 2.05 ypos -0.4 rotate 0
                    with Pause(2.16)
                    show hand jelly onlayer l0:
                        ypos -0.4 rotate 0.0 
                    window auto show

                    with dissolve
                    player_base "{fi=[0]-[1]-[0]}Кажется я начинаю вспоминать...{/fi}"
                    player_base "Точно!" with vpunch
                    "Воспоминания ударили словно лавина! {fi=[0]-[2]-[0]}Кажется у вас опять начинает болеть голова...{/fi}"
                    player_base "{glitch=10}Ай-яй...{/glitch} еще не отошел." 

                    player_base "Так о чем это я. А точно!"

                    "Ваш взгляд наконец сфокусировался на билете"

                    "Вы вспоминаете как выиграли круиз на корабле этих инопланетян похожих на медуз, заполонивших города."
                    $ exit = True
                else:
                    "Вы нащупываете какой-то листок бумаги"
                    $ scenep()
                    $ showp("hand ticket_light_off")
                    with dissolve
                    player_base "{fi=[0]-[1]-[0]}Черт, ничего не видно!{/fi}"
                    "Надо найти выключатель, чтобы разобрать что здесь написано. Положу пока обратно."
                    $ scenep()
                    with dissolve
                    $ check_ticket = True
            "Нащупать выключатель" if not light_on:
                $ light_on = True
                $ check_ticket = False
                $ renpy.block_rollback()
                "Вы находите выключатель и белый свет ламп бьет вам в глаза"
                #hide bg morgue_black
                scene bg morgue_light with Fade(0.2, 1.0, 0.5, color="#ffffff")
                show dust_left
                show dust_right
                
                player_base "{glitch=20}Агъх.. черт!{/glitch}"
                '''
                Cпустя несколько минут {glitch=10}жжения{/glitch}, вы все же приходите в себя, а
                ваши глаза постепенно начинают привыкать к свету...

                Вы наблюдаете странные и подозрительные шкафы вокруг вас...
                '''
                player_base "{glitch=20}Черт возьми...{/glitch}"
                player_base "{fi=[0]-[1]-[0]}Как я сюда попал? Ничерта не помню{/fi} {glitch=20}угх-х-х... голова...{glitch=20}"
    hide dust_left
    hide dust_right
    $ scenep()
    with dissolve
    jump prologue_flashback

label prologue_flashback: # Воспоминания о том как прилетели пришельцы 
    window hide
    show bg city_without_jelly with ImageDissolve("transitions/005.webp", 7.0, 80)


    window show dissolve
    '''
    Наши ученые искали ответ, одни ли мы во вселенной.\nИ спустя много лет поисков, ответ был найден…
    ''' with dissolve

    window hide
    show bg city_jellyfish with Dissolve(2)
    pause(2)
    nvl show dissolve
    narrator_base '''
    Ученые послали в космос сигнал, и на сигнал откликнулись эти существа.

    Пришельцы заполонили всё вокруг, мы их стали называть котомедузками из-за их формы.

    Они делились с нами технологиями, едой, своей культурой и музыкой…

    Чтобы рассказать людям о себе ещё больше, котомедузки даже решили провести лотерею для счастливчиков.

    Главный приз - круиз на их космическом корабле.

    {clear}

    Пришельцы раздавали свои билеты на улицах,\nОтправляли билеты почтой, чтобы приобщить нас к свой “высокой культуре”.

    Удивительно, как быстро они смогли выучить абсолютно все языки народов Земли и войти со своей модой в каждый дом. 

    Так люди стали фанатеть от пришельцев.
    '''
    

label prologue_02:

    scene bg morgue_light with ImageDissolve("transitions/005.webp", 7.0, 80)

    show dust_left
    show dust_right
    $ showp(("hand jelly", default_hand_sposition))
    "{cps=30}Но всё же мне ещё непонятно как я оказался здесь…{/cps}" with dissolve


    $ check_pockets = False
    $ exit = False
    while not exit:
        menu:
            "Проверить карманы" if not check_pockets:
                $ renpy.block_rollback()
                "В карманах теперь пусто, положу пока билет обратно в жилетку"

                window auto hide
                show hand jelly onlayer l0:
                    subpixel True
                    ypos -0.4 rotate 0.0
                    ease 2.05 ypos 0.8 rotate -90.0
                with Pause(2.16)
                show hand jelly onlayer l0:
                    ypos 0.8 rotate 0.0

                $ scenep()
                with dissolve
                $ check_pockets = True
            "Осмотреться":
                $ exit = True
                $ check_ticket = False
                $ renpy.block_rollback()

                window auto hide
                show hand jelly onlayer l0:
                    subpixel True
                    ypos -0.4 rotate 0.0
                    ease 2.05 ypos 0.9 rotate -90.0
                with Pause(2.16)
                show hand jelly onlayer l0:
                    ypos 0.8 rotate 0.0

                '''
                Это определённо морг. Не знаю, был ли я здесь раньше - я не помню, голова {glitch=10}трещит…{/glitch}

                Что это там? Кажется на каталке что-то блестит...
                '''
                show katalka_with_blink_scalpel blink with dissolve
                # shound ШАГИ
                "Вы подходите к каталке и наблюдаете, что металический блеск исходил от скальпеля."                 

                $ scenep()
                $ mouse_parallax.set((-20, -10, "l0"))
                hide bg morgue_light
                hide dust_left
                hide dust_right

                show bg katalka_without_scalpel

                $ showp(("hand with_scalpel", offscreendown_end))

                window auto hide
                show hand with_scalpel onlayer l0:
                    subpixel True 
                    ypos 0.8 rotate -90.0
                    ease 1.3 ypos -0.75 rotate 0
                with Pause(1.5)
                show hand with_scalpel onlayer l0:
                    ypos -0.75 rotate 0.0 
                window auto show

                player_base "{fi=[0]-[1]-[0]}Возьму его, вдруг пригодиться. Пускай лежит в ближнем кармане{/fi}"

                window auto hide
                show hand with_scalpel onlayer l0:
                    subpixel True 
                    ypos -0.75 rotate 0.0
                    ease 1.3 ypos 0.9 rotate -90.0
                with Pause(1.5)
                show hand with_scalpel onlayer l0:
                    ypos 0.9 rotate  -90.0
                window auto show

    $ q = []
    while len(q) < 2:
        menu:
            "Осмотреться еще раз" if not 1 in q:
                $ renpy.block_rollback()
                $ q.append(1)
                "В комнате ничего не осталось"
            "Пойти дальше" if not 2 in q:
                $ renpy.block_rollback()
                $ q.append(2)
                "Вы подходите к единственной двери в помещении и решаетесь идти дальше."
            
    # Фон: светлый длинный, но заброшенный коридор, который должен нагонять не мрачняк, в надежду на возрождение 
    $ scenep()
    scene bg corridor_hight with dissolve
    "Перед вашим взором открывается коридор."
    player_base "{fi=[0]-[1]-[0]}Какой длинный коридор...{/fi}"
    
    window auto hide
    camera:
        subpixel True 
        parallel:
            ypos 0 
            ease 1.21 ypos 50 
            ease 1.15 ypos 0 
            ease 1.25 ypos 50 
            ease_back 1.29 ypos 0 
        parallel:
            zoom 1.0 
            linear 4.91 zoom 1.1 
    with Pause(5.01)
    camera:
        ypos 0 zoom 1.1 
    window auto show


    "Вы проходите пару метров, как видите, что перед вами появляется девушка."
    show alice
    "Ваша рука тянется к кормашку со скальпелем."
    #Появляется персонаж Элис, это участник «Сопротивления», тайной организации, которая ведет подпольную борьбу с пришельцами

    alice_base '''
    {fi=[0]-[0.5]-[0]}Привет, Кир, ну ты и соня. Ты что-нибудь помнишь после вчера?{/fi}

    {fi=[0]-[0.5]-[0]}Бойцам сопротивления удалось вырвать тебя\nиз лап этих тварей в самый последний момент.{/fi}

    {fi=[0]-[0.5]-[0]}Котомедузы почти полностью стерли твою личность.{/fi}
    '''

    player_base "{fi=[0]-[1]-[0]}Сопротивление...?{/fi}"

    alice_base '''
    {fi=[0]-[0.5]-[0]}Ооо... вижу ты совсем плох...{/fi}

    {fi=[0]-[0.5]-[0]}Ну ничего, дай мне пару минут.{/fi}
    '''

    "Элис взглядом указала на скальпель в кармашке, к которому вы тянитесь последние несколько секунд..."

    player_base "{fi=[0]-[1]-[0]}Ты что-то говорила про стирание личности?{/fi}"

    alice_base '''
    {fi=[0]-[0.5]-[0]}Да. Котомедузы умеют мурчать и издавать странные звуки.{/fi}
    
    {fi=[0]-[0.5]-[0]}Затем они начинают поглаживать человека своими\nотростками-щюпальцами по голове.{/fi}

    {fi=[0]-[0.5]-[0]}После всего этого, жертва пришельца теряет все...{/fi}
    
    {fi=[0]-[0.5]-[0]}Память... разум...  мысли...{/fi}

    {fi=[0]-[0.5]-[0]}Обычно, такой человек пропадает в их зданиях.\n

    {fi=[0]-[0.5]-[0]}Мы пока не знаем зачем инопланетяне это делают,\nтак как никто ещё не видел
    куда уводят людей,\nпосле стирания личности.{/fi}
    '''

    alice_base '''
    {fi=[0]-[0.5]-[0]}Пойдем со мной.{/fi}

    {fi=[0]-[0.5]-[0]}Я покажу тебе как всё устроено на нашей базе.{/fi}
    '''
    scene bg white with eyeopen




