.. role:: python(code)
   :language: python

.. |br| raw:: html

   <br/>

Datatypes
=========

.. dropdown:: Wat leer je in dit hoofdstuk
    :open:
    :color: primary
    :icon: book

    * [NOG AANVULLEN]

Getallen, tekst en waarheid
---------------------------

Wanneer je in Python twee getallen door elkaar deelt, gebeurt er iets opvallends:

.. prompt:: python >>> auto

    >>> 6 / 2
    3.0

Je zou verwachten dat :python:`6` gedeeld door :python:`2` het getal :python:`3` oplevert, maar Python maakt er :python:`3.0` van. Waarom komt die :python:`.0` er ineens bij?

In de :ref:`voorbeeldcode <code_example_using_variables>` over het gebruik van variabelen zag je iets soortgelijks:

.. prompt:: python >>> auto

    >>> 12 * 2.50
    30.0

Wellicht denk je: ':python:`30` en :python:`30.0` zijn toch dezelfde getallen, waar maak je je druk over?' Maar voor Python zijn deze getallen níet hetzelfde. Het maakt onderscheid tussen gehele getallen en kommagetallen (die in Python niet met een komma worden genoteerd maar met een punt). De eerste worden *integers* genoemd en de tweede *floats*.

.. card::

    .. list-table:: 
        :header-rows: 1

        * - Naam
          - Afkorting 
          - Betekenis
          - Voorbeeld 
        * - Integer
          - :python:`int` 
          - Geheel getal
          - :python:`42`
        * - Float
          - :python:`float` 
          - Kommagetal
          - :python:`7.5`

Python gebruikt bij het maken van berekeningen onder meer de volgende regels:

* deling van twee getallen resulteert *altijd* in een :python:`float`;
* wanneer in een vermenigvuldiging van getallen een :python:`float` voorkomt, is het resultaat ook een :python:`float`.     

Nu begrijp je waarom de deling :python:`6 / 2` het resultaat :python:`3.0` geeft en de vermenigvuldiging :python:`12 * 2.50` het getal :python:`30.0` oplevert. De :python:`.0` in de uitkomsten laat zien dat het floats zijn. 

Integer en float zijn zogenoemde *datatypes*. Het datatype van een waarde geeft aan met welk soort waarde je te maken hebt. Python kent verscheidene datatypes, van heel eenvoudig tot zeer complex. De belangrijkste voor dit moment zijn de volgende vier:

.. card:: 

    .. list-table:: 
        :header-rows: 1

        * - Datatype
          - Afkorting 
          - Betekenis
          - Voorbeeld 
        * - Integer
          - :python:`int` 
          - Geheel getal
          - :python:`42`
        * - Float
          - :python:`float` 
          - Kommagetal
          - :python:`7.5`
        * - String
          - :python:`str`
          - Tekst
          - :python:`'Hello, world!'`
        * - Boolean
          - :python:`bool`
          - Waarheid
          - :python:`True`   

| Zoals je ziet, noemen we een tekstwaarde in Python een *string*. Strings moeten altijd tussen aanhalingstekens staan om ervoor te zorgen dat Python ze ook als zodanig herkent. 
| Een waarde van het datatype *boolean* geeft aan of iets *waar* of *niet waar* is. Er zijn dus slechts twee waarden mogelijk: :python:`True` en :python:`False`. Merk op dat deze in Python met een hoofdletter worden geschreven!

Programmeertalen gebruiken datatypes om vast te kunnen stellen of een bepaalde bewerking toegestaan is. Het is bijvoorbeeld geen probleem om twee integers met elkaar te vermenigvuldigen, maar twee strings kan niet:

.. prompt:: text >>> auto

    >>> 4 * 6
    24
    >>> 'vier' * 'zes'
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    TypeError: can't multiply sequence by non-int of type 'str'

Zoals je ziet, geeft Python een TypeError wanneer je twee strings probeert te vermenigvuldigen. In het vorige hoofdstuk zag je dat je twee strings wel kunt optellen en je kunt ook een string met een integer vermenigvuldigen:

.. prompt:: python >>> auto

    >>> 'Dit ' + 'is ' + 'een ' + 'zin.'
    'Dit is een zin.'
    >>> 5 * 'bla'
    'blablablablabla'

Voordat Python een berekening uitvoert, checkt het eerst de datatypes van de waarden in die berekening om vast te stellen of de berekening überhaupt mogelijk is. 

De functie :python:`type()`
---------------------------

Als je het voorgaande hebt begrepen, kun je nu herkennen wat het datatype is van bijvoorbeeld de waarde :python:`5.8` of van de waarde :python:`'datatype'`. Mocht je er nog onzeker over zijn, dan kun je de functie :python:`type()` gebruiken, waaraan je tussen de haakjes een waarde meegeeft:

.. prompt:: python >>> auto

    >>> type(5.8)
    <class 'float'>
    >>> type('datatype')
    <class 'str'>

Je ziet dat Python :python:`5.8` als een float identificeert en :python:`'datatype'` als een string.    

.. dropdown:: Opdracht 01
    :color: secondary
    :icon: pencil

    Run in Mu editor het lege bestand :file:`blank.py` dat je in het hoofdstuk :ref:`Variabelen <blank-py>` maakte om in de CLI te kunnen werken. Gebruik in de CLI de functie :python:`type()` om achtereenvolgens de datatypes van de onderstaande waarden te verkrijgen. Druk telkens pas op :kbd:`Enter` nadat je zelf een voorspelling hebt gedaan over het resultaat.

    * :python:`100`
    * :python:`-2`
    * :python:`True`
    * :python:`'True'`
    * :python:`'3.14'`
    * :python:`3.14`

.. dropdown:: Opdracht 02
    :color: secondary
    :icon: pencil

    Je kunt aan :python:`type()` in plaats van een waarde ook een *expressie* meegeven. Een expressie evalueert tenslotte naar een waarde. Voorspel de uitkomsten van de onderstaande :python:`type()`-aanroepen en test in de CLI of je voorspelling klopt.

    .. prompt:: python >>> auto 

        >>> type(10 + 6)
        ...
        >>> type(12 / 3)
        ...
        >>> type(5 * 2.0)
        ...
        >>> type(7 * 'ha')
        ...
        >>> type('Tot' + ' ' + 'ziens!')
        ...
        >>> type(6 > 2)
        ...

    De expressie :python:`6 > 2` in de laatste regel betekent '6 is groter dan 2'. We komen later terug op dit soort expressies. 

.. dropdown:: Opdracht 03
    :color: secondary
    :icon: pencil

    | Je kunt aan :python:`type()` ook een variabele meegeven. Een variabele bevat immers een waarde.
    | Maak in Mu editor een nieuw bestand :file:`datatypes.py` en kopieer onderstaande code erin.

    .. code-block:: python
        :linenos:
        :caption: datatypes.py

        import turtle

        getal = 18
        tekst = 'Tony is een schildpad.'
        getal_is_klein = getal < 100
        tony = turtle.Turtle()

        print('De waarde van de variabele getal is', getal)
        print('Het datatype van de variabele getal is', type(getal))

    Run de code. Als het goed is, zie je de volgende output:

    .. prompt:: raw

        De waarde van de variabele getal is 18
        Het datatype van de variabele getal is <class 'int'>

    Vul de code aan zodat op dezelfde manier de waarden en datatypes van de variabelen :python:`tekst`, :python:`getal_is_klein` en :python:`tony` worden getoond.

Type casting
------------

Als je programmeert, komt het regelmatig voor dat je een waarde van een bepaald datatype krijgt, terwijl je liever een ander datatype zou hebben. Dan is het handig als je het datatype kunt veranderen. Het veranderen van een datatype noemen we *type casting*. In Python kun je daar de volgende functies voor gebruiken:

.. list-table::
    :header-rows: 1

    * - Functie
      - Werking 
    * - :python:`int(value)`
      - Converteert value naar een integer, indien mogelijk.
    * - :python:`float(value)`
      - Converteert value naar een float, indien mogelijk.
    * - :python:`str(value)`
      - Converteert value naar een string, indien mogelijk.
    * - :python:`bool(value)`
      - Converteert value naar een boolean, indien mogelijk.

In het voorbeeld hieronder zie je dat de variabele :python:`spam` de waarde '5' krijgt. Het datatype van :python:`spam` is dus :python:`string`.

.. prompt:: python >>> auto 

    >>> spam = '5'
    >>> type(spam)
    <class 'str'>

Met de functie :python:`int()` kun je de *string*\waarde :python:`'5'` converteren naar de *integer*\waarde :python:`5`:

    >>> spam = '5'
    >>> spam
    '5'
    >>> int(spam)
    5

Echter de waarde van :python:`spam` is hierdoor niet gewijzigd:

    >>> spam = '5'
    >>> int(spam)
    5
    >>> spam
    '5'

Om :python:`spam` te veranderen in een integervariabele, gebruik je een assignment statement:

    >>> spam = '5'
    >>> spam = int(spam)   # assignment statement
    >>> spam
    5
    >>> type(spam)
    <class 'int'>

Een standaard onderdeel bij het programmeren van een game is het tonen van de score aan de speler. Meestal is de score een integer waarde. Voor het tonen van informatie aan de gebruiker heb je echter liever een string omdat je die aan andere stringwaarden kunt plakken met de :python:`+` operator. Dan kun je handig gebruik maken van de :python:`str()` functie:

    >>> score = 100
    >>> score_message = 'Uw score is ' + str(score) + ' punten!'
    >>> print(score_message)
    Uw score is 100 punten!