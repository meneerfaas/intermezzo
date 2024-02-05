.. role:: python(code)
   :language: python

Code herhalen met loops
=======================

Heb je het werken met variabelen door? Mooi, dan kunnen we nu weer verdergaan met het leukere programmeerwerk!

While loops
-----------

Maak in Mu editor weer een nieuw bestand door op de knop :guilabel:`New` te klikken. Kopieer en plak de onderstaande code in het bestand en sla het op als :file:`turtle_while.py`.

.. code-block:: python
    :linenos:
    :caption: turtle_while.py
    :name: turtle_while_v01

    import turtle

    tony = turtle.Turtle()

    zijde = 0
    while zijde < 4:
        tony.fd(100)
        tony.lt(90)
        zijde = zijde + 1

Run de code om het resultaat te bekijken. Snap je hoe deze code werkt? Het Python keyword :python:`while` in regel 6, kun je vertalen als *terwijl* of *zolang*. En het :python:`<`  symbool betekent *kleiner dan*. Dus regel 6 kun je lezen als:

    Zolang de waarde van :python:`zijde` kleiner is dan :python:`4`, doe het volgende:

De regels 7, 8 en 9 zijn **ingesprongen**. Dat is belangrijk! Daardoor weet Python dat die drie regels binnen de 'while lus' vallen. Zolang aan de voorwaarde :python:`zijde < 4` is voldaan, voert Python deze regels uit. Regel 9 zorgt ervoor dat de waarde van :python:`zijde` met 1 wordt verhoogd. Na het uitvoeren van deze regel, springt Python terug naar regel 6 om de voorwaarde :python:`zijde < 4` opnieuw te checken.

Klinkt moeilijk? Misschien helpt het dan om de while loop echt in actie te zien. Maak Opdracht 01 hieronder om te leren over de 'debugging mode' van Mu-editor en te zien hoe de while loop wordt uitgevoerd.

.. _opdracht-01:

.. dropdown:: Opdracht 01
    :color: secondary
    :icon: pencil

    Klik op regel 6 in :file:`turtle_while.py` met de muiscursor in het grijze stukje rechts naast het regelnummer 6 om een zogenoemd **breakpoint** te plaatsen.

    .. figure:: images/debug_breakpoint.png
        :align: left
        :figwidth: 100%

    Klik daarna op :guilabel:`Debug` bovenin de knoppenbalk.

    .. figure:: images/debug_debug_button.png
        :align: left
        :figwidth: 100%

    Nu start Mu editor de uitvoering van de code, maar pauzeert op regel 6, waar je zojuist het breakpoint plaatste. Gebruik de knop :guilabel:`Step over` om de code vanaf het breakpoint telkens een stapje verder uit te voeren. Houd daarbij in de gaten wat er in de turtle tekening gebeurt, maar ook wat de waarde van de variabele :python:`zijde` is. Die waarde wordt in Mu editor aan de rechterkant getoond. 

    .. figure:: images/debug_step_over.png
        :align: left
        :figwidth: 100%

    Begrijp je nu hoe de while loop werkt? Klik op :guilabel:`Stop` om het debuggen te stoppen. 

.. dropdown:: Meer weten over inspringing van regels?
    :color: info
    :icon: info

    In Python bepaalt de inspringing (Engels: indentation) van een coderegel tot welk blok die regel behoort. Kopieer de onderstaande code naar Mu editor om te zien hoe dat werkt:

    .. code-block:: python
        :linenos:
        :caption: hello_while.py
        :name: hello_while

        i = 0
        while i < 3:
            print('Deze zin wordt drie keer geprint.')
            print('En deze zin valt ook binnen de while lus.')
            i = i + 1
        print('Maar deze zin wordt slechts één keer geprint.')
    
    De regels 3, 4 en 5 van :file:`hello_while.py` zijn ingesprongen: ze worden voorafgegaan door 4 spaties. Daardoor weet Python dat die regels één blokje vormen binnen de while lus.
    Regel 6 is niet ingesprongen en hoort daardoor niet bij het blokje dat wordt herhaald.
    
    Bestudeer nu de volgende code eens, nadat je hem in Mu editor hebt uitgevoerd. Je ziet hier een while lus bínnen een andere while lus.

    .. code-block:: python
        :linenos:
        :caption: turtle_while.py
        :name: turtle_while_v02

        import turtle

        tony = turtle.Turtle()

        vierkant = 0
        while vierkant < 3:
            zijde = 0
            while zijde < 4:
                tony.fd(100)        # Deze regels
                tony.lt(90)         # vallen binnen
                zijde = zijde + 1   # de 2e while lus
            tony.pu()
            tony.lt(120)
            tony.fd(100)
            tony.pd()
            vierkant = vierkant + 1

    De regels 7 t/m 16 in deze code vallen binnen de while lus die begint op regel 6. Maar in dat blok begint op regel 8 een tweede while lus, die de regels 9 t/m 11 herhaalt. Let op de inspringing van regel 12: die valt niet meer onder de tweede while lus.

    Wanneer je in Mu editor op :kbd:`Enter` drukt nadat je regel 6 hebt getypt, springt de volgende regel automatisch in. Wil je handmatig een regel laten inspringen, dan kun je daarvoor de :kbd:`Tab` toets gebruiken (links naast de :kbd:`Q`).

In de volgende opdrachten ga je je eigen while loops schrijven. Je zult merken dat je met loops mooie patronen kunt tekenen.

.. dropdown:: Opdracht 02
    :color: secondary
    :icon: pencil

    Vervang de code in :file:`turtle_while.py` door een programma dat met behulp van een while loop een driehoek tekent met zijden van 100 pixels. Na het tekenen van een zijde moet de turtle telkens 120 graden draaien.

    .. dropdown:: Oplossing
        :color: secondary
        :icon: check-circle

        .. code-block:: python
            :linenos:
            :caption: turtle_while.py
            :name: turtle_while_opdr02

            import turtle

            tony = turtle.Turtle()

            zijde = 0
            while zijde < 3:
                tony.fd(100)
                tony.lt(120)
                zijde = zijde + 1

.. dropdown:: Opdracht 03
    :color: secondary
    :icon: pencil

    Vervang de code in :file:`turtle_while.py` door een programma dat met behulp van een **while loop binnen een andere while loop** vier driehoeken op een rij tekent zoals hieronder afgebeeld.

    .. image:: images/triangles_in_a_row.png
        
    .. dropdown:: Hint
        :color: secondary
        :icon: light-bulb

        Gebruik voor je programma de volgende structuur:

        .. code-block:: python
            :name: turtle_while_opdr03_hint

            import turtle

            tony = turtle.Turtle()

            driehoek = 0
            while driehoek < 4:
                zijde = 0
                while zijde < 3:
                    ...
                    ...
                    ...
                ...
                ...

    .. dropdown:: Oplossing
        :color: secondary
        :icon: check-circle

        .. code-block:: python
            :linenos:
            :caption: turtle_while.py
            :name: turtle_while_opdr03

            import turtle

            tony = turtle.Turtle()

            driehoek = 0
            while driehoek < 4:
                zijde = 0
                while zijde < 3:
                    tony.fd(100)
                    tony.lt(120)
                    zijde = zijde + 1
                tony.fd(100)
                driehoek = driehoek + 1

.. dropdown:: Opdracht 04
    :color: secondary
    :icon: pencil

    Vervang de code in :file:`turtle_while.py` door een programma dat met behulp van een **while loop binnen een andere while loop** 20 vierkanten tekent, waarbij elk vierkant 18 graden gedraaid is ten opzicht van het vorige. Dit moet de volgende figuur opleveren:
    
    .. image:: images/star_of_squares.png

    .. dropdown:: Hint
        :color: secondary
        :icon: light-bulb

        Je programma bestaat uit twee while loops, waarvan de binnenste het tekenen van één vierkant verzorgt. Na het tekenen van een vierkant moet de turtle 18 graden linksom draaien.

        .. code-block:: python
            :name: turtle_while_opdr04_hint

            ...
            while ...:
                # Deze while loop zorgt voor 20 herhalingen.
                ...
                while ...:
                    # Deze while loop zorgt voor één vierkant.
                    ...
                    ...
                tony.lt(18)  # Draai tony 18 graden linksom
                ...

.. dropdown:: Opdracht 05
    :color: secondary
    :icon: pencil

    Maak een nieuw bestand in Mu editor, kopieer onderstaande de code erin en sla het op onder de naam :file:`turtle_dots.py`. 

    .. code-block:: python
        :linenos:
        :emphasize-lines: 8, 10, 12-18
        :caption: turtle_dots.py
        :name: turtle_dots

        import turtle

        tony = turtle.Turtle()
        tony.hideturtle()
        tony.speed(0)

        rij = 0
        while ...:
            kolom = 0
            while ...:
                tony.dot(20, 'red')
                ...
                ...
                ...
                ...
            ...
            ...
            ...
    
    Vervang de puntjes in de gemarkeerde regels door code die ervoor zorgt dat een rooster van 10 bij 10 rode puntjes wordt getekend.

    .. image:: images/red_dots.png


Het wordt nóg interessanter wanneer je de while loop variabele niet alleen als *teller* gebruikt, maar bijvoorbeeld ook aan :python:`turtle.fd()` meegeeft zoals in onderstaand voorbeeld :file:`turtle_spiral.py`.

.. code-block:: python
    :linenos:
    :caption: turtle_spiral.py
    :name: turtle_spiral_v01

    import turtle

    tony = turtle.Turtle()

    lengte = 2
    while lengte < 300:
        tony.fd(lengte)
        tony.lt(30)
        lengte = lengte + 2

Deze code tekent eerst een lijnstukje van 2 pixels, vervolgens een lijnstukje van 4 pixels, dan 6 pixels, dan 8 pixels, enzovoort. En tussendoor draait de turtle telkens 30 graden. Kijk maar eens wat dat oplevert, door de code in Mu editor uit te proberen.

.. dropdown:: Opdracht 06
    :color: secondary
    :icon: pencil

    Experimenteer met de code in :file:`turtle_spiral.py` door telkens één getal een beetje te veranderen en te bekijken hoe de figuur verandert. En wat gebeurt er als je op regel 8 :python:`tony.lt(30)` vervangt door :python:`tony.lt(lengte)` of :python:`tony.lt(3 * lengte)`? Probeer maar uit!

For loops
---------

Een while loop kost je tenminste 3 regels code:

1. Een regel om de tellervariabele aan te maken.
2. Een regel met het :python:`while` statement.
3. Een regel die de tellervariabele aanpast.

Voor het tekenen van een vierkant waarmee deze les begon, zag dat er zo uit:

.. code-block:: python
    :name: while_code

    zijde = 0               # Hier wordt de tellervariabele aangemaakt.
    while zijde < 4:        # Dit is het while statement.
        ...
        ...
        zijde = zijde + 1   # Hier wordt de tellervariabele aangepast.

Een for loop voegt deze drie acties samen in slechts één coderegel. Test de volgende code maar eens in Mu editor:

.. code-block:: python
    :linenos:
    :caption: turtle_for.py
    :name: turtle_for

    import turtle

    tony = turtle.Turtle()

    for zijde in range(4):
        tony.fd(100)
        tony.lt(90)

Waar we in het :ref:`eerste voorbeeld <turtle_while_v01>` van deze les nog 5 regels code nodig hadden om een vierkant te tekenen, hebben we nu genoeg aan 3 regels! Als je een breakpoint in regel 5 plaatst en de :guilabel:`Debug` mode gebruikt (zie :ref:`Opdracht 01 <opdracht-01>` voor uitleg over debuggen), kun je checken dat de waarde van de variabele :python:`zijde` weer van 0 tot en met 3 loopt.

.. dropdown:: Opdracht 07
    :color: secondary
    :icon: pencil

    Vervang de code in :file:`turtle_for.py` door een programma dat de onderstaande figuur tekent. Je mag zelf de kleur en de pendikte bepalen, maar voor het daadwerkelijke tekenen mag je **maximaal 3 regels code** gebruiken.

    .. image:: images/five_pointed_star.png
        :align: center

    .. dropdown:: Hint
        :color: secondary
        :icon: light-bulb

        Vind je het lastig om de draaiingshoek te bepalen? Bedenk dan dat de turtle in totaal 2 keer volledig ronddraait (dus de totale draaiingshoek is 2 * 360° = 720°) en dat die volledige draai over 5 stappen wordt verdeeld.

.. dropdown:: Opdracht 08
    :color: secondary
    :icon: pencil

    Vervang de code in :file:`turtle_for.py` door een programma dat de onderstaande figuur tekent. Deze 'bloem' bestaat uit 10 vierkanten met zijden van lengte 100. Om hem te tekenen heb je twee for loops nodig: één om iets 10 keer uit te voeren en daarbinnen één om een vierkant te tekenen.

    .. image:: images/flower_of_squares.png
        :align: center

    Je kunt de bloem nog mooier maken door :python:`fillcolor()`,  :python:`begin_fill()` en :python:`end_fill()` te gebruiken en een stip (:python:`dot()`) in het midden te plaatsen.

    .. image:: images/flower_of_squares_2.png
        :align: center