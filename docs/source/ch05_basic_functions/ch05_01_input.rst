.. role:: python(code)
    :language: python

.. |br| raw:: html

   <br/>

Input van de gebruiker
=======================

In de voorgaande hoofdstukken hebben we veelvuldig gebruik gemaakt van de functie :python:`print()` om tekst op het scherm te tonen. Het wordt een stuk interessanter wanneer je de gebruiker de mogelijkheid geeft om zelf tekst te typen, waarmee het programma vervolgens iets doet. Op die manier maak je je programma *interactief*. 

.. dropdown:: Wat leer je in dit hoofdstuk
    :open:
    :color: primary
    :icon: book

    * Hoe je met de functie :python:`input()` de gebruiker iets kunt laten typen.
    * ...

De functie :python:`input()` 
-----------------------------

De werking van de functie :python:`input()` kun je het beste begrijpen door het meteen uit te proberen. Maak een nieuw codebestand, met bijvoorbeeld de naam :file:`input.py` en probeer de volgende code uit:

.. code-block:: python
    :linenos:
    :caption: input.py

    # Demonstratie van de functie input()

    print('Hoe heet je?')
    naam = input()
    print(f'Aangenaam kennis te maken {naam}!')

De aanroep :python:`input` in regel 4 zorgt ervoor dat de gebruiker data kan invoeren; in dit geval een naam. De invoer van de gebruiker wordt met het assignment statement opgeslagen in de variabele :python:`naam` .

.. image:: images/input_animation.gif
    :align: center

Opdrachten
-----------

.. dropdown:: Opdracht 01
    :open:
    :color: secondary
    :icon: pencil

    Maak in Mu editor een nieuw codebestand en sla het op onder de naam :file:`foute_strings.py`. Kopieer de onderstaande code naar het bestand:

    .. code-block::
      :linenos:
      :caption: foute_strings.py

      # Strings - opdracht 01

      print('Goedemorgen allemaal!)
      print("Het is nog vroeg."
      print("Kunt u mij de weg naar Hamelen vertellen meneer?')
      print('De opa's reden in oude auto's')
      print(""Wie dit leest is gek", stond op het briefje.")
      print('Opa vroeg: "Wie van de oma's vind je het eigenaardigst?"')
      print('De geheime code is ' + 112358)

    Elk van de regels 3 t/m 9 bevat een of meerdere fouten. Verbeter deze fouten, opdat de teksten goed worden getoond.

.. dropdown:: Opdracht 02
    :open:
    :color: secondary
    :icon: pencil

    Maak in Mu editor een nieuw codebestand en sla het op als :file:`concatenatie.py`. Kopieer de onderstaande code naar het bestand:

    .. code-block::
      :linenos:
      :caption: concatenatie.py

      # Strings - opdracht 02

      naam = "Galahad"
      leeftijd = 10
      favoriete_eten = "gehaktbrood"

      voorsteltekst = ...
      print(voorsteltekst)

    Gebruik de variabelen :python:`naam`, :python:`leeftijd` en :python:`favoriete_eten` om op regel 7 de variabele :python:`voorsteltekst` een waarde te geven, zodanig dat het programma exact (!) de volgende tekst toont:

    ``Hallo! Mijn naam is Galahad. Ik ben 10 jaar oud en mijn favoriete eten is gehaktbrood.``

    Extra uitdaging: gebruik een escape karakter om ervoor te zorgen dat de derde zin van de tekst op een nieuwe regel begint:

    ``Hallo! Mijn naam is Galahad.`` |br| ``Ik ben 10 jaar oud en mijn favoriete eten is gehaktbrood.``