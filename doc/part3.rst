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

...



  
To be continued...
------------------

