.. role:: python(code)
    :language: python

.. |br| raw:: html

   <br/>

Functies basics
=======================

Je hebt inmiddels kennisgemaakt met de functies :python:`print()`, :python:`input()`, :python:`type()`, :python:`int()`, :python:`float()` en :python:`str()`. Dit zestal vormt slechts het topje van de spreekwoordelijke ijsberg. Functies zijn belangrijke bouwstenen voor een computerprogramma. Hoog tijd dus om er wat dieper op in te gaan.      

.. dropdown:: Wat leer je in dit hoofdstuk
    :open:
    :color: primary
    :icon: book

    * ...

Onderdelen van een functie
----------------------------

Wanneer je in Python :python:`print('Hello, World!')` aanroept, wordt op de achtergrond een stuk code uitgevoerd waardoor de tekst ``Hello, World!`` op het scherm verschijnt. Die code is geprogrammeerd door de makers van Python. Een functie is dan ook eigenlijk een blok code dat je kunt laten uitvoeren wanneer je het nodig hebt. Om dat voor elkaar te krijgen moet je drie dingen weten:

* De naam van de functie.
* De eventuele parameters die de functie nodig heeft (de input).
* De eventuele waarde die de functie teruggeeft (de output).

Je zou een functie enigszins kunnen vergelijken met een recept in een kookboek. Wanneer je een appeltaart wilt bakken, gebruik je het recept ``Appeltaart``. De ingrediënten voor de taart zijn de input en de output is een overheerlijke versgebakken appeltaart.

.. card::

    .. list-table::
        :header-rows: 1
        :align: center
        :stub-columns: 1

        * - 
          - Functie
          - Recept
        * - Naam
          - :python:`str()` 
          - ``Appeltaart``
        * - Input
          - een waarde, bijvoorbeeld :python:`42` 
          - ingrediënten
        * - Output
          - de :python:`string` versie van de waarde: :python:`'42'` 
          - een taart

Meestal verbeelden we een functie als een *black box* of een machientje waar je input in kunt stoppen en waar output uit komt:

.. figure:: images/function_black_box_transparent.png
    :width: 500

