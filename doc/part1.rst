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
          tile = 1
          screen.blit(str(tile), (x * 40, 0))

- Press **Play**

OK, now we have 10 tiles across the screen. That's what the :code:`for x in range(10)` does, it repeats the code inside 10 times, setting :code:`x` to each number between 0 and 9 (most programming languages start counting at 0)! We then use the :code:`x` to calculate the tile's x position on the screen, as :code:`x * 40` since each tile is 40 pixels wide.

Let's mix up the tiles a bit, change the line :code:`tile = 1` to the following:

.. code:: python
          
   tile = random.randint(1,8)

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

Now you can move the cursor, but did you notice a weird bug when you press play?

The background changes each time we move! Why is that? Have a look at the draw code and have a think...

Fixing the background
---------------------

Did you figure it out? That's right, we just set each tile to a random number when we draw the board, and it's never going to be the same each time, so the board keeps changing. Let's fix that...

We need to remember what each tile is, and then use this record to draw the same board each time. Let's use a two dimensional list to do this. Add this just above your :code:`draw` function:

.. code:: python

    board = []
    for row in range(14):
        # Make a list of 10 random tiles
        tiles = [random.randint(1,8) for x in range(10)]
        board.append(tiles)

Now change your :code:`draw` function so that it uses this list:

.. code:: python

    def draw():
        for y in range(14):
            for x in range(10):
                tile = board[y][x]
                screen.blit(str(tile), (x * 40, y * 40))
        cursor.draw()

So, to recap: we create a new two dimensional list called :code:`board`, and we add lists of tiles, one for each row. We then use this when drawing the board, looking up the correct tile given :code:`x` and :code:`y`.

There's a lot of code there! Take a look carefully and see if you spot some things you've not used before... there's two big new things here: *lists* and *list comprehensions*. Let's take a little diversion to explore them...

First let's open a new Python tab and switch to a REPL (pronounced repple) , this is a place we can type in Python code and see the results immediately - useful for checking out language features. So:

* Click **New**
* Click **Mode** and choose Python 3
* Click **REPL**, you should now see a window at the bottom of the screen with a prompt :code:`In [0]`


Lists
------

Lists are a nice data type that lets of store a sequence of values (in our game a sequence of tiles) and retrieve them later.

To try them out type each line of code here, one at a time, in your REPL. You don't need to type the comments (starting with a hash :code:`#`) if you don't want to.

.. code:: python

   # Create an list of numbers 6-1
   a = [6,5,4,3,2,1]
   # Print the list
   a
   # Print first then last item of the list
   a[0]
   a[5]
  
So as you can see, you can easily make an list, then print it out to the REPL. We can also add to the list:

.. code:: python

   a.append(0)
   a.append(-1)
   # Print it out
   a

You can store anything in an list, including other lists...

.. code:: python

   # Start with an empty list
   b = []
   # Add list `a` from before
   b.append(a)
   # A new list of strings
   c = ['the', 'quick', 'brown', 'fox']
   
   b.append(c)
   b.append(sorted(c))

   # Print out b
   b
   
   

List Comprehensions
-------------------

To be completed...
