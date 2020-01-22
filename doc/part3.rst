.. _part3:

Part 3
======

Keep the cursor on screen
-------------------------

So we need to check the cursor's current position and only allow it to move if it will remain onscreen after the move. Change your :code:`on_key_up` function as follows, moving the :code:`x, y` assignment to the first line of the function and adding clauses to each :code:`if` statement...

.. code:: python

   def on_key_up(key):
       x, y = cursor_tile_pos()
       if key == keys.LEFT and x > 0:
          cursor.x -= 40
       if key == keys.RIGHT and x < 8:
          cursor.x += 40
       if key == keys.UP and y > 0:
          cursor.y -= 40
       if key == keys.DOWN and y < 13:
          cursor.y += 40
       if key == keys.SPACE:
          board[y][x], board[y][x+1] = board[y][x+1], board[y][x]          

* Press **Run** and Test that this works OK.

Have you noticed that we have some repeated numbers in our code now? We are using the numbers 8 and 13 above, which relate to the board size, as used in the loops to set up the board.

This means if we change the board size we have to remember to find all the other numbers that relate to this and change those too, that's boring and, more importantly, likely to cause bugs. 

* Try changing the board size and screen size to see this limitation in our code, you'll need to change :code:`HEIGHT` and the two loop ranges as follows (the elipses ... represent existing code):

.. code:: python

   HEIGHT = 720

   ...
   for row in range(18):
   ...

   def draw():
     for y in range(18):
         ...

Now try moving the cursor to the bottom.

*Can you see the relationship between these values?*


D.R.Y.
------

Remember Don't Repeat Yourself? Well let's fix the repeated numbers.

We have two variables, in fact because these don't change during the game we call them *constants*:

1. the screen width in tiles, 10
2. the screen height in tiles, 14

And we have a bunch of other constants or calculations that relate to these:

1. the screen width in pixels is 10 * 40 = 400
2. the screen height in pixels is 14 * 40 = 560
3. the maximum x pos of the cursor is 10 - 2 (as it is two tiles wide
4. the maximum y pos of the cursor is 14 - 1.

Here's the code with the numbers replaced with constants or calculations using the constants:

.. code:: python

   import random

   # The size of the board in tiles
   TILESW = 10
   TILESH = 14
   # The pixel size of the screen
   WIDTH = TILESW * 40
   HEIGHT = TILESH * 40

   TITLE = 'Candy Crush'

   cursor = Actor('selected', topleft=(0,0))

   board = []
   for row in range(TILESH):
       # Make a list of 10 random tiles
       tiles = [random.randint(1,8) for _ in range(TILESW)]
       board.append(tiles)

   def draw():
       for y in range(TILESH):
           for x in range(TILESW):
               tile = board[y][x]
               screen.blit(str(tile), (x * 40, y * 40))
       cursor.draw()

   def cursor_tile_pos():
       return (int(cursor.x // 40)-1, int(cursor.y // 40))

   def on_key_up(key):
       x, y = cursor_tile_pos()
       if key == keys.LEFT and x > 0:
          cursor.x -= 40
       if key == keys.RIGHT and x < TILESW-2:
          cursor.x += 40
       if key == keys.UP and y > 0:
          cursor.y -= 40
       if key == keys.DOWN and y < TILESH-1:
          cursor.y += 40
       if key == keys.SPACE:
          board[y][x], board[y][x+1] = board[y][x+1], board[y][x]

To see how this works better, go ahead and try different values for :code:`TILESW` and :code:`TILESH`. The game should just work with no errors, although probably not for very small or very large values. 


Matching Tiles
--------------

When two tiles match we want to remove them from the screen and then move the tiles above down, we can think of this as two new functions: :code:`check_matches` and :code:`drop_tiles`.

There are a few decisions to make:

1. when should we check for matches? 
2. should we check the whole board or just where the cursor is?

Let's check whenever the user presses SPACE as that could cause a match. As we did before, let's just put in the function call then write the code inside:

Add the last line here *inside* the :code:`if` statement:

.. code:: python

   def on_key_up(key):
       ...
       if key == keys.SPACE:
          board[y][x], board[y][x+1] = board[y][x+1], board[y][x]
          check_matches()
          
Running the program should report an error whenever you press SPACE. Go ahead and confirm this - it means we have the function in the correct place. 

Let's check all the tiles on the board for matches, this will be simpler and if it proves to be too slow we can optimise it later.

.. code:: python

   def check_matches():
       for y in range(TILESH): 
           for x in range(TILESW-1):
               if board[y][x] == board[y][x+1]:
                   board[y][x] = None
                   board[y][x+1] = None

That loop code should look familiar, it's the same pattern as drawing the board. This time we are looping through every tile and checking to see if each is the same as its neighbour. Did you see that we use a double equals sign to check that two things are the same :code:`==`, this is different to assignment with one equals sign.

If we spot a duplicate we remove the two tiles and replace them with a blank, a :code:`None` in python.

OK, now let's test and see what errors we get...

First we see this one:

.. code:: python

   File "candy3.py", line 27, in draw
   ...
   KeyError: "No image found like 'None'. Are you sure the image exists?"

*OK, so our drawing code assumes that there's a tile at every position and just draws it, let's fix that.*

Go to line 27 in your draw function (your line number might be a bit different, do check your error message) and add an :code:`if` statement to check, like so:

.. code:: python

   ...
   for x in range(TILESW):
       tile = board[y][x]
       if tile:
           screen.blit(str(tile), (x * 40, y * 40))

Run again and you'll notice no errors, but the tiles don't leave the screen. We need to add a :code:`screen.clear()` to the start of the draw function:

.. code:: python

   def draw():
       screen.clear()
       for y in range(TILESH):

OK, that's better, but there is one more weird thing: on the first press of SPACE a lot of holes open up on the board because we didn't check for matches when we generated the board in the first place.

Periodic functions
------------------

We saw in the last section that no matches are found until we press SPACE, but actually there could be matches at the start of the game. Instead of running :code:`check_matches` when we press SPACE let's run it every second.

Remove the call to this function from :code:`on_key_up` and add the following to the end of your code:

.. code:: python

   def every_second():
       check_matches()

   clock.schedule_interval(every_second, 1.0)

*Now run and test your code. Better?*


Filling in the gaps
-------------------

So now we have gaps we need to drop tiles into them. This function looks a bit similar to the function you just wrote: :code:`check_matches`.

.. code:: python
          
   def check_gaps():
       # Work from the bottom up
       for y in range(TILESH-1,-1,-1):
           for x in range(TILESW):
               if board[y][x] is None:
                   drop_tiles(x,y)

And that function needs this one to actually drop the tiles:

.. code:: python

   def drop_tiles(x,y):
       # Loop backwards through the rows from x,y to the top
       for row in range(y,0,-1):
           # Copy the tile above down
           board[row][x] = board[row-1][x]
       # Finally blank the tile at the top
       board[0][x] = None          

When do we run this code? Let's add it to our :code:`every_second` function:

.. code:: python

   def every_second():
       check_matches()
       check_gaps()

*That's it, we should have a working Candy Crush Clone!* 
       
What's next?
------------

Maybe we should add new tiles as we clear the screen?

Read on to :ref:`part4`.

