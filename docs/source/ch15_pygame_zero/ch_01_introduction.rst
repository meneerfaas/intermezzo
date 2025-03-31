.. role:: python(code)
   :language: python

.. |br| raw:: html

   <br/>

Endless Runner
================

Een `Endless Runner <https://en.wikipedia.org/wiki/Endless_runner>`_ is een soort platformspel waarin de speler oneindig kan rennen door een landschap vol obstakels. De speler kan de obstakels ontwijken door te springen (en soms ook door te bukken of naar links en rechts te bewegen). Het doel is zo lang mogelijk te overleven en een zo hoog mogelijke score te behalen. Het bekendste voorbeeld is waarschijnlijk de `Google Dino <https://trex-runner.com/>`_ game.

.. image:: images/google_dino.gif
   :class: border
   :align: center

De Endless Runner die we hier gaan maken is geïnspireerd op de `Engelstalige tutorial <https://quirkycort.github.io/tutorials/20-Pygame-Zero-Basics/30-Ninja/10-infinite.html>`_ van `A Posteriori <https://www.aposteriori.com.sg/>`_.

Voorbereiding
---------------

Maak voor dit project in je :file:`games` map een nieuwe map aan met de naam :file:`endlessrunner`. Maak in die nieuwe map ook alvast de map :file:`images` aan. 

Download de sprites die we gaan gebruiken: :download:`assets.zip <../game_assets/endless_runner/assets.zip>`. Dit is een zip-bestand dat alle benodigde sprites bevat. Open het zip-bestand en plaats de sprites in de :file:`images` map in de :file:`endlessrunner` map.

Download :download:`pgzhelper.py <https://raw.githubusercontent.com/QuirkyCort/pgzhelper/main/pgzhelper.py>` en plaats het in de :file:`endlessrunner` map. Dit bestand bevat een aantal handige functies die we gaan gebruiken in de game.

Maak in Mu Editor een nieuw bestand en sla het op in je :file:`endlessrunner` map onder de naam :file:`endlessrunner.py`.

Als je alles goed hebt gedaan, zou je nu de volgende structuur moeten hebben:

.. card::

   .. uml::
      :align: left
      :html_format: svg

      @startuml
         @startfiles
         /games/endlessrunner/images/cactus00.png
         /games/endlessrunner/images/cactus01.png
         /games/endlessrunner/images/cactus02.png
         /games/endlessrunner/images/cactus03.png
         /games/endlessrunner/images/cactus04.png
         /games/endlessrunner/images/cactus05.png
         /games/endlessrunner/images/heart00.png
         /games/endlessrunner/images/heart01.png
         /games/endlessrunner/images/heart02.png
         /games/endlessrunner/images/heart03.png
         /games/endlessrunner/images/heart04.png
         /games/endlessrunner/images/heart05.png
         /games/endlessrunner/images/heart06.png
         /games/endlessrunner/images/heart07.png
         /games/endlessrunner/images/heart08.png
         /games/endlessrunner/images/heart09.png
         /games/endlessrunner/images/heart10.png
         /games/endlessrunner/images/idle.png
         /games/endlessrunner/images/walk00.png
         /games/endlessrunner/images/walk01.png
         /games/endlessrunner/images/walk02.png
         /games/endlessrunner/images/walk03.png  
         /games/endlessrunner/endlessrunner.py
         /games/endlessrunner/pgzhelper.py
         @endfiles
      @enduml

Bronnen
---------
De assets die we gebruiken in deze les zijn afkomstig van de volgende websites:

* Dino sprites: `Freepik.com <https://www.freepik.com/free-vector/cartoon-dinosaur_996559.htm>`_ 
* Cactus sprites: `Freepik.com <https://www.freepik.com/premium-vector/cacti-pixel-art-set-cactus-with-flowers-collection-desert-flora-8-bit-sprite_28762544.htm>`_
* Heart sprites: `Vecteezy.com <https://www.vecteezy.com/vector-art/14177554-animation-sprite-sheet-of-red-heart-rotation>`_.