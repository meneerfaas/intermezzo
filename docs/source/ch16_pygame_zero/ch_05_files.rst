.. role:: python(code)
   :language: python

.. |br| raw:: html

   <br/>

Bestanden lezen
====================

In de huidige versie van ons Alchemy spel zijn de elementen en de recepten *hardcoded* in de programmacode. De elementen in de dictionary :python:`elements` en de recepten in de string :python:`recipes_txt`:

.. code-block:: python

   elements = {
      'fire': 'vuur',
      'water': 'water',
      'wind': 'wind',
      'earth': 'aarde',
      'steam': 'stoom',
      'wave': 'golf',
      'plant': 'plant',
      'smoke': 'rook',
      'lava': 'lava',
      'dust': 'stof'
   }

   recipes_txt = '''water
   fire
   wind
   earth
   -
   water+fire=steam
   water+wind=wave
   water+earth=plant
   fire+wind=smoke
   fire+earth=lava
   wind+earth=dust'''

Dit betekent dat we de code moeten aanpassen als we een nieuw element of recept willen toevoegen. Dit is niet erg handig, vooral als we veel elementen en recepten hebben. Het is beter om deze gegevens in een apart bestand te zetten, zodat we ze gemakkelijk kunnen aanpassen zonder de code te veranderen. 