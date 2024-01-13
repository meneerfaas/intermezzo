.. role:: python(code)
   :language: python

.. |br| raw:: html

   <br/>

Python Turtle - Extra oefeningen
================================

Opdrachten
----------

.. dropdown:: Opdracht 07 - Windows logo
    :open:
    :color: secondary
    :icon: pencil

    Schrijf een programma dat een eenvoudige versie van het Windows logo tekent:

    .. figure:: images/turtle_windows_logo.png
      :align: center

    Het logo bestaat uit vier vierkantjes met zijden van 100 pixels. De ruimte tussen de vierkantjes is 20 pixels. De in het voorbeeld gebruikte kleuren heten:
    
    * :python:`'tomato'`
    * :python:`'yellow green'`
    * :python:`'deep sky blue'`
    * :python:`'gold'`

    .. dropdown:: Hint 1
        :color: secondary
        :icon: light-bulb

        De vierkantjes hebben geen zichtbare rand. Dat kun je voor elkaar krijgen door de penkleur en de vulkleur voor elk vierkant dezelfde waarde te geven:

        .. code-block:: python

            tony.pencolor('tomato')
            tony.fillcolor('tomato')

        Het is ook mogelijk dit met één regel code te bewerkstelligen:

        .. code-block:: python

            tony.color('tomato', 'tomato')

        Met de functie :python:`turtle.color()` kun je in één keer de penkleur én de vulkleur instellen.

    .. dropdown:: Hint 2
        :color: secondary
        :icon: light-bulb

        Het is handig om je code netjes te structureren in een aantal blokken:

        * Tekenen van het rode vierkant.
        * De turtle verplaatsen.
        * Tekenen van het groene vierkant.
        * De turtle verplaatsen.
        * Tekenen van het gele vierkant.
        * De turtle verplaatsen.
        * Tekenen van het blauwe vierkant.

        Door dat te doen, kun je veel code copy-pasten. Het tekenen van een vierkant is namelijk elke keer hetzelfde.

.. dropdown:: Opdracht 08 - Zandloper
    :open:
    :color: secondary
    :icon: pencil

    Schrijf een programma dat een zandloper tekent:

    .. figure:: images/turtle_hourglass.png
      :align: center

    De zandloper bestaat uit twee gelijkzijdige driehoeken met zijden van 200 pixels. Voor het zand is in het voorbeeld de kleur :python:`'sandy brown'` gebruikt en voor het glas de kleur :python:`'alice blue'`. De pendikte in het voorbeeld is 5 pixels.

    .. dropdown:: Hint
        :color: secondary
        :icon: light-bulb

        Bij deze opdracht zou je verschillende driehoeken over elkaar kunnen tekenen. Voor de bovenste helft bijvoorbeeld eerst een driehoek met een lichtblauwe vulling en daaroverheen een driehoek met een zandkleurige vulling.
       
.. dropdown:: Opdracht 09 - Olympische ringen
    :open:
    :color: secondary
    :icon: pencil

    Schrijf een programma dat de Olympische ringen tekent:

    .. figure:: images/turtle_olympic_rings.png
      :align: center

    In het voorbeeld hebben de ringen een straal van 80 pixels (dus een diameter van 160 pixels) en is de pendikte 15 pixels. De gebruikte kleuren zijn:

    * :python:`'royal blue'`
    * :python:`'black'`
    * :python:`'crimson'`
    * :python:`'sea green'`
    * :python:`'orange'` 

    .. dropdown:: Opmerking
        :color: secondary
        :icon: note

        De echte Olympische ringen zien er iets anders uit. Kijk maar eens hoe de ringen voor en achter elkaar zijn geplaatst:

        .. figure:: images/turtle_olympic_rings_2.png
          :align: center
          :scale: 75%

        Je zou dit met de turtle wel voor elkaar kunnen krijgen, maar dat is niet eenvoudig!

.. dropdown:: Opdracht 10 - Sheriff ster
    :open:
    :color: secondary
    :icon: pencil

    Schrijf een programma dat de ster van een Sheriff tekent:

    .. figure:: images/turtle_sheriff_star.png
      :align: center

    In het voorbeeld is de pendikte 5 pixels, de penkleur :python:`'orange'` en de vulkleur :python:`'gold'`. De lijnstukjes zijn 80 pixels lang en de rondjes hebben een diameter van 32 pixels.

    .. dropdown:: Hint 1
        :color: secondary
        :icon: light-bulb

        Bedenk op welke manier je de rondjes gaat tekenen. Gebruik je daar de :python:`turtle.circle()` functie voor of liever :python:`turtle.dot()`? 

    .. dropdown:: Hint 2
        :color: secondary
        :icon: light-bulb

        De punten van de ster kun je beschouwen als gelijkzijdige driehoeken rondom een regelmatige zeshoek. Kun je daaruit afleiden wat de draaiingshoeken zijn? Je moet de turtle afwisselend linksom en rechtsom laten draaien.

Oplossingen
-----------

.. dropdown:: Oplossing opdracht 07
    :color: secondary
    :icon: check-circle

    .. code-block:: python
        :linenos:
        :caption: turtle_windows_logo.py

        import turtle

        tony = turtle.Turtle()

        # Teken rood vierkant
        tony.color('tomato', 'tomato')
        tony.begin_fill()
        tony.fd(100)
        tony.lt(90)
        tony.fd(100)
        tony.lt(90)
        tony.fd(100)
        tony.lt(90)
        tony.fd(100)
        tony.lt(90)
        tony.end_fill()

        # Verplaats 120 pixels naar rechts
        tony.pu()
        tony.fd(120)
        tony.pd()

        # Teken groen vierkant
        tony.color('yellow green', 'yellow green')
        tony.begin_fill()
        tony.fd(100)
        tony.lt(90)
        tony.fd(100)
        tony.lt(90)
        tony.fd(100)
        tony.lt(90)
        tony.fd(100)
        tony.lt(90)
        tony.end_fill()

        # Verplaats 120 pixels naar beneden
        tony.pu()
        tony.rt(90)
        tony.fd(120)
        tony.lt(90)
        tony.pd()

        # Teken geel vierkant
        tony.color('gold', 'gold')
        tony.begin_fill()
        tony.fd(100)
        tony.lt(90)
        tony.fd(100)
        tony.lt(90)
        tony.fd(100)
        tony.lt(90)
        tony.fd(100)
        tony.lt(90)
        tony.end_fill()

        # Verplaats 120 pixels naar links
        tony.pu()
        tony.bk(120)
        tony.pd()

        # Teken blauw vierkant
        tony.color('deep sky blue', 'deep sky blue')
        tony.begin_fill()
        tony.fd(100)
        tony.lt(90)
        tony.fd(100)
        tony.lt(90)
        tony.fd(100)
        tony.lt(90)
        tony.fd(100)
        tony.lt(90)
        tony.end_fill()

.. dropdown:: Oplossing opdracht 08
    :color: secondary
    :icon: check-circle

    .. code-block:: python
        :linenos:
        :caption: turtle_zandloper.py

        import turtle

        tony = turtle.Turtle()
        tony.pensize(5)

        # Teken bovenste driehoek
        tony.fillcolor('alice blue')
        tony.begin_fill()
        tony.fd(200)
        tony.rt(120)
        tony.fd(200)
        tony.rt(120)
        tony.fd(200)
        tony.end_fill()

        # Teken zandvulling in bovenste driehoek
        tony.fillcolor('sandy brown')
        tony.bk(200)
        tony.begin_fill()
        tony.fd(140)
        tony.rt(120)
        tony.fd(140)
        tony.rt(120)
        tony.fd(140)
        tony.end_fill()

        # Teken onderste driehoek
        tony.fillcolor('alice blue')
        tony.begin_fill()
        tony.fd(200)
        tony.lt(120)
        tony.fd(200)
        tony.lt(120)
        tony.fd(200)
        tony.end_fill()

        # Teken zandvulling in onderste driehoek
        tony.fillcolor('sandy brown')
        tony.bk(200)
        tony.begin_fill()
        tony.fd(60)
        tony.lt(60)
        tony.fd(140)
        tony.lt(60)
        tony.fd(60)
        tony.lt(120)
        tony.fd(200)
        tony.end_fill()
        
.. dropdown:: Oplossing opdracht 09
    :color: secondary
    :icon: check-circle

    .. code-block:: python
        :linenos:
        :caption: turtle_olympische_ringen.py

        import turtle

        tony = turtle.Turtle()
        tony.pensize(15)

        # Teken blauwe ring
        tony.pencolor('royal blue')
        tony.circle(80)

        # Verplaats 200 pixels naar rechts
        tony.pu()
        tony.fd(200)
        tony.pd()

        # Teken zwarte ring
        tony.pencolor('black')
        tony.circle(80)

        # Verplaats 200 pixels naar rechts
        tony.pu()
        tony.fd(200)
        tony.pd()

        # Teken rode ring
        tony.pencolor('crimson')
        tony.circle(80)

        # Verplaats 80 pixels naar beneden en 100 pixels naar links
        tony.pu()
        tony.rt(90)
        tony.fd(80)
        tony.lt(90)
        tony.bk(100)
        tony.pd()

        # Teken groene ring
        tony.pencolor('sea green')
        tony.circle(80)

        # Verplaats 200 pixels naar links
        tony.pu()
        tony.bk(200)
        tony.pd()

        # Teken gele ring
        tony.pencolor('orange')
        tony.circle(80)

.. dropdown:: Oplossing opdracht 10
    :color: secondary
    :icon: check-circle

    .. code-block:: python
        :linenos:
        :caption: turtle_sheriff_ster.py

        import turtle

        tony = turtle.Turtle()
        tony.pensize(5)

        tony.color('orange', 'gold')
        tony.begin_fill()

        tony.fd(80)
        tony.dot(32)
        tony.lt(120)
        tony.fd(80)
        tony.rt(60)

        tony.fd(80)
        tony.dot(32)
        tony.lt(120)
        tony.fd(80)
        tony.rt(60)

        tony.fd(80)
        tony.dot(32)
        tony.lt(120)
        tony.fd(80)
        tony.rt(60)

        tony.fd(80)
        tony.dot(32)
        tony.lt(120)
        tony.fd(80)
        tony.rt(60)

        tony.fd(80)
        tony.dot(32)
        tony.lt(120)
        tony.fd(80)
        tony.rt(60)

        tony.fd(80)
        tony.dot(32)
        tony.lt(120)
        tony.fd(80)
        tony.rt(60)

        tony.end_fill()

    .. dropdown:: Extra - Tekst tonen
        :color: secondary
        :icon: plus-circle

        Als je de tekst 'Sheriff' op de ster wilt tonen, kun je de volgende code toevoegen:

        .. code-block:: python
            :linenos:
            :lineno-start: 47
            :caption: turtle_sheriff_ster.py

            # Tekst
            tony.pu()
            tony.bk(40)
            tony.lt(90)
            tony.fd(40)
            tony.rt(90)
            tony.pencolor('dark goldenrod')
            tony.write('SHERIFF', False, align = 'center', font = ('Arial Narrow', 32, 'bold'))            

    .. dropdown:: Extra - Cirkels in plaats van stippen
        :color: secondary
        :icon: plus-circle

        Wanneer je in plaats van :python:`turtle.dot()` de functie :python:`turtle.circle()` gebruikt, kun je de volgende ster tekenen:

        .. image:: images/turtle_sheriff_star_2.png
          :align: center

        In dit voorbeeld is er met de aanroep :python:`tony.circle(16, 320)` voor gezorgd, dat de turtle 320° van een hele cirkel (360°) met straal 16 tekent. Echter direct vóór en ná deze aanroep moet de turtle 100° rechtsom draaien.

        .. dropdown:: Oplossing
            :color: secondary
            :icon: check-circle

            .. code-block:: python
                :linenos:
                :caption: turtle_sheriff_ster_v2.py

                import turtle

                tony = turtle.Turtle()
                tony.pensize(5)

                tony.color('orange', 'gold')
                tony.begin_fill()

                tony.fd(80)
                tony.rt(100)
                tony.circle(16,320)
                tony.rt(100)
                tony.fd(80)
                tony.rt(60)

                tony.fd(80)
                tony.rt(100)
                tony.circle(16,320)
                tony.rt(100)
                tony.fd(80)
                tony.rt(60)

                tony.fd(80)
                tony.rt(100)
                tony.circle(16,320)
                tony.rt(100)
                tony.fd(80)
                tony.rt(60)

                tony.fd(80)
                tony.rt(100)
                tony.circle(16,320)
                tony.rt(100)
                tony.fd(80)
                tony.rt(60)

                tony.fd(80)
                tony.rt(100)
                tony.circle(16,320)
                tony.rt(100)
                tony.fd(80)
                tony.rt(60)

                tony.fd(80)
                tony.rt(100)
                tony.circle(16,320)
                tony.rt(100)
                tony.fd(80)
                tony.rt(60)

                tony.end_fill()