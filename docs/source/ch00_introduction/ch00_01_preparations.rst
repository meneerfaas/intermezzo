.. role:: python(code)
   :language: python

Voorbereiding
=============

Om te kunnen programmeren heb je een *programmeeromgeving* nodig: een programma waarin je code kunt typen en kunt laten uitvoeren. In deze cursus gebruiken we daarvoor `Mu editor <https://codewith.mu/>`_. Nadat je Mu editor hebt gestart, ga je de benodigde vensters handig rangschikken op je scherm en je eerste programma maken.

.. dropdown:: Wat leer je in dit hoofdstuk
    :open:
    :color: primary
    :icon: book

    * Hoe start je Mu editor.
    * Hoe plaats je vensters in Windows mooi naast elkaar.
    * Hoe typ je programmacode in Mu editor.
    * Hoe run je programmacode in Mu editor.
    * Hoe sla je je programma op in Mu editor.

Mu editor starten
-----------------
Start Mu editor via de Windows Startknop linksonder in je scherm.

.. grid:: 2

    .. grid-item::
        :columns: auto

        .. image:: images/windows_start.png
            :height: 39px

    .. grid-item::
        :columns: auto

        .. image:: images/mu_windows_start.png
            :height: 36px

.. card:: :octicon:`x-circle-fill` Probleem?

    Kun je Mu editor niet vinden in het Startmenu in Windows? Wellicht is het programma dan nog niet geïnstalleerd. Download Mu editor via `deze link <https://codewith.mu/en/download>`_ en installeer het op je PC.

Controleer nadat je Mu editor hebt opgestart, dat rechtsonder in de statusbalk Python 3 staat. Als er iets anders staat, klik dan op de Mode knop en selecteer Python 3.

.. image:: images/mu_editor.png
    

Vensters rangschikken
---------------------
Je hebt nu minstens twee vensters open op je scherm: het venster van de webbrowser waarin je deze tekst leest en het Mu editor venster. Rangschik deze vensters op de volgende manier:

.. tab-set:: 

    .. tab-item:: Stap 1

        Pak met je muis het venster van Mu editor vast bij de balk aan de bovenkant en sleep het venster naar de linkerkant van het scherm totdat de muiscursor de schermrand raakt. Je ziet dan een soort schaduwvenster verschijnen dat de gehele linkerhelft van het scherm beslaat.
        
        .. image:: images/windows_arrange_1_small.png

    .. tab-item:: Stap 2

        Laat de muisknop los en voilà, het venster van Mu editor neemt precies de linkerhelft van het scherm in.

        .. image:: images/windows_arrange_2_small.png

    .. tab-item:: Stap 3

        Zorg er zelf voor dat het venster van je webbrowser op de rechterhelft van het scherm terecht komt. 

        .. image:: images/windows_arrange_3_small.png

        Nu staan de twee vensters die je nodig hebt mooi naast elkaar, waardoor je tegelijkertijd deze uitleg kunt volgen en code kunt typen.

Je eerste programma
-------------------

Nu ben je gereed om je eerste programma te maken in Mu editor. Het woord programma is enigszins overdreven, want het bestaat slechts uit twee regels code. Typ de onderstaande code voor het programma :file:`hello_word.py` in Mu editor. Uiteraard hoef je de regelnummers 1 en 2 niet te typen.

.. code-block:: python
    :class: no-copybutton
    :linenos:
    :caption: hello_world.py
    :name: hello_world

    # Dit is mijn eerste programma
    print('Hello, World!')

.. dropdown:: Hoe typ je aanhalingstekens? (Klik op deze balk om de uitleg te openen.)
    :color: info
    :icon: info

    Een aanhalingsteken typ je door eerst op de toets met het aanhalingsteken :kbd:`'` te drukken, gevolgd door :kbd:`Spatie`. Het aanhalingsteken verschijnt pas nadat je op de spatiebalk heb gedrukt.

    .. image:: images/typing_quotes_small.png

    Je kunt ook dubbele aanhalingstekens gebruiken (voor Python maakt dat weinig uit). Daarvoor moet je :kbd:`Shift` ingedrukt houden terwijl je op :kbd:`'` drukt. En daarna weer :kbd:`Spatie`.

Klik in de knoppenbalk op :guilabel:`Save` om het bestand op te slaan. Navigeer naar je Gymnasium Beekvliet Sharepoint map en sla daarin het bestand op onder de naam :file:`hello_world`.

.. image:: images/mu_save_file.png

Klik in de knoppenbalk op :guilabel:`Run` om je programma uit te voeren. Als je alles goed hebt gedaan, wordt de tekst :code:`Hello, World!` getoond.

.. image:: images/mu_hello_world.png

Klik in de knoppenbalk op de knop :guilabel:`Stop` om de uitvoering van het programma te stoppen.

.. dropdown:: Wist je dat?
    :open:
    :color: info
    :icon: info

    Een programma dat :code:`Hello, World!` op het scherm toont, is traditioneel het eerste dat elke programmeur maakt wanneer zij/hij een nieuwe programmeertaal leert. Het is eenvoudig, maar toch heb je nu al een aantal dingen geleerd:

    * Hoe je in Mu editor code typt, opslaat en uitvoert.
    * Dat je in Python met een hekje :python:`#` commentaar kunt aangeven. Commentaar wordt door Python genegeerd bij het uitvoeren van de code.
    * Dat je in Python een tekst op het scherm kunt tonen met de functie :python:`print()` en dat de tekst tussen aanhalingstekens moet staan.

..
    Je bent klaar voor het echte werk. Ga door met :doc:`lesson_01_algorithms`.