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
       screen.blit('1.png', (0, 0))
       
- Press **Play**

OK, one tile. We need more, in fact we need to fill the screen. Change your :code:`draw` function to the following:

.. code:: python

   def draw():
       screen.blit('1.png', (0, 0))
       screen.blit('2.png', (40, 0))
       screen.blit('3.png', (80, 0))
       screen.blit('4.png', (120, 0))

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

If you look carefully you'll see that the cursor is not properly on the screen. Let's fix that using a nice feature on the actor object. Change your :code:`cursor` definition to this:

.. code:: python

   cursor = Actor('selected', topleft=(0,0))

Using :code:`topleft` we can position the cursor so that it's exactly in the top corner of the screen.

Moving the cursor
-----------------

Let's move the cursor when the player presses the arrow keys.

Add the following new function at the end of your program:

.. code:: python

    def on_key_up(key):
        if key == keys.LEFT:
            cursor.x -= 40
        if key == keys.RIGHT:
            cursor.x += 40
        if key == keys.UP:
            cursor.y -= 40
        if key == keys.DOWN:
            cursor.y += 40

Now you can move the cursor, but did you notice a quite weird bug when you press play?

The background changes each time we move! Why is that? Have a look at the draw code and have a think...

Fixing the background
---------------------

Did you figure it out? That's right, we just set each tile to a random number when we draw the board, and it's never going to be the same each time, so the board keeps changing. Let's fix that...

We need to remember what each tile is, and then use this record to draw the same board each time. Let's use a two dimensional array to do this. Add this just above your :code:`draw` function:

.. code:: python

    board = []
    for row in range(14):
        # Make a list of 10 random tiles
        tiles = [random.randint(1,8) for _ in range(10)]
        board.append(tiles)

Now change your :code:`draw` function so that it uses this array:

.. code:: python

    def draw():
        for y in range(14):
            for x in range(10):
                tile = board[y][x]
                screen.blit(str(tile), (x * 40, y * 40))
        cursor.draw()

So, to recap: we create a new two dimensional array called :code:`board`, and we add lists of tiles, one for each row. We then use this when drawing the board, looking up the correct tile given :code:`x` and :code:`y`.

