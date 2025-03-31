.. role:: python(code)
   :language: python

.. |br| raw:: html

   <br/>

Levens verliezen
===================

In de huidige versie van onze Endless Runner is het spel afgelopen zodra de dinosaurus een cactus raakt. Misschien vind je het leuker om de speler een aantal levens te geven en het spel pas te beëindigen als de levens op zijn. In dit deel gaan we dat programmeren.

Knipperende dino
--------------------

Als de dinosaurus een cactus raakt, willen we dat de dinosaurus even knippert. Dat maakt voor de speler duidelijk dat er iets is gebeurd, en bovendien kan de dino tijdens het knipperen niet nogmaals worden geraakt door een cactus.

.. figure:: images/flash.gif

Er zijn meerdere manieren om het knippereffect te programmeren. Je zou bijvoorbeeld de :python:`player.images` lijst kunnen wijzigen naar een lijst waarin zich ook *lege* sprites bevinden. Dat zijn sprites die volledig transparant zijn. Als je dit wilt proberen, download dan :download:`empty.png <../game_assets/endless_runner/images/empty.png>` en plaats het in de :file:`images` map. Vervolgens voeg je aan je code een tweede lijst met sprites toe:

.. code-block:: python
   :caption: endlessrunner.py
   :linenos:
   :lineno-start: 19
   :emphasize-lines: 4

   # Actors
   player = Actor('walk00')
   walk_images = ['walk00', 'walk01', 'walk02', 'walk03']
   hit_images = ['walk00', 'empty', 'walk01', 'empty', 'walk02', 'empty', 'walk03', 'empty']
   player.images = walk_images

Wanneer de dino een cactus raakt, kun je de :python:`player.images` variabele veranderen naar de :python:`hit_images` lijst. Na een paar seconden kun je de :python:`player.images` weer terugzetten naar de :python:`walk_images` lijst. Dit is een manier om het knippereffect te programmeren.

Je kunt het knipperen echter ook laten gebeuren door in de :python:`draw()` functie de dino afwisselend wél en níet te laten tekenen. Deze manier is iets ingewikkelder, maar je hebt meer controle over de snelheid van het knipperen en je hebt geen extra sprite nodig. In dit deel beschrijven we deze manier.

Voeg allereerst een nieuwe constante toe aan de code, die de duur van het knipperen bepaalt.

.. code-block:: python
   :caption: endlessrunner.py
   :linenos:
   :lineno-start: 9
   :emphasize-lines: 6

   # Constanten
   HORIZON = 400
   BASELINE = HORIZON + 45
   GRAVITY = 1
   SPEED = 8
   BLINK_DURATION = 45

De constante :python:`BLINK_DURATION` geeft aan hoe lang de dino moet knipperen in frames. In dit geval is dat 45 frames, wat ongeveer 0,75 seconden is. Dit is een goede tijd om de dino te laten knipperen. Je kunt deze waarde natuurlijk ook aanpassen naar eigen voorkeur.

Aan de :python:`player` actor voegen we twee nieuwe variabelen toe: :python:`is_blinking` en :python:`blink_timer`. De eerste is een boolean die aangeeft of de dino aan het knipperen is. De tweede is een timer die bijhoudt hoe lang de dino al knippert. Voeg de volgende regels toe aan de code: 

.. code-block:: python
   :caption: endlessrunner.py
   :linenos:
   :lineno-start: 20
   :emphasize-lines: 9-10

   # Actors
   player = Actor('walk00')
   walk_images = ['walk00', 'walk01', 'walk02', 'walk03']
   player.images = walk_images
   player.fps = 10
   player.left = 10
   player.bottom = BASELINE
   player.vy = 0
   player.is_blinking = False
   player.blink_timer = BLINK_DURATION

In de :python:`update()` functie moeten we nu een paar dingen regelen:

#. Als de dinosaurus een cactus raakt terwijl hij knippert, mag er niets gebeuren.
#. Als de dinosaurus een cactus raakt en hij is niet aan het knipperen, moet hij gaan knipperen.
#. Als de dinosaurus aan het knipperen is, moet :python:`blink_timer`  worden verlaagd. Zodra de timer op 0 staat, moet de dinosaurus stoppen met knipperen en de timer wordt weer op :python:`BLINK_DURATION` gezet.

We pakken eerst de punten 1 en 2 aan:

.. code-block:: python
   :caption: endlessrunner.py
   :linenos:
   :lineno-start: 91

      if not player.is_blinking and player.collidelist(obstacles) != -1:
         player.is_blinking = True

De dino gaat nu alleen knipperen als hij niet al bezig was met knipperen en een cactus raakt.

Het verlagen van de timer en het stoppen met knipperen regelen we met een nieuw :python:`if` statement in de :python:`update()` functie:

.. code-block:: python
   :caption: endlessrunner.py
   :linenos:
   :lineno-start: 94

      if player.is_blinking:
         player.blink_timer -= 1
         if player.blink_timer <= 0:
               player.is_blinking = False
               player.blink_timer = BLINK_DURATION

Nu moeten we alleen nog de :python:`draw()` functie aanpassen. Dit is misschien wel het ingewikkeldste stukje. We gaan er met een :python:`if` statement voor zorgen dat:

* als :python:`player.is_blinking` :python:`False` is, de dino gewoon wordt getekend;
* als :python:`player.is_blinking` :python:`True` is, de dino wordt getekend als :python:`player.blink_timer` een even getal is en niet wordt getekend als :python:`player.blink_timer` een oneven getal is. Dit zorgt ervoor dat de dino knippert.

In code ziet dat er zo uit:

.. code-block:: python
   :caption: endlessrunner.py
   :linenos:
   :lineno-start: 49
   :emphasize-lines: 8-9

   # Functie draw()
   def draw():
      draw_background()
      if game_over:
         screen.draw.text('Game Over', midbottom = (WIDTH / 2, HEIGHT / 2 - 10), color = 'white', fontsize = 60)
         screen.draw.text(f'Score: {score}', midtop = (WIDTH / 2, HEIGHT / 2 + 10), color = 'white', fontsize = 60)
      else:
         if not player.is_blinking or player.blink_timer % 2 == 0:
               player.draw()
         for obstacle in obstacles:
               obstacle.draw()
         screen.draw.text(f'Score: {score}', (15, 10), color = 'darkorchid4', fontsize = 48)

Kun je je herinneren dat de :python:`%` operator de restwaarde van een deling geeft? Als we bijvoorbeeld 5 % 2 doen, krijgen we 1. Dit komt omdat 2 in 5 gaat met een restwaarde van 1. Als we 4 % 2 doen, krijgen we 0, omdat er geen restwaarde is. Dit is precies wat we hier gebruiken om te bepalen of de timer een even of oneven getal is.

Wanneer je nu het spel speelt, zie je dat het knippereffect werkt, maar veel te snel gaat. De dino knippert nu 30 keer per seconde. Door een extra berekening in regel 56 toe te voegen, kunnen we het knipperen vertragen:

.. code-block:: python
   :class: no-copybutton
   :caption: endlessrunner.py
   :linenos:
   :lineno-start: 56
   :emphasize-lines: 1

         if not player.is_blinking or (player.blink_timer // 5) % 2 == 0:
            player.draw()

Nu delen we de tijd eerst door 5 en bekijken dan of het resultaat even of oneven is. Dit zorgt ervoor dat de dino in een rustiger tempo knippert. Uiteraard kun je zelf experimenteren met de snelheid van het knipperen door de waarde 5 te vervangen door een andere waarde.
