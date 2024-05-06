.. role:: python(code)
   :language: python

.. |br| raw:: html

   <br/>

Pygame Zero
===========

Voor het maken van een game in Mu editor, is het nodig dat je Mu in de Pygame Zero stand zet. Dat gaat als volgt:

1. Klik op de :guilabel:`Mode` knop.
   
   .. image:: images/mu_mode_button.png

2. Selecteer Pygame Zero en klik op Ok.

   .. image:: images/mu_mode.png

Als je dit goed hebt gedaan, staat nu rechtsonder in de statusbalk van Mu editor *Pygame Zero*.

.. figure:: images/mu_pygame_zero_mode.png

Je ziet tevens dat de knoppenbalk een beetje is veranderd. Bijvoorbeeld in plaats van :guilabel:`Run` vind je nu een :guilabel:`Play` knop.

.. _mappen-structuur-maken:

Mappenstructuur
---------------

Bij het programmeren van een game gebruik je vaak veel bestanden: afbeeldingen, geluiden, lettertypes etcetera. Om te voorkomen dat je na enige tijd door de bomen het bos niet meer ziet, is het belangrijk dat je werkt met een goede mappenstructuur. Die structuur ga je nu maken.

.. figure:: images/folder_structure_goal.png

Als je al weet hoe je met de Windows Verkenner nieuwe mappen maakt en hoe je bestanden verplaatst, open dan de korte uitleg hieronder. Als je meer hulp nodig hebt, open dan de uitgebreide uitleg.

.. dropdown:: Mappenstructuur korte uitleg.
   :color: info
   :icon: info

   Maak in je :file:`Documenten` map een map :file:`python projects` aan en daarin weer twee mappen: :file:`turtle exercises` en :file:`games`. Verplaats de eventuele Python bestanden uit de voorgaande lessen die zich nu in je :file:`Documenten` map bevinden naar de map :file:`turtle exercises`.

   .. image:: images/folder_structure_00.png

.. dropdown:: Mappenstructuur uitgebreide uitleg.
   :color: info
   :icon: info

   1. Open een Windows Verkenner en ga daarin naar je :file:`Documenten` map. Waarschijnlijk staan hier verschillende Python bestanden in, die je tijdens de vorige lessen hebt aangemaakt.

      .. image:: images/folder_structure_01.png

   2. Selecteer in het lint bovenin de verkenner het :guilabel:`Start` tabblad (in het Engels :guilabel:`Home`). Je vindt daarin een knop waarmee je een nieuwe map kunt aanmaken. Klik op die knop.

      .. image:: images/folder_structure_02.png

   3. Noem de nieuwe map :file:`python projects`.

      .. image:: images/folder_structure_03.png

   4. Dubbelklik op de zojuist gemaakte map om hem te openen. Je kunt in de adresbalk van de verkenner zien dat je je nu in de map :file:`python projects` bevindt. 

      .. image:: images/folder_structure_04.png

   5. Maak in de map :file:`python projects` twee nieuwe mappen aan met de namen :file:`turtle exercises` en :file:`games`. Je kunt dit op dezelfde manier doen als in stap 2, maar als je avontuurlijk bent, kun je ook de toetscombinatie :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`N` gebruiken om een nieuwe map te maken.

      .. image:: images/folder_structure_05.png

   6. Ga terug naar je :file:`Documenten` map (door in de adresbalk of in het linker navigatiepaneel op :guilabel:`Documenten` te klikken). Klap vervolgens in het navigatiepaneel aan de linkerkant :file:`Deze computer` (Engels: :file:`This PC`) uit, vervolgens je :file:`Documenten` map en ook de map :file:`python projects` die eronder zit. 

      .. image:: images/folder_structure_06.png

   7. Selecteer nu alle Python bestanden door er met de muis 'een rechthoek overheen te slepen'. 

      .. image:: images/folder_structure_07.png

   8. Verplaats de geselecteerde Python bestanden door ze naar de map :file:`turtle exercises` in het navigatiepaneel aan de linkerkant te slepen.

      .. image:: images/folder_structure_08.png

   9. Nu is je :file:`Documenten` map mooi opgeschoond, en je oude turtle oefeningen staan handig bij elkaar in een map.

      .. image:: images/folder_structure_09.png

      De :file:`games` map ga je uiteraard gebruiken om straks je eerste game in op te slaan.

Vensterafmetingen
-----------------

Maak in Mu editor een nieuwe bestand aan met de :guilabel:`New` knop. Voordat je er code in gaat typen, sla je het bestand op in wederom een nieuwe map. Doe dat op de volgende manier:

1. Klik op :guilabel:`Save`. Navigeer naar je nieuwe :file:`games` map en klik daarna op de knop :guilabel:`Nieuwe map` (Engels: :guilabel:`New folder`).

   .. image:: images/save_file_01.png

2. Noem de nieuwe map :file:`alien`.

   .. image:: images/save_file_02.png

3. Dubbelklik op de map :file:`alien` om hem te openen. Sla je bestand vervolgens op onder de naam :file:`alien.py`.

   .. image:: images/save_file_03.png

En nu is het tijd voor de eerste code. Typ het volgende in je bestand. Niet kopiëren en plakken, want het is belangrijk dat je deze code (letterlijk) in de vingers krijgt voor later. Let op het verschil tussen hoofdletters en kleine letters.

.. code-block:: python
   :class: no-copybutton
   :linenos:
   :caption: alien.py
   :name: alien_v01

   # Vensterafmetingen
   WIDTH = 600
   HEIGHT = 400

Klik op :guilabel:`Play` om deze code te runnen. Er verschijnt een venster:

.. image:: images/game_window.png

Waarschijnlijk begrijp je al wat de woorden :python:`WIDTH` en :python:`HEIGHT` betekenen. Zo niet, verander dan iets aan de getallen en run de code opnieuw om het effect ervan te zien.

Wellicht lijkt het alsof je veel werk hebt moeten verzetten om alleen maar een zwart venster op het scherm te toveren, maar van de mappenstructuur die je in dit hoofdstuk hebt gemaakt, ga je nog veel plezier hebben. En in het volgende hoofdstuk wordt de invulling van het venster uiteraard een stuk interessanter.