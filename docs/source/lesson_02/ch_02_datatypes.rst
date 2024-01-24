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

De functie :python:`type()`
---------------------------

