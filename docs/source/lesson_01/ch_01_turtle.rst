.. role:: python(code)
   :language: python

Python Turtle
=============

.. dropdown:: Wat leer je in dit hoofdstuk
    :open:
    :color: primary
    :icon: book

    * Hoe importeer je de :python:`turtle` module in je programma.
    * Hoe maak je een turtle aan.
    * Hoe laat je de turtle bewegen.
    * Hoe verander je het uiterlijk van de turtle.
    * Hoe haal je de pen van het tekenpapier en hoe zet je hem weer neer.
    * Hoe wijzig je de dikte en de kleur van de pen.
    * Hoe vul je een getekende figuur op met een kleur.
    * Hoe laat je de turtle een cirkel tekenen.

    :bdg-warning:`Let op!` Dit hoofdstuk bevat vragen en opdrachten. Deze moet je 'uitklappen' om ze te kunnen lezen. Klik daartoe op de gekleurde titelbalk, net zoals je op de titelbalk van dit blok kunt klikken om het in te klappen.

Start in Mu editor met een nieuw bestand door op de knop :guilabel:`New` te klikken. Typ onderstaande code in het bestand en let daarbij goed op het verschil tussen hoofdletters en kleine letters! Sla het bestand op als :file:`hello_turtle.py` in de Documenten map.

.. code-block:: python
    :class: no-copybutton
    :linenos:
    :caption: hello_turtle.py
    :name: hello_turtle_v01

    import turtle

    tony = turtle.Turtle()

    tony.forward(100)

Run deze code om het resultaat te bekijken.

Sommige functies zoals :python:`print()` zitten standaard in Python, maar om met de schildpad te kunnen werken is het nodig de module :python:`turtle` te importeren. Dat gebeurt op regel 1. Op regel 3 maken we met de functie :python:`Turtle()` uit de :python:`turtle` module een schildpad aan met de naam :python:`tony`. Op regel 5 sturen we :python:`tony` 100 pixels naar voren.

.. image:: images/turtle_01.png
    :scale: 50%

Maar wat is dat nu? Onze Tony lijkt helemaal niet op een schildpad! Hij lijkt meer op een pijlpunt! Daar gaan we verandering in brengen. En we gaan hem ook van richting laten veranderen. Pas je code als volgt aan (de nieuwe regels zijn gemarkeerd):

.. code-block:: python
    :class: no-copybutton
    :linenos:
    :caption: hello_turtle.py
    :name: hello_turtle_v02
    :emphasize-lines: 4,7-12

    import turtle

    tony = turtle.Turtle()
    tony.shape('turtle')

    tony.forward(100)
    tony.left(90)
    tony.forward(50)
    tony.left(90)
    tony.forward(100)
    tony.left(90)
    tony.forward(50)

Op regel 4 zorgt :python:`tony.shape('turtle')` ervoor dat onze schildpad er ook uitziet als een schildpad. De regels 7, 9 en 11 laten :python:`tony` linksaf slaan alvorens verder te lopen.

.. dropdown:: Meer weten over turtle shapes?
    :color: info
    :icon: info

    Om de vorm van :python:`tony` in een schildpad te veranderen, gaven we de functie :python:`tony.shape()` de waarde :python:`'turtle'` mee. Er zijn echter nog andere vormen mogelijk. Dit is de volledige lijst:

    * :python:`'arrow'`
    * :python:`'turtle'`
    * :python:`'circle'`
    * :python:`'square'`
    * :python:`'triangle'`
    * :python:`'classic'`
 
De waarde die je tussen de haakjes aan de functie :python:`tony.forward()` meegeeft, is het aantal pixels dat de schildpad vooruit moet bewegen. Maar wat doet het getal :python:`90` tussen de haakjes van :python:`tony.left()`?

.. dropdown:: Vraag
    :open:
    :color: secondary
    :icon: question

    Wat betekent het getal :python:`90` tussen de haakjes van :python:`turtle.left()`?

    .. dropdown:: Antwoord
        :color: secondary
        :icon: check-circle

        Dat getal geeft aan hoeveel **graden** de turtle moet draaien. Een hoek van 90° is een rechte hoek. De aanroep :python:`turtle.left(90)` zorgt er dus voor dat de turtle 90° naar links draait, oftewel linksaf slaat.

        In onderstaande figuur zie je hoe een cirkel in graden is verdeeld. Hoeveel graden zitten er in een volledige cirkel denk je?

        .. image:: images/turtle_angles.png

De basisbewegingen
------------------
        
Tot nu toe hebben we in onze code voor de beweging van de schilpad de functies :python:`forward()` en :python:`left()` gebruikt. Kun je voorspellen welke bewegingsfuncties er nog meer zijn? Juist, :python:`backward()` en :python:`right()`. Omdat je deze vier functies heel vaak gebruikt, zijn er afkortingen voor, zodat je minder hoeft te typen.

.. list-table:: Afkortingen van de turtle functies
    :header-rows: 1

    * - Functie
      - Afkorting
    * - :python:`turtle.forward()`
      - :python:`turtle.fd()`
    * - :python:`turtle.backward()`
      - :python:`turtle.bk()`
    * - :python:`turtle.left()`
      - :python:`turtle.lt()`
    * - :python:`turtle.right()`
      - :python:`turtle.rt()`


.. dropdown:: Opdracht 01
    :color: secondary
    :icon: pencil

    Vervang de code in :file:`hello_turtle.py` door onderstaande code. Je hoeft de code niet over te typen, je kunt kopiëren en plakken.

    .. code-block:: python
        :linenos:
        :caption: hello_turtle.py
        :name: hello_turtle_oef01

        import turtle

        tony = turtle.Turtle()
        tony.shape('turtle')

        tony.lt(90)
        tony.fd(100)
        tony.bk(50)
        tony.rt(90)
        tony.fd(60)

    Run de code om te zien dat de schildpad het begin van een hoofdletter H tekent. Maak de code af zodat een volledige hoofdletter H wordt getekend. 

Pen up, pen down en pen size
----------------------------

Zoals je hebt gemerkt, is :python:`tony` een schildpad die van tekenen houdt, want hij heeft een pen vast waarmee hij zijn afgelegde weg tekent. Soms wil je echter dat :python:`tony` zijn pen even van het 'papier' haalt. Met de volgende twee functies kun je de pen van de schildpad bedienen:

.. list-table::
    :header-rows: 1

    * - Functie
      - Afkorting
    * - :python:`turtle.penup()`
      - :python:`turtle.pu()` of :python:`turtle.up()`
    * - :python:`turtle.pendown()`
      - :python:`turtle.pd()` of :python:`turtle.down()`

Daarnaast kun je de pendikte instellen met de volgende functie:

.. list-table::
    :header-rows: 1

    * - Functie
    * - :python:`turtle.pensize()`

Bij de functies :python:`turtle.penup()` en :python:`turtle.pendown()` zet je niks tussen de haakjes, maar de functie :python:`turtle.pensize()` heeft wél input nodig. Tussen de haakjes zet je een geheel getal dat de pendikte in pixels aangeeft. Dus bijvoorbeeld :python:`turtle.pensize(10)`

.. dropdown:: Opdracht 02
    :color: secondary
    :icon: pencil

    Breid je code in :file:`hello_turtle.py` uit zodat naast de letter H ook een hoofdletter E wordt getekend, met pendikte 5.

    .. image:: images/turtle_HE.png

    Kies zelf mooie lengtes voor de drie horizontale lijnen van de letter E, zodat je resultaat lijkt op het bovenstaande plaatje.

    .. dropdown:: Hint
        :color: secondary
        :icon: light-bulb

        Na de code die de letter H tekent, moet je dus eerst :python:`tony.penup()` aanroepen om de pen van het papier te halen. Vervolgens beweeg je de schildpad 20 pixels vooruit met :python:`tony.fd(20)` (misschien moet je hem eerst nog draaien, zodat hij de goede kant op gaat). Daarna roep je :python:`tony.pendown()` aan om de pen weer op het papier te zetten. Als je dat voor elkaar hebt, kun je de code maken die de letter E tekent. 


Kleuren
-------

Onze schildpad tekent vooralsnog zwarte lijnen; tijd voor wat fleurigheid! Uiteraard is er een functie om de penkleur van :python:`tony` te veranderen.

.. list-table::
    :header-rows: 1

    * - Functie
    * - :python:`turtle.pencolor()`

Tussen de haakjes geef je de gewenste kleur mee met de Engelse naam tussen aanhalingstekens, bijvoorbeeld :python:`turtle.pencolor('yellow')` of :python:`turtle.pencolor('green')`. Andere kleuren zijn :python:`gold`, :python:`orange`, :python:`red`, :python:`maroon`, :python:`violet`, :python:`magenta`, :python:`purple`, :python:`navy`, :python:`blue`, :python:`skyblue`, :python:`cyan`, :python:`turquoise`, :python:`lightgreen`, :python:`darkgreen`, :python:`chocolate`, :python:`brown`, :python:`black` en :python:`gray`. En er zijn er nog veel meer! Op `deze website <https://trinket.io/docs/colors>`_ kun je een kleurenpalet vinden.

.. dropdown:: Opdracht 03
    :color: secondary
    :icon: pencil

    Breid je code in :file:`hello_turtle.py` uit zodat de schildpad het woord HELLO tekent, waarbij elke letter een andere kleur en een andere pendikte heeft. Je mag zelf je favoriete kleuren en pendiktes kiezen. Hieronder staat een voorbeeldje.

    .. image:: images/turtle_HELLO.png

Draaiingshoeken
---------------

Draaien met een hoek van 90° is niet zo moeilijk. Draaiingshoeken met een andere grootte zijn lastiger dan je misschien denkt. Probeer de onderstaande opdracht maar eens.

.. dropdown:: Opdracht 04
    :color: secondary
    :icon: pencil

    Begin met een nieuw codebestand (via de :guilabel:`New` knop). Importeer de :python:`turtle` module en maak een turtle aan. In de vorige opdrachten heette de turtle :python:`tony`, maar je mag nu ook zelf een naam verzinnen. Sla het bestand op onder de naam :file:`turtle_house.py`.

    Maak een algoritme dat de onderstaande figuur tekent zónder de pen van het papier te halen, zónder de :python:`turtle.bk()` functie te gebruiken en zónder een draai van 180° te maken.

    .. image:: images/turtle_house.png
      :align: center

    .. dropdown:: Hint 1
        :color: secondary
        :icon: light-bulb

        Teken de figuur eerst eens zelf op papier zonder je pen op te tillen. Kun je erachter komen in welk punt je het beste kunt beginnen?

    .. dropdown:: Hint 2
        :color: secondary
        :icon: light-bulb

        Begin in de hoek linksonder en teken eerst het vierkant van 80 bij 80 pixels. Maak dan de diagonaal, het dak en tenslotte de diagonaal naar rechtsonder.

    .. dropdown:: Hint 3
        :color: secondary
        :icon: light-bulb

        De hoeken in de figuur zijn niet altijd de hoeken die je moet invullen bij :python:`turtle.lt()` of :python:`turtle.rt()`. Kijk maar eens naar de onderstaande afbeelding. De turtle komt van boven naar beneden aangelopen en moet vervolgens de diagonaal van linksonder naar rechtsboven maken. Om dat te doen moet hij niet 45° draaien, maar 90° + 45° = 135°. Ook bij het tekenen van het dak moet je goed nadenken over de te draaien hoeken.

        .. image:: images/turtle_house_hint.png

Figuurvulling
-------------
Het is mogelijk om een door de turtle getekende figuur op te vullen met een kleur. Daarvoor gebruik je de volgende functies:

.. list-table::
    :header-rows: 1

    * - Functie
      - Werking 
    * - :python:`turtle.fillcolor()`
      - Op dezelfde manier als :python:`turtle.pencolor()`
    * - :python:`turtle.begin_fill()`
      - Roep deze functie aan juist voordat de te vullen vorm wordt getekend.
    * - :python:`turtle.end_fill()`
      - Roep deze functie aan meteen nadat de te vullen vorm is getekend.

Je kunt dit uitproberen met het onderstaande codevoorbeeld. Maak hiervoor weer een nieuw bestand aan, met de naam :file:`turtle_fill.py`.

.. code-block:: python
    :linenos:
    :caption: turtle_fill.py
    :name: turtle_fill

    import turtle

    tony = turtle.Turtle()
    tony.shape('turtle')
    tony.pensize(5)

    # Stel de penkleur en de vulkleur in
    tony.pencolor('black')
    tony.fillcolor('yellow')

    # Teken een driehoek met vulling
    tony.begin_fill()
    tony.fd(100)
    tony.lt(120)
    tony.fd(100)
    tony.lt(120)
    tony.fd(100)
    tony.lt(120)
    tony.end_fill()

.. dropdown:: Opdracht 05
    :color: secondary
    :icon: pencil

    Breid de code in :file:`turtle_fill.py` uit, zodat links van het driehoekje een regelmatige vijfhoek met rode vulling wordt getekend, zoals in onderstaande figuur. De zijden van de vijfhoek zijn 60 pixels lang.

    .. image:: images/turtle_fill.png
      :align: center

    .. dropdown:: Hint
        :color: secondary
        :icon: light-bulb

        Om te berekenen hoeveel graden de turtle telkens moet draaien, kun je bedenken dat gedurende het tekenen van de vijfhoek de turtle in totaal precies één hele draai maakt van 360°. Deze draai wordt gelijk verdeeld over de vijf hoeken.

        .. list-table::
          :header-rows: 1

          * - Vorm
            - Aantal hoeken
            - Turtle draaihoek
            - Totale draaiing 
          * - Driehoek
            - 3
            - 120°
            - 3 * 120° = 360°
          * - Vierhoek
            - 4
            - 90°
            - 4 * 90° = 360°
          * - Vijfhoek
            - 5
            - ?°
            - 5 * ?° = 360°

Cirkels
-------

Veelhoeken zijn leuke figuren, en we zullen er later nog vaker op terugkomen, maar soms wil je gewoon een cirkel tekenen. Met Python turtle kan dat op twee manieren; met :python:`turtle.dot()` en met :python:`turtle.circle()`.

.. list-table::
    :header-rows: 1

    * - Functie
      - Werking 
    * - :python:`turtle.dot(size, color)`
      - Tekent een ronde stip met een diameter die je aangeeft met :python:`size` en een kleur die je aangeeft met :python:`color`. Bijvoorbeeld :python:`turtle.dot(40, "blue")`.  
    * - :python:`turtle.circle(radius)`
      - Tekent een cirkel met een straal (dat is de afstand tussen het middelpunt van de cirkel en de rand, dus eigenlijk de halve diameter) die je aangeeft met :python:`radius`. Bijvoorbeeld :python:`turtle.circle(20)`.  

Probeer beide functies uit met onderstaande code. Gebruik een nieuw bestand, met de naam :file:`turtle_circles.py`

.. code-block:: python
    :linenos:
    :caption: turtle_circles.py
    :name: turtle_circles

    import turtle

    tony = turtle.Turtle()

    tony.circle(40)
    tony.dot(80)

Zie je het verschil tussen de beide functies? :python:`turtle.dot()` levert een gevulde cirkel (een stip) en :python:`turtle.circle()` een niet-gevulde cirkel. Je kunt met :python:`turtle.begin_fill()` en :python:`turtle.end_fill()` de niet-gevulde cirkel natuurlijk alsnog vullen, zoals in onderstaand voorbeeld. Om het verschil tussen rand en vulling goed zichtbaar te maken worden in dit voorbeeld ook de pendikte en de kleuren ingesteld.

.. code-block:: python
    :linenos:
    :emphasize-lines: 4-6,8,10
    :caption: turtle_circles.py
    :name: turtle_circles_v02

    import turtle

    tony = turtle.Turtle()
    tony.pensize(5)
    tony.pencolor("black")
    tony.fillcolor("green")

    tony.begin_fill()
    tony.circle(40)
    tony.end_fill()
    tony.dot(80)

.. dropdown:: Meer weten over extra mogelijkheden met turtle.circle()? 
    :color: info
    :icon: info

    Behalve de straal van de cirkel, kun je aan :python:`turtle.circle()` nóg een getal meegeven. Probeer de volgende code maar eens:

    .. code-block:: python
        :linenos:
        :caption: turtle_circles.py
        :name: turtle_circles_v03

        import turtle

        tony = turtle.Turtle()

        tony.circle(40, 90)
    
    Run het programma en wijzig daarna regel 5 in :python:`tony.circle(40, 180)`. Run weer en wijzig daarna regel 5 in :python:`tony.circle(40, 270)`. Zie je wat dat tweede getal doet?

    Je kunt zelfs nog een derde getal toevoegen binnen de haakjes. Probeer het volgende:

    .. code-block:: python
        :linenos:
        :caption: turtle_circles.py
        :name: turtle_circles_v04

        import turtle

        tony = turtle.Turtle()

        tony.circle(40, 360, 4)
    
    Run het programma en wijzig daarna regel 5 in :python:`tony.circle(40, 360, 5)`. Run weer en wijzig daarna regel 5 in :python:`tony.circle(40, 360, 6)`. Zie je wat het derde getal doet?

.. dropdown:: Opdracht 06
    :color: secondary
    :icon: pencil

    Vervang de code in :file:`turtle_circles.py` door een programma dat een stoplicht tekent zoals hieronder getoond. De afmetingen mag je zelf kiezen en hoeven niet exact overeen te komen met het voorbeeld.

    .. image:: images/turtle_trafficlight.png
      :align: center