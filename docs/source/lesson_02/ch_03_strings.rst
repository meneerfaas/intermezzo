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
Wanneer programmeurs het hebben over een *string*, bedoelen zij daarmee een reeks van karakters. Die karakters vormen meestal een woord, een zin of een nog grotere tekst, maar dat hoeft niet per se. Het kan ook een onbegrijpelijke tekenreeks zijn zoals P%5_9#à2o. Om een stringwaarde te kunnen onderscheiden van andere woorden in je code zoals keywords en variabelenamen, moet je haar tussen aanhalingstekens zetten. Door die aanhalingstekens kan Python zien waar de string begint en eindigt. Je mag enkele of dubbele aanhalingstekens gebruiken:

.. code-block:: python

  'Dit is een string tussen enkele aanhalingstekens.'
  "Dit is een string tussen dubbele aanhalingstekens."

.. dropdown:: Hoe typ je aanhalingstekens?
    :color: info
    :icon: info

    Een aanhalingsteken typ je door eerst op de toets met het aanhalingsteken :kbd:`'` te drukken, gevolgd door :kbd:`Spatie`. Het aanhalingsteken verschijnt pas nadat je op de spatiebalk heb gedrukt.

    .. image:: ../images/typing_quotes_small.png

    Om dubbele aanhalingstekens te typen, houd je :kbd:`Shift` ingedrukt terwijl je op :kbd:`'` drukt. En daarna weer :kbd:`Spatie`.

Je moet wel consequent zijn: als je een string met een enkel aanhalingsteken begint, moet je ook met een enkel aanhalingsteken eindigen. Anders krijg je een foutmelding:

.. prompt:: raw >>> auto

  >>> 'Dit is een string tussen verschillende aanhalingstekens."
  SyntaxError: EOL while scanning string literal
