.. role:: python(code)
   :language: python

.. |br| raw:: html

   <br/>

Extra oefening: SpeedBrick
============================

Deze opdracht gaat over het reageren op toetsenbordaanslagen en werken met snelheid.

Mappenstructuur
----------------

Voor deze oefening gebruik je de mappenstructuur en de sprite uit de vorige opdracht: :doc:`Brick </ch13_pygame_zero/ch_04_brick>`. Maak in Mu editor een nieuw bestand en sla het op in je :file:`brick` map onder de naam :file:`speedbrick.py`.

.. card::

   .. uml::
      :align: left
      :html_format: svg

      @startuml
         @startfiles
         /games/brick/images/green_brick.png
         /games/brick/brick.py
         /games/brick/speedbrick.py
         @endfiles
      @enduml

Starter code
-------------

Begin met de volgende code in :file:`flying_ball.py`:

.. code-block:: python
   :linenos:

   # Vensterinstellingen
   WIDTH = 600
   HEIGHT = 400
   TITLE = 'SpeedBrick'

   # Actor
   player = Actor('green_brick')
   player.x = WIDTH / 2
   player.y = HEIGHT / 2
   player.speedx = 5  # horizontale snelheid
   player.speedy = 0  # verticale snelheid

   # Event handler on_key_down()
   def on_key_down(key):
      if key == keys.RIGHT:
         player.speedx += 2
      if key == keys.LEFT:
         player.speedx -= 2

   # Functie draw()
   def draw():
      screen.fill('darkorchid4')
      player.draw()

   # Functie update()
   def update():
      player.x += player.speedx
      # Als de snelheid positief is en de legosteen rechts uit het venster verdwijnt:
      if player.speedx > 0 and player.left > WIDTH:
         player.right = 0

Wanneer je deze code uitvoert, zie je dat de legosteen naar rechts beweegt. Test wat er gebeurt wanneer je de rechterpijltjestoets indrukt. Test ook wat er gebeurt wanneer je de linkerpijltjestoets indrukt.

Opdracht
---------

Breid de code uit met de volgende functionaliteit:

* Als de legosteen links uit het venster verdwijnt, moet hij rechts weer verschijnen.
* Voeg een verticale beweging toe aan de legosteen. Indrukken van de pijltjestoetsen omhoog en omlaag moet de verticale snelheid veranderen, op dezelfde manier als bij de horizontale snelheid gebeurt.
* Als de legosteen boven of onder het venster verdwijnt, moet hij respectievelijk onder of boven weer verschijnen.

Extra:

* Verander de getallen zodanig dat de speler de legosteen ook helemaal stil kan zetten met de pijltjestoetsen.
* Als de speler de spatiebalk indrukt, moet de legosteen meteen stil staan.