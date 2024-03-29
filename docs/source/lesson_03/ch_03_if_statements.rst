.. role:: python(code)
   :language: python

Als... dan...
=============

Je hebt inmiddels kennisgemaakt met :python:`while` loops, die je in staat stellen een blok code te herhalen. In dit hoofdstuk behandelen we het :python:`if` statement, waarmee Python kan kiezen om een blok code wel of niet uit te voeren.

Kopieer onderstaande code naar een nieuw bestand in Mu editor en sla het op als hello_if.py. 

.. code-block:: python
    :linenos:
    :caption: hello_if.py
    :name: hello_if_v01

    # Functie say_hello() toont een begroeting
    def say_hello(name):
        print("Hallo", name)
        
    # Hoofdprogramma
    say_hello("Tony")
    say_hello("Tina")

In :file:`hello_if.py` wordt de functie :python:`say_hello()` gedefinieerd, die een begroeting op het scherm toont. In regels 6 en 7 wordt deze functie aangeroepen met twee verschillende namen. De output van het programma is:

.. code-block:: text
    :caption: hello_if.py output
    :name: hello_if_v01_output

    Hallo Tony
    Hallo Tina

Nu gaan we de functie :python:`say_hello()` uitbreiden met een :python:`if` statement:

.. code-block:: python
    :linenos:
    :emphasize-lines: 3,4
    :caption: hello_if.py
    :name: hello_if_v02

    # Functie say_hello() toont een begroeting
    def say_hello(name):
        if name == "Tony":
            print("Hallo", name)
        
    # Hoofdprogramma
    say_hello("Tony")
    say_hello("Tina")

Met het dubbele is-gelijk-aan-teken :python:`==` kun je Python laten checken of twee waarden aan elkaar gelijk zijn. Regel 3 van :file:`hello_if.py` kun je dus lezen als: 'Als de waarde van de variabele :python:`name` gelijk is aan :python:`"Tony"`, doe dan het volgende.' Merk op dat de inspringing van regel 4 aangeeft dat die regel binnen het :python:`if` statement valt.

Wanneer je deze code runt, is de output:

.. code-block:: text
    :caption: hello_if.py output
    :name: hello_if_v02_output

    Hallo Tony

Het programma toont nu alleen een begroeting als de naam Tony wordt gebruikt en anders niet.

If en else
----------

Een :python:`if` statement gebruik je om Python te vertellen: *'Als er dit aan de hand is, doe dan het volgende.'* Met het keyword :python:`else`  kun je dat uitbreiden naar *'Als er dit aan de hand is, doe dan het volgende, en zo niet, doe dan iets anders.'*

Wijzig de functie :python:`say_hello()` als volgt:

.. code-block:: python
    :linenos:
    :emphasize-lines: 5-8
    :caption: hello_if.py
    :name: hello_if_v03

    # Functie say_hello() toont een begroeting
    def say_hello(name):
        if name == "Tony":
            print("Hallo", name)
            print("Leuk je weer te zien.")
        else:
            print("Hallo", name)
            print("Aangenaam kennis te maken.")
        
    # Hoofdprogramma
    say_hello("Tony")
    say_hello("Tina")

Begrijp je wat hier gebeurt? De regels 4 en 5 worden uitgevoerd als aan de functie :python:`say_hello()` het argument :python:`"Tony"` wordt meegegeven. In alle andere gevallen worden de regels 7 en 8 uitgevoerd. Je kunt aan het hoofdprogramma nog extra regels toevoegen om het effect te zien:

.. code-block:: python
    :linenos:
    :lineno-start: 10
    :emphasize-lines: 2
    :caption: hello_if.py
    :name: hello_if_v04

    # Hoofdprogramma
    say_hello("Tabe")
    say_hello("Tess")
    say_hello("Tony")
    say_hello("Tina")

Run het programma en zie dat alleen bij de naam Tony de reactie 'Leuk je weer te zien.' wordt geprint.

Wanneer je deze code runt, is de output:

.. code-block:: text
    :emphasize-lines: 5,6
    :caption: hello_if.py output
    :name: hello_if_v04_output

    Hallo Tabe
    Aangenaam kennis te maken.
    Hallo Tess
    Aangenaam kennis te maken.
    Hallo Tony
    Leuk je weer te zien.
    Hallo Tina
    Aangenaam kennis te maken.

.. dropdown:: Opdracht 01
    :color: secondary
    :icon: pencil

    Je gaat een eenvoudig raadspelletje maken, waarbij de gebruiker een getal moet raden dat de computer 'in gedachten heeft'. Maak daartoe in Mu editor een nieuw bestand :file:`raad_het_getal.py` aan en kopieer onderstaande code erin.

    .. code-block:: python
        :caption: raad_het_getal.py
        :name: if_statements_opdracht_01
        :linenos:

        import random

        # Variabele getal_in_gedachten bevat een willekeurige integer tussen 0 en 5.
        getal_in_gedachten = random.randint(1, 4)

        print('Ik heb een getal onder de vijf in gedachten. Kun je het raden?')
        getal = int(input('Typ een getal onder de vijf: '))

    Op regel 1 wordt met :python:`import random` de Python random module geïmporteerd, die je in staat stelt om op regel 4 met de functie :python:`randint()` een willekeurig getal te genereren.
    
    Voeg onder deze code een :python:`if` statement toe waardoor

    * als de gebruiker het goed heeft geraden, de tekst ``Dat klopt, goed geraden!`` wordt geprint;
    * als de gebruiker het fout heeft, de tekst ``Helaas. Het goede getal was ..`` met op de puntjes het goede getal wordt geprint.

    .. dropdown:: Hint
        :color: secondary
        :icon: light-bulb

        Het :python:`if` statement heeft de volgende vorm:

        .. code-block:: python

            if ...:
                print('Dat klopt, goed geraden!')
            else:
                print('Helaas. Het goede getal was ' + str(getal_in_gedachten))

        Welke voorwaarde moet op de puntjes staan?   

.. dropdown:: Opdracht 02
    :color: secondary
    :icon: pencil

    Het raadspelletje van opdracht 01 wordt leuker als een speler meerdere keren kan raden. Om dat voor elkaar te krijgen, hebben we een while loop nodig. Pas je code als volgt aan:

    .. code-block:: python
        :caption: raad_het_getal.py
        :name: if_statements_opdracht_02
        :linenos:
        :emphasize-lines: 5,6,10-12

        import random

        # Variabele getal_in_gedachten bevat een willekeurige integer tussen 0 en 5.
        getal_in_gedachten = random.randint(1, 4)
        # Variabele geraden is een boolean die aangeeft of het getal is geraden
        geraden = False
        
        print('Ik heb een getal onder de vijf in gedachten. Kun je het raden?')

        while not geraden:
            getal = int(input('Typ een getal onder de vijf: '))
            if ...

    Op regel 10 zie je de start van de while loop :python:`while not geraden:`. Zolang de waarde van de variabele :python:`geraden` :python:`False` is, blijft deze while loop zich herhalen.

    Vul vanaf regel 12 het :python:`if` statement aan waardoor 

    * als de gebruiker het goed heeft geraden, de tekst ``Dat klopt, goed geraden!`` wordt geprint **en de while loop stopt**;
    * als de gebruiker het fout heeft, de tekst ``Helaas, dat is fout.`` wordt geprint.

.. dropdown:: Opdracht 03
    :color: secondary
    :icon: pencil

    Breid het raadspelletje van opdracht 02 uit zodat wordt getoond hoeveel beurten de gebruiker nodig had om het getal te raden. Voeg daartoe een variabele :python:`aantal_beurten` aan de code toe en geef deze de waarde 1. Bij elke herhaling van de :python:`while` loop moet :python:`aantal_beurten` met 1 worden opgehoogd. Wanneer de gebruiker het getal heeft geraden, moet worden geprint hoeveel beurten daarvoor nodig waren.

Elif
----

Je kunt een :python:`if` statement nog verder uitbreiden met het keyword :python:`elif`, dat staat voor 'else if'. In de onderstaande code zie je hoe dat werkt. Hierin is tevens de aanroep :python:`print("Hallo", name)` buiten het :python:`if` statement geplaatst (op regel 3) omdat we die begroeting voor elke naam willen tonen.

.. code-block:: python
    :linenos:
    :emphasize-lines: 3-9
    :caption: hello_if.py
    :name: hello_if_v05

    # Functie say_hello() toont een begroeting
    def say_hello(name):
        print("Hallo", name)
        if name == "Tony":
            print("Leuk je weer te zien.")
        elif name == "Tina":
            print("Hoe gaat het met je?")
        else:
            print("Aangenaam kennis te maken.")
        
    # Hoofdprogramma
    say_hello("Tabe")
    say_hello("Tess")
    say_hello("Tony")
    say_hello("Tina")

Op regel 4 checkt Python of de waarde van :python:`name` gelijk is aan :python:`"Tony"`. Zo ja, dan wordt regel 5 uitgevoerd. Zo nee, dan checkt Python in regel 6 of :python:`name` misschien de waarde :python:`"Tina"` bevat. Zo ja, dan wordt regel 7 uitgevoerd. Zo nee, dan zorgt regel 8 ervoor dat de code in regel 9 wordt uitgevoerd.

.. code-block:: text
    :caption: hello_if.py output
    :name: hello_if_v05_output

    Hallo Tabe
    Aangenaam kennis te maken.
    Hallo Tess
    Aangenaam kennis te maken.
    Hallo Tony
    Leuk je weer te zien.
    Hallo Tina
    Hoe gaat het met je?

.. dropdown:: Opdracht 04
    :color: secondary
    :icon: pencil

    Je gaat weer een raadspelletje maken, maar nu met een getal onder de 100. Maak daartoe in Mu editor een nieuw bestand :file:`raad_het_getal_2.py` aan en kopieer onderstaande code erin.

    .. code-block:: python
        :caption: raad_het_getal.py
        :name: if_statements_opdracht_04
        :linenos:

        import random

        # De variabele getal_in_gedachten bevat een willekeurige integer tussen 0 en 100.
        getal_in_gedachten = random.randint(1, 99)
        # Variabele geraden is een boolean die aangeeft of het getal is geraden
        geraden = False

        print('Ik heb een getal onder de honderd in gedachten. Kun je het raden?')

        while not geraden:
            getal = int(input('Typ een getal onder de honderd: '))
            if ...

    Vul vanaf regel 12 het :python:`if` statement aan waardoor 

    * als de gebruiker het goed heeft geraden, de tekst ``Dat klopt, goed geraden!`` wordt geprint en de while loop stopt;
    * als de gebruiker een te laag getal heeft geraden, de tekst ``Helaas, dat is te laag.`` wordt geprint.
    * als de gebruiker een te hoog getal heeft geraden, de tekst ``Helaas, dat is te hoog.`` wordt geprint.

.. dropdown:: Opdracht 05
    :color: secondary
    :icon: pencil

    Breid je code van opdracht 04 net als bij opdracht 03 weer uit met een :python:`aantal_beurten` variabele zodat wordt getoond hoeveel beurten de gebruiker nodig had om het getal te raden. 

And en or
---------

In een :python:`if` statement kun je gebruik maken van :python:`and` en :python:`or` om voorwaarden te combineren. Stel dat we zowel Tony als Tina willen begroeten met de zin 'Leuk je weer te zien.', dan zouden we de functie :python:`say_hello()` als volgt kunnen aanpassen (het hoofdprogramma blijft ongewijzigd):

.. code-block:: python
    :linenos:
    :caption: hello_if.py
    :name: hello_if_v06

    # Functie say_hello() toont een begroeting
    def say_hello(name):
        print("Hallo", name)
        if name == "Tony" or name == "Tina":
            print("Leuk je weer te zien.")
        else:
            print("Aangenaam kennis te maken.")

In regel 4 staat :python:`if name == "Tony" or name == "Tina":`. Het keyword :python:`or` betekent **of**. Hier staat dus: 'Als de waarde van :python:`name` gelijk is aan :python:`"Tony"` **of** als de waarde van :python:`name` gelijk is aan :python:`"Tina"`, doe dan het volgende.'

.. dropdown:: Vraag 01
    :color: secondary
    :icon: question

    Het keyword :python:`and` betekent **en**. Wat zou er gebeuren als je regel 4 wijzigt in :python:`if name == "Tony" and name == "Tina":`? Probeer het maar eens uit. Kun je het resultaat verklaren?

    .. dropdown:: Antwoord
        :color: secondary
        :icon: check-circle

        De waarde van :python:`name` kan niet tegelijkertijd zowel :python:`"Tony"` als :python:`"Tina"` zijn. Dus :python:`name == "Tony" and name == "Tina"` is altijd onwaar. Daardoor springt de code naar regel 6 en wordt elke naam begroet met :python:`"Aangenaam kennis te maken."`.

.. dropdown:: Opdracht 06
    :color: secondary
    :icon: pencil

    Je kent vast wel het spelletje *Steen, Papier, Schaar*. We gaan dit spel nu programmeren in Python. Maak een nieuw bestand :file:`rock_paper_scissors.py` aan en kopieer onderstaande code erin.

    .. code-block:: python
        :caption: rock_paper_scissors.py
        :name: if_statements_opdracht_06
        :linenos:

        import random

        print('*********************************************')
        print('* Welkom bij het spel Rock, Paper, Scissors *')
        print('*********************************************')
        print('Typ r, p, of s om rock, paper of scissors te kiezen')
        human = input('Uw keuze: ')

        computer = random.choice(['r', 'p', 's'])

        print('De computer koos ' + computer + ' en u koos ' + human + '.')

    In regels 3 t/m 7 wordt een welkomstboodschap geprint en krijgt de gebruiker de gelegenheid om ``r``, ``p``, of ``s`` te typen. In regel 9 gebruiken we de :python:`random.choice()` functie om de computer een willekeurige keuze uit deze drie letters te laten maken.

    Voeg aan de code een :python:`if` statement toe waarmee je vaststelt welke speler het spel heeft gewonnen. Gebruik de volgende structuur:

    .. code-block:: python

        if ... :
            # De speler wint
            print('U wint!')
        elif ... :
            # De computer wint
            print('De computer wint...')
        else:
            # Gelijkspel
            print('Gelijkspel.')

    Bedenk zelf welke voorwaarden op de puntjes moeten staan. De speler wint bijvoorbeeld als zij/hij steen koos en de computer schaar, maar ook als zij/hij papier koos en de computer steen. Gebruik :python:`and` en :python:`or` om voorwaarden te combineren. 

.. dropdown:: Opdracht 07
    :color: secondary
    :icon: pencil

    Deze opdracht volgt op opdracht 06. In regel 11 van :file:`rock_paper_scissors.py` staat:
    
    .. code-block:: python
        :linenos:
        :lineno-start: 11
        
        print('De computer koos ' + computer + ' en u koos ' + human + '.')

    De variabelen :python:`computer` en :python:`human` bevatten elk een letter :python:`r`, :python:`p` of :python:`s`.       De output van regel 11 zou dus bijvoorbeeld kunnen zijn:

    .. code-block::

        De computer koos r en u koos p.

    Dit ziet er niet zo mooi uit. Beter zou zijn:

    .. code-block::

        De computer koos steen en u koos papier.

    Vervang regel 11 door twee :python:`if` statements. Het eerste statement zorgt ervoor dat met een zin de keuze van de computer wordt getoond en het tweede doet dat voor de keuze van de speler. De output zou er dan bijvoorbeeld zo uit kunnen zien:

    .. code-block::

        De computer koos steen.
        U koos papier.

