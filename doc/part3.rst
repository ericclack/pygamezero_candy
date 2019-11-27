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

It's not obvious but we have some repetition in our code now. We are using the numbers 8 and 13 above, which relate to the board size, as used in the loops to set up the board.

* Try changing the board size and screen size to see this limitation in our code, e.g.:

.. code:: python

   HEIGHT = 720

   ...
   for row in range(18):
   ...

   def draw():
     for y in range(18):

Now try moving the cursor to the bottom.

*Can you see the relationship between these values?*



  
To be continued...
------------------

