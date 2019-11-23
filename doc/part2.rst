.. _part2:

Part 2
======

Swap those tiles
----------------

Let's add code to swap two tiles. We first need to add some code to the :code:`on_key_up` function to run when the user presses the space key:

.. code:: python

   # You already have these two lines
   if key == keys.DOWN:
      cursor.y += 40

   # Add these three lines
   if key == keys.SPACE:
      x, y = cursor_tile_pos()
      board[y][x], board[y][x+1] = board[y][x+1], board[y][x]

Here's what this code does:

#. if they key pressed is space...
#. get the co-ordinates of the tile that the cursor is over
#. swap the tiles at :code:`(x,y)` and :code:`(x+1,y)`

Did you notice something wrong with that code? Press run to see. That's right, we've not written the code for :code:`cursor_tile_pos` yet. Let's add that now, above the :code:`draw` function, add this code...

.. code:: python

  def cursor_tile_pos():
    return (int(cursor.x // 40)-1, int(cursor.y // 40))

Here we are tranlating the pixel position of the cursor into a tile co-ordinate.

Time for testing
----------------

Testing is very important when developing software.

Almost every piece of code that every developer writes (yes even professional ones!) has bugs and we need to find them. Otherwise our players will find them and get frustrated -- after all they can't fix the bugs unless they are programmers too.

* Spend a bit of time playing and testing the game and see if you can find some bugs. 

Hint: there's a pretty big one that generates the error :code:`IndexError: list index out of range`

To be continued...
------------------
