.. role:: python(code)
   :language: python

.. |br| raw:: html

   <br/>

Strings
=========

.. dropdown:: Wat leer je in dit hoofdstuk
    :open:
    :color: primary
    :icon: book

    * :bdg-warning:`NOG AANVULLEN`

Aanhalingstekens
---------------------------
Wanneer programmeurs het hebben over een *string*, bedoelen zij daarmee een reeks van karakters. Die karakters vormen meestal een woord, een zin of een nog grotere tekst, maar dat hoeft niet per se. Het kan ook een onbegrijpelijke tekenreeks zijn zoals ``P%5_9#à2o``. Om een stringwaarde te kunnen onderscheiden van andere woorden in je code zoals keywords en variabelenamen, moet je haar tussen aanhalingstekens zetten. Door die aanhalingstekens kan Python zien waar de string begint en eindigt. Je mag enkele (:kbd:`'`) of dubbele (:kbd:`"`) aanhalingstekens gebruiken:

.. code-block:: python

  'Dit is een string tussen enkele aanhalingstekens.'
  "Dit is een string tussen dubbele aanhalingstekens."

.. dropdown:: Hoe typ je aanhalingstekens?
    :color: info
    :icon: info

    Een aanhalingsteken typ je door eerst op de toets met het aanhalingsteken :kbd:`'` te drukken, gevolgd door :kbd:`Spatie`. Het aanhalingsteken verschijnt pas nadat je op de spatiebalk heb gedrukt.

    .. image:: ../images/typing_quotes_small.png

    Om dubbele aanhalingstekens te typen, houd je :kbd:`Shift` ingedrukt terwijl je op :kbd:`'` drukt. En daarna weer :kbd:`Spatie`.

    Deze methode met de spatiebalk werkt alleen als je toetsenbord op United States-International staat ingesteld, maar dat is in Nederland meestal het geval.

    .. image:: images/keyboard_settings.png

    Je kunt met deze methode ook letters met accenten typen. Typ bijvoorbeeld :kbd:`'` gevolgd door :kbd:`e` om een é te krijgen, of :kbd:`"` gevolgd door :kbd:`o` voor een ö.

Je moet wel consequent zijn: als je een string met een enkel aanhalingsteken begint, dien je ook met een enkel aanhalingsteken te eindigen. Anders krijg je een foutmelding:

.. prompt:: raw >>> auto

  >>> 'Dit is een string tussen verschillende aanhalingstekens."
  SyntaxError: EOL while scanning string literal


Escapes
--------
Een string kan bestaan uit letters, cijfers, leestekens en andere symbolen, maar er is één teken dat problemen oplevert: het aanhalingsteken! Stel dat je de volgende zin in een stringvariabele zou willen opslaan:

.. rst-class:: center

  ``Ook opa's en oma's kunnen leren programmeren!``

Dan zou je dat wellicht als volgt doen:

.. prompt:: python >>> auto

  >>> zin = 'Ook opa's en oma's kunnen leren programmeren!'

Hierop reageert Python als volgt:

.. prompt:: raw >>> auto

    File "<stdin>", line 1
      zin = 'Ook opa's en oma's kunnen leren programmeren!'
                    ^
  SyntaxError: invalid syntax

De *apostrof* (zo noem je die zwevende komma) in het woord ``opa's`` ziet Python aan voor een aanhalingsteken, waardoor het denkt dat de string is afgelopen. Omdat er na die apostrof nog tekst volgt, waar Python niks van begrijpt, krijgen we een SyntaxError.

De backslash
^^^^^^^^^^^^

Je kunt het apostrofprobleem oplossen door de apostrofs in de string vooraf te laten gaan door een backslash (:kbd:`\\`). Dat noemen we *escapen*.

.. prompt:: python >>> auto

  >>> zin = 'Ook opa\'s en oma\'s kunnen leren programmeren!'

Als je vervolgens de waarde van :python:`zin` opvraagt in de CLI, zie je iets opmerkelijks:

.. prompt:: python >>> auto

  >>> zin
  "Ook opa's en oma's kunnen leren programmeren!"

Python heeft van de enkele aanhalingstekens dubbele gemaakt en de backslashes zijn verdwenen. Blijkbaar kun je in een string die wordt begrensd door dubbele aanhalingstekens zonder problemen enkele aanhalingstekens gebruiken. En het omgekeerde kan ook:

.. prompt:: python >>> auto

  >>> zin = 'Ada zegt: "Iedereen kan leren programmeren."'

Je ziet hier een string begrensd door enkele aanhalingstekens waarin dubbele aanhalingstekens voorkomen. Wanneer je zowel enkele als dubbele aanhalingstekens in een string verwerkt, ontkom je echter niet meer aan escapes:

.. prompt:: python >>> auto

  >>> zin = 'Ada zegt: "Ook opa\'s en oma\'s kunnen leren programmeren!"'

of:

.. prompt:: python >>> auto

  >>> zin = "Ada zegt: \"Ook opa's en oma's kunnen leren programmeren!\""

.. dropdown:: Opdracht 01
    :color: secondary
    :icon: pencil

    Maak in Mu editor een bestand :file:`hello_strings.py` met daarin de volgende code:

    .. code-block:: python
        :linenos:
        :caption: hello_strings.py code

        tekst_01 = ...
        tekst_02 = ...
        tekst_03 = ...

        print(tekst_01)
        print(tekst_02)
        print(tekst_03)

    Vervang de puntjes in regels 1, 2 en 3 door strings, zodat de output van het programma als volgt is:

    .. code-block:: text
        :caption: hello_strings.py output
        :class: no-copybutton

        's Ochtends en 's avonds poets ik mijn tanden.
        "Heb je je tanden wel gepoetst?", vroeg mijn vader.
        Ik zei: "Al mijn opa's en oma's hebben een kunstgebit."

Escape characters
^^^^^^^^^^^^^^^^^

Naast aanhalingstekens kun je nog enkele escapes gebruiken in strings:

.. list-table::
    :header-rows: 1

    * - Code
      - Doel
    * - :python:`\\'` en :python:`\\"`
      - Aanhalingsteken of apostrof
    * - :python:`\\\\`
      - Backslash
    * - :python:`\\n`
      - Regeleinde 
    * - :python:`\\t`
      - Tab

Het effect van :python:`\\n` en :python:`\\t` zie je pas wanneer je :python:`print()` aanroept om een string af te drukken:

.. prompt:: python >>> auto

  >>> tekst = 'Eerste regel.\nTweede regel.'
  >>> tekst
  'Eerste regel.\nTweede regel.'
  >>> print(tekst)
  Eerste regel.
  Tweede regel.

Met het *new line escape character* :python:`\\n` kun je dus bij het afdrukken van een string de cursor naar de volgende regel laten springen. Het *tab escape character* voegt een witruimte in, alsof je op de :kbd:`Tab` toets drukt:

.. prompt:: python >>> auto
  
  >>> tekst = 'Naam:\tAlan Turing'
  >>> print(tekst)
  Naam:  Alan Turing
  >>> tekst = 'Naam:\t\tAlan Turing'
  >>> print(tekst)
  Naam:          Alan Turing

Tab karakters gebruikt men vaak om tekst recht onder elkaar uit te lijnen:

.. grid:: 2
  :padding: 0

  .. grid-item:: 
    :columns: auto

    .. code-block:: python
      :caption: Code
      :linenos:

      print('Voornaam:\tAlan')
      print('Achternaam:\tTuring')
      print('Geboortedatum:\t23 juni 1912')
      print('Nationaliteit:\tBrits')

  .. grid-item:: 
    :columns: auto

    .. code-block:: text
      :caption: Output
      :class: no-copybutton

      Voornaam:      Alan
      Achternaam:    Turing
      Geboortedatum: 23 juni 1912
      Nationaliteit: Brits

.. dropdown:: Opdracht 02
    :color: secondary
    :icon: pencil

    Voeg aan :file:`hello_strings.py` op regel 9 de volgende :python:`print()` aanroep toe: 

    .. code-block:: python
        :linenos:
        :lineno-start: 9
        :caption: hello_strings.py code

        print('Naam:GarfieldDiersoort:katLievelingseten:lasagneHekel aan:maandagen')

    Plaats escape karakters :python:`\\t` en :python:`\\n` (en geen andere karakters zoals bijvoorbeeld spaties) in de stringwaarde tussen de haakjes om ervoor te zorgen dat deze ene coderegel de volgende output produceert, waarbij de tekst mooi recht onder elkaar staat:

    .. code-block:: text
        :caption: hello_strings.py output
        :class: no-copybutton

        Naam:                Garfield
        Diersoort:           kat
        Lievelingseten:      lasagne
        Hekel aan:           maandagen  

Multiline strings
-----------------

Met het :python:`\\n` escape character kun je dus multiline (meerregelige) strings maken, maar er is nog een andere manier. Wanneer je je string begrenst met maar liefst drie aanhalingstekens, kun je een multiline string typen door meerdere regels in je code te gebruiken:

.. code-block:: python
  :linenos:

  multiline_string = '''Regel 01.
  Regel 02.
  Regel 03.'''

  print(multiline_string)

Zoals je ziet begint de string in deze code op regel 1 en eindigt op regel 3. Het is zelfs mogelijk om dit in de CLI te doen:

.. prompt:: python >>>,... auto
  
  >>> multiline_string = '''Regel 01.
  ... Regel 02.
  ... Regel 03.'''

De CLI snapt door het gebruik van :python:`'''` dat je aan het einde van de eerste regel nog niet klaar bent en plaatst nadat je op :kbd:`Enter` drukt drie puntjes op de volgende regel, zodat je verder kunt gaan met de string. Pas na de afsluitende :python:`'''` wordt de code uitgevoerd. Wanneer je vervolgens de waarde van :python:`multiline_string` opvraagt, zie je dat Python zelf de :python:`\\n` escapes heeft ingevoegd:

.. prompt:: python >>>,... auto
  
  >>> multiline_string
  'Regel 01.\nRegel 02.\nRegel 03.'

In een string tussen drie aanhalingstekens hoef je andere aanhalingstekens ook niet meer te escapen met backslashes:

.. prompt:: python >>> auto

  >>> zin = '''Ada zegt: "Ook opa's en oma's kunnen leren programmeren!"'''

Waarden embedden met f-strings
-------------------------------

In het hoofdstuk :doc:`Datatypes <ch_02_datatypes>` werd de volgende manier getoond om de waarde van een variabele :python:`score` te *embedden* (in te bedden) in een string:

.. prompt:: python >>> auto 

    >>> score = 100
    >>> score_message = 'Uw score is ' + str(score) + ' punten!'
    >>> print(score_message)
    Uw score is 100 punten!

Er is echter een mooiere, eenvoudigere manier om waarden in strings op te nemen, namelijk door zogenoemde *f-strings* (formatted strings) te gebruiken. Een f-string maak je door de letter :python:`f` vóór het eerste aanhalingsteken te typen. Vervolgens kun je een variabelewaarde embedden door de naam tussen *accolades* :python:`{ }` in de string te zetten. Dat ziet er dan zo uit:

.. prompt:: python >>> auto 

    >>> score = 100
    >>> score_message = f'Uw score is {score} punten!'
    >>> print(score_message)
    Uw score is 100 punten!

Voordelen van deze methode zijn onder andere dat je niet meer hoeft te typecasten met de :python:`str()` functie en dat de code beter leesbaar is.
|br|
Uiteraard kun je meerdere variabelen embedden in een f-string:

.. prompt:: python >>> auto 

    >>> naam = 'Guido'
    >>> leeftijd = 68
    >>> print(f'Mijn naam is {naam} en ik ben {leeftijd} jaar oud.')
    Mijn naam is Guido en ik ben 68 jaar oud.

Strings en turtle
-----------------

