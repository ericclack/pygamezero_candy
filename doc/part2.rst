.. _part2:

Part 2
======

Swap those tiles
----------------

Now it's time to add the code to swap the two tiles under the cursor. We first need to add some code to the :code:`on_key_up` function to run when the user presses the space key. Add the last 3 lines below to your function:

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

        # Add these three lines...
        if key == keys.SPACE:
            x, y = cursor_tile_pos()
            board[y][x], board[y][x+1] = board[y][x+1], board[y][x]

Here's what this code does:

#. if the key pressed is SPACE...
#. get the co-ordinates of the tile that the cursor is over and store in :code:`x` and :code:`y` variables
#. swap the tiles at co-ordinates :code:`(x,y)` and :code:`(x+1,y)`

Did you notice something wrong with that code? Press run to see. That's right, we've not written the code for :code:`cursor_tile_pos` yet. Let's add that now, above the :code:`draw` function, add this code...

.. code:: python

  def cursor_tile_pos():
    return (int(cursor.x // 40)-1, int(cursor.y // 40))

This function translates the pixel position of the cursor into a tile co-ordinate. The tiles are 40 pixels wide, which explains the number 40 in the code. :code:`//` means divide with integers, as we don't want decimals in the result.

*You might be wondering: why do we bother creating a new function when we could just put this code into our `on_key_up` function?*

Well two reasons: firstly creating the function makes our intentions clear, when we read the code we know that we are working out the cursor tile position; secondly we might need to do this in other places and we can re-use this function whenever we need to.

These are two really important things that professional programmers do: **make your intetions clear** and **don't repeat yourself (DRY)**. Another way of thinking about DRY is **be lazy**, avoid any boring, repetitive work! (If only all of life was like that!)

Time for testing
----------------

Testing is very important when developing software.

Almost every piece of code that every developer writes (yes even professional ones!) has bugs and we need to find them. Otherwise our players will find them and get frustrated -- after all they can't fix the bugs unless they are programmers too.

* Spend a bit of time playing and testing the game and see if you can find some bugs. Make a list on a piece of paper (or in a document on your computer) of all the ones you find. 

Hint: there's a pretty big one that generates the error :code:`IndexError: list index out of range`

Looking in the error message you should also be able to see the line number where this error is caused in your program. Take a look at that line and see if you can work out what is going on. Talk to a mentor if you are not sure. 

Debugging
---------

Testing is only half the story. Once we have a list of errors we need to work out the cause of each error and figure out the best way of fixing each one. So let's do this...

*You could just skip this section and look at the fixed code in the next part of this tutorial but that would be cheating!*

That's OK with me, but you will learn a lot more coding skills by working through the debugging first - and if you become a programmer later in life these skills will be super useful.

*So before you read further, try to make a good list of bugs (no peaking at the list below!)*

...

...

...

...

Here's my list of bugs -- how does it compare to yours?

1. The cursor can go off the screen: off the top or left hand side there's no crash, but the wrong tiles are affected by space.
2. Pressing space when the cursor is off the right and bottom causes a crash: :code:`IndexError: list index out of range`
3. Nothing happens if tiles are matched after a swap
4. Tiles that match on start up just stay on the screen.

What about the causes?

* 1 & 2 are caused by the array indexes (x and y) being out of range, in other words: less than zero, or greater than the size of the array
* 3 & 4 are caused because we're not written the code yet.

What about fixes?

* For 1 & 2: We could check the cursor position and not allow a move if it would result in the cursor moving off the screen.
* For 3 & 4: We need to write the code!

Read on to :ref:`part3`.

