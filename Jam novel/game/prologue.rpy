label brief: # Бриф
    $ mouse_parallax.set((-10, -5, "l0"), (-20, -5, "l1"), (-40, -10, "l2"))
    $ showp("bg stars_l0", "bg stars_l1", "bg stars_l2") 
    with eyeopen
    hide prologue_text

    '''

    {fi=[0]-[2]-[0]}С первого полета человека в космос \nбыл проделан огромный путь в попытке покорить звёзды.{/fi}

    {fi=[0]-[2]-[0]}Прогресс двигался семимильными шагами, \nно космос всё также оставался непостижим.{/fi}

    {fi=[0]-[2]-[0]}Пусть каждый запуск космического корабля и требует \nогромных усилий, множества вычислений и расчетов.{/fi}

    {fi=[0]-[1]-[0]}Но это все также {/fi} {bt=h1-p0.5-s0.5}прыжок в неизвестность{/bt}. 

    {fi=[0]-[2]-[0]}Ведь космоса не видно ни конца ни края...{/fi}

    {fi=[0]-[2]-[0]}И в каждой миссии мы на самом деле изучали не \nбескрайние просторы Вселенной, а самих себя...{/fi}

    {fi=[0]-[2]-[0]}В попытке найти ответ на вечный вопрос: \nдействительно ли мы одни в этом бескрайнем океане звезд.{/fi}

    {fi=[0]-[2]-[0]}Увы...{/fi} 

    {fi=[0]-[2]-[0]}Наших технологий не хватало даже на то, \nчтобы вылететь за пределы Солнечной системы.{/fi} 

    '''

    $ scenep()
    $ mouse_parallax.set((-2, -5, "l0"), (-4, -5, "l1"), (-8, -5, "l2"), (-12, -5, "l3"), (-17, -5, "l4"))
    $ showp("bg antenna_l0", "bg antenna_l1", "bg antenna_l2", "bg antenna_l3", "bg antenna_l4") 
    with ImageDissolve("transitions/wet.webp", 4.0, 80)
    play sound "music/radio_bip_bup.ogg" fadein 2.0
    
    '''
    {fi=[0]-[2]-[0]}Тогда мы начали отправлять сигналы в космос, \nв надежде, что кто-то нас услышит и отзовется.{/fi} 

    {fi=[0]-[2]-[0]}В надежде, что кто-то поможет нам преодолеть звёздные \nрубежи в этом огромном пространстве пустоты.{/fi}

    {fi=[0]-[2]-[0]}И нас услышали...{/fi}
    '''

    $ scenep()
    $ mouse_parallax.set((0, 0, "l0"), (-20, -10, "l1"), (0, 0, "l2"))
    $ showp("bg ship_l0", "bg stars_l2", "bg ship_l1") 
    with ImageDissolve("transitions/wet.webp", 4.0, 80)
    
    '''
    {fi=[0]-[2]-[0]}Раньше все хотели в космос...{/fi}
    
    {fi=[0]-[2]-[0]}Но космос...{/fi}

    {fi=[0]-[2]-[0]}Пришёл к нам сам...{/fi}
    '''
    stop music fadeout 2.0
    $ scenep()


label prologue_01: # Пробуждение
    with ImageDissolve("transitions/01.webp", 4.0, 70)
    show bg black
    pause(1.5)
    hide bg black
    with Fade(0.5, 0.5, 0.5)
    
    show bg morgue_black with eyeopen
    play music "music/ambient_morgue.ogg"
    player_base '''
    {fi=[20]-[3]-[20]}Мг-мм-мм...{/fi}

    {fi=[20]-[3]-[20]}А-а-а...?{/fi}
    
    {fi=[20]-[3]-[20]}Где я? 
    {fi=[0]-[1]-[0]}Как же... болит голова...{/fi} 
    ''' with dissolve

    # {fi=[0]-[1]-[0]}Ничерта не помню. Как я сюда попал?{/fi}

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
                    play sound "music/sound_paper.ogg" fadeout 1.0
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
                    "Воспоминания нахлынули словно цунами. {fi=[0]-[2]-[0]}Кажется у вас опять начинает болеть голова...{/fi}"
                    player_base "{glitch=10}Ай-яй...{/glitch} еще не отошел." 

                    player_base "О чем это я... а, ну конечно"

                    "Ваш взгляд наконец сфокусировался на билете"

                    "Вы вспоминаете как выиграли круиз на корабле этих, заполонивших города, инопланетян, похожих на медуз."
                    $ exit = True
                else:
                    "Вы нащупываете какой-то листок бумаги"
                    $ scenep()
                    play sound "music/sound_paper.ogg" fadeout 1.0
                    $ showp("hand ticket_light_off")
                    with dissolve
                    player_base "{fi=[0]-[1]-[0]}Черт, ничего не видно, хоть глаз выколи.{/fi}"
                    player_base "Для начала найду способ включить свет, чтобы хоть что-то разобрать. \nЛисток подождет."
                    $ scenep()
                    with dissolve
                    $ check_ticket = True
            "Найти выключатель" if not light_on:
                $ light_on = True
                $ check_ticket = False
                $ renpy.block_rollback()
                "В этой темноте, вам наконец удается найти выключатель."
                play sound "music/sound_click_lamp.ogg"
                play ambient "music/lamp_gool.ogg"
                play music "music/ambient_morgue_2.ogg"
                scene bg morgue_light with Fade(0.2, 1.0, 0.5, color="#ffffff")
                show dust_left
                show dust_right   
                player_base "{glitch=20}Агъх.. черт!{/glitch}"
                '''
                Cпустя несколько мгновений {glitch=10}жжения{/glitch}, вы все же приходите в себя, 
                а ваши глаза постепенно начинают привыкать к свету...

                Вы наблюдаете какие-то странные шкафы вокруг вас...
                '''
                player_base "{glitch=20}Что за...{/glitch}"
                player_base "{fi=[0]-[1]-[0]}Как я сюда попал? Ничерта не помню{/fi} {glitch=20}ух-х-х... голова...{glitch=20}"
    hide dust_left
    hide dust_right
    $ scenep()
    with dissolve
    stop ambient fadeout 5.0
    jump prologue_flashback

label prologue_flashback: # Воспоминания о том как прилетели пришельцы 
    window hide
    play music "music/city_noise.ogg"
    show bg city_without_jelly with ImageDissolve("transitions/005.webp", 7.0, 80)


    window show dissolve
    '''
    Люди тысячелетиями искали ответ на вопрос: одни ли мы во вселенной.\nНесколько лет назад ответ был найден...
    ''' with dissolve

    window hide
    show bg city_jellyfish with Dissolve(2)
    pause(2)
    nvl show dissolve
    narrator_base '''
    Ученые отправили в космос сигнал.

    И на сигнал откликнулись эти существа.

    Пришельцы заполонили всё вокруг. Из-за их характерного внешнего вида мы стали называть котомедузками.

    Они поделились с нами своими технологиями, своей культурой...
    
    Удивительно, как быстро они смогли выучить абсолютно все языки народов Земли и войти со своей модой в каждый дом. 

    Чтобы рассказать людям о себе ещё больше, котомедузки решили воспользоваться человеческим азартом – провести лотерею.

    Главный приз – круиз на их космическом корабле.

    {clear}

    Пришельцы раздавали билеты на улицах, отправляли их почтой. 
    
    Делали все, чтобы приобщить нас к свой «высокой культуре».

    Так люди стали фанатеть от пришельцев.
    '''
    stop music fadeout 3.0
    

label prologue_02:

    play ambient "music/lamp_gool.ogg" fadein 4.0
    scene bg morgue_light with ImageDissolve("transitions/005.webp", 5.0, 80)

    show dust_left
    show dust_right
    $ showp(("hand jelly", default_hand_sposition))
    with Dissolve(1.5)
    "{cps=30}И всё же, как я здесь оказался...{/cps}" with dissolve


    $ check_pockets = False
    $ exit = False
    while not exit:
        menu:
            "Проверить карманы" if not check_pockets:
                $ renpy.block_rollback()
                "В карманах теперь пусто. Уберу пока билет обратно"
                play sound "music/sound_paper_end.ogg" fadeout 1.0
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
                $ renpy.block_rollback()
                if not check_pockets:
                    play sound "music/sound_paper_end.ogg" fadeout 1.0
                    window auto hide
                    show hand jelly onlayer l0 :
                        subpixel True
                        ypos -0.4 rotate 0.0
                        ease 2.05 ypos 0.9 rotate -90.0
                    with Pause(2.16)
                    show hand jelly onlayer l0:
                        ypos 0.8 rotate 0.0

                '''
                Ладно, это определённо морг. Не знаю... не помню, был ли я здесь раньше. Голова {glitch=10}трещит...{/glitch}

                Что это там? Кажется на каталке что-то блестит...
                '''
                show katalka_with_blink_scalpel blink with dissolve
                # shound ШАГИ
                "Вы подходите ближе и понимаете, что металический блеск исходил от скальпеля."                 

                $ scenep()
                $ mouse_parallax.set((-20, -10, "l0"))
                hide bg morgue_light
                hide dust_left
                hide dust_right

                show bg katalka_without_scalpel
                
                $ showp(("hand with_scalpel", offscreendown_end))
                play sound "music/take_knife_new.ogg"

                window auto hide
                show hand with_scalpel onlayer l0:
                    subpixel True 
                    ypos 0.8 rotate -90.0
                    ease 1.3 ypos -0.75 rotate 0
                with Pause(1.5)
                show hand with_scalpel onlayer l0:
                    ypos -0.75 rotate 0.0 
                window auto show

                player_base "{fi=[0]-[1]-[0]}Возьму его, может пригодится.{/fi}"

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
                "В комнате ничего не осталось."
            "Пойти дальше" if not 2 in q:
                $ renpy.block_rollback()
                $ q.append(2)
                "Вы подходите к единственной двери в помещении и решаетесь идти дальше."
            
    # Фон: светлый длинный, но заброшенный коридор, который должен нагонять не мрачняк, в надежду на возрождение 
    $ scenep()
    stop ambient fadeout 2.0
    scene bg corridor_hight with dissolve
    play music "music/pre_end.ogg"
    "Вашему взору предстает коридор."
    player_base "{fi=[0]-[1]-[0]}Какой длинный коридор...{/fi}"
    
    window auto hide
    play ambient "music/staps.ogg"
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
    stop ambient
    window auto show

    show alice with dissolve
    "С трудом сделав несколько шагов, вы замечаете перед собой девушку"
    
    "Ваша рука медленно тянется к карману со скальпелем."
    #Появляется персонаж Элис, это участник «Сопротивления», тайной организации, которая ведет подпольную борьбу с пришельцами

    alice_base '''
    {fi=[0]-[0.5]-[0]}Привет, Кир, ну ты и соня. Ты что-нибудь помнишь после вчера?{/fi}

    {fi=[0]-[0.5]-[0]}Бойцам сопротивления удалось вырвать тебя\nиз лап этих тварей в самый последний момент.{/fi}

    {fi=[0]-[0.5]-[0]}Котомедузы почти полностью стерли твою личность.{/fi}
    '''

    player_base "{fi=[0]-[1]-[0]}Сопротивление...?{/fi}"

    alice_base '''
    {fi=[0]-[0.5]-[0]}О-о-о... вижу ты совсем плох...{/fi}

    {fi=[0]-[0.5]-[0]}Ну ничего, дай мне пару минут.{/fi}
    '''

    "Элис взглядом указала на скальпель в вашем кармане, к которому вы тянитесь последние несколько секунд..."

    player_base "{fi=[0]-[1]-[0]}Ты что-то говорила про стирание личности?{/fi}"

    alice_base '''
    {fi=[0]-[0.5]-[0]}Да. Котомедузы мурчат, издают странные звуки.{/fi}
    
    {fi=[0]-[0.5]-[0]}Затем начинают поглаживать человека своими\nотростками-щупальцами по голове.{/fi}

    {fi=[0]-[0.5]-[0]}После этого жертва теряет все...{/fi}
    
    {fi=[0]-[0.5]-[0]}Память... эмоции...  мысли...{/fi}

    {fi=[0]-[0.5]-[0]}Чаще всего этих бедолаг в последний раз видят, \nидущими в строну зданий пришельцев.{/fi}

    {fi=[0]-[0.5]-[0]}Мы до сих пор не знаем зачем котомедузы это делают...{/fi}
    '''

    alice_base '''
    {fi=[0]-[0.5]-[0]}Пойдем со мной.{/fi}

    {fi=[0]-[0.5]-[0]}Я покажу тебе как всё устроено на нашей базе.{/fi}
    '''
    play music "music/end_prologue_ambient.ogg"
    # Конец
    scene bg white with eyeopen
    pause 2.0
    show black with Dissolve(3)
    show prologue_text_end:
        xalign 0.45
        yalign 0.45
    with Dissolve(8)




