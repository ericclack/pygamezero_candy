.. _part1:

Part 1
======

Getting Started
---------------

- Press the **New** button in Mu to open a new file and enter the following lines:

.. code:: python

    WIDTH = 400
    HEIGHT = 560
    TITLE = 'Candy Crush'

- Press **Save** and save the file as candy.py

- press **Play** to see what this code does.

You should see an new empty window appear.


Let's add some tiles
--------------------
- Add these lines to the end of your program. Make sure you *indent* the second line so that it's inside the `draw` function, in other words, press the TAB key before typing it. 
  
.. code:: python

   def draw():
       screen.blit('tile1.png', (0, 0))
       
- Press **Play**

OK, one tile. We need more, in fact we need to fill the screen. Change your :code:`draw` function to the following:

.. code:: python

   def draw():
       screen.blit('tile1.png', (0, 0))
       screen.blit('tile2.png', (40, 0))
       screen.blit('tile3.png', (80, 0))
       screen.blit('tile4.png', (120, 0))

- Press **Play**       

Now 4 tiles. You are probably wondering: how much typing am I going to have to do to fill up the screen?! Fear not, let's use some loops to save typing.

Change your :code:`draw` function to the following:

.. code:: python

  def draw():
      for x in range(10):
          tile = random.randint(1,8)
          screen.blit(str(tile), (x * 40, 0))

- Press **Play**

Oops, we get an error. Whenever you see an error, look at the last line first as this has the error message.

  :code:`NameError: name 'random' is not defined`

This is Python's way of telling us that we need to import the :code:`random` library. So add this as the first line of your program:

.. code:: python

   import random

- Now press **Run** again

Cool! We have a row of tiles. Run the program again and you'll see a different set of tiles -- that's what :code:`random.randint` does for us, it picks a random number between 1 and 8 each time. 

So how do we create multiple rows? Well let's put our loop inside a loop... you only need to add one line (the :code:`for y...`) and then indent the following three lines:

.. code:: python

  def draw():
      for y in range(14):
          for x in range(10):
              tile = random.randint(1,8)
              screen.blit(str(tile), (x * 40, y * 40))

              
Adding our cursor
-----------------

To play Candy Crush the player moves around a cursor, which highlights two tiles. The player can then swap the tiles by pressing space.

Let's use an :code:`Actor` to represent the cursor. Add this code above your :code:`draw` function:

.. code:: python

   cursor = Actor('selected', (0,0))

Then add this code to draw the cursor right at the end of your :code:`draw` function, it needs to line up exactly with the :code:`f` of the first :code:`for` loop:

.. code:: python

   draw():
      for y in range(14):
          for x in range(10):
              tile = random.randint(1,8)
              screen.blit(str(tile), (x * 40, y * 40))
      cursor.draw()

      
