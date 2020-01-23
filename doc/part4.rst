.. _part4:

.. To do
   Explain why we use `global`

Part 4
======

In Part 4 of Candy Crush we will add these features:

* add new tiles to fill the gaps
* make it a match 3 game, or match squares
* add a score
* add fruits that you need to get to the bottom of the screen for bonus points
* add bombs that help you clear the screen.

One thing: now that we are on part 4 and you have a bit of practice
thinking like a developer we are going to ask you to start creating
your own algorithms and Python code. Don't worry, we've supplied some
solutions at the end.


Adding new tiles
----------------

The screen starts to look quite empty as you match and remove
tiles. If our game objective is to clear the screen then that's OK,
but let's keep the player busy by adding tiles as gaps appear at the
top of the screen.

First have a think about a good algorithm to achieve this. You can do
this on a piece of paper or in the code with comments, let's try
this...

Add this method and comments:

.. code:: python

   def new_tiles():
       # Put the steps of your algorithm here.
       # Go on, have a think first... before you scroll down
       # and see a solution.
       #
       # What are the steps we need to do to add new tiles?

...

...

...
       
Here's one algorithm that might work:

.. code:: python

   def new_tiles():
       # Check for gaps starting at the top of the screen
       # Can we just check the first row?
       # Place a new tile into any gaps we find
       # The existing code will make them fall down the screen.

How did this compare with yours?

Now can you use what you've already practiced to turn your algorithm
into Python code?


Make it a match 3 game
----------------------

Right now you only have to match 2 tiles to remove them from the
screen. This is too easy. Let's make it so that you have to match 3 tiles.

Have a look at the matching code and see if you can work out how to achieve this.

You may well get this error on your first attempt: ::

  IndexError: list index out of range

If you do, then take a look at the line above the matching code that reads: ::

  for x in range(TILESW-1):

Why do you think we put in :code:`TILESW-1` and not just
:code:`TILESW` ? Could this help you fix the error?


Matching squares
................

Instead of matching a row of 3 tiles we could get the player to match a set
of 2x2 tiles instead. Once you've worked out how to move to a match 3 game then
this change shouldn't be too hard to achieve. 

As with the change to match 3 above, you might see that
:code:`IndexError` error but on the line :code:`for y ...`. The fix is very similar. 
  

Adding a score
--------------

Let's add a score so that the player gets some sense of achievement from playing the game.

We'll need to add a variable to the start of the game, so add the
following line near the top of your code:

.. code:: python

  score = 0

Now we need to draw the score, where shall we place it on the screen?
Shall we place it over the top of tiles or make space for it on a
blank row with no tiles? You decide.

In order to display text you'll need to use the function
:code:`screen.draw.text` like this:

.. code:: python

   screen.draw.text("Score: %s" % score, bottomleft=(0, HEIGHT), fontsize=60)

Now on to changing the score... Inside any function that changes the
score we need to add this line at the top of the function:

.. code:: python

  global score

Now you get to decide when and how to change the score. Clearly we
should increase it when the user gets a match, but by how much? We
could reduce it when they move, maybe?

What's `global` do?
...................

You might not have seen :code:`global` before. It tells Python that
when we use :code:`score` in this function we want to use the one
defined outside the function (in global scope), not one private to
this function's scope.

By default in Python (and many other programming languages) if you
create a variable in a function then it is assumed that this is
private to that function. This is a good thing as it stops code in a
function messing up code outside the function.

Here's an example (create a new Python script if you want to see it in
action):

.. code:: python

    def fac(i):
        f = 1
        for a in range(i, 0, -1):
            f = f * a
        return f

    a = 5
    print(fac(a))
    a = a + 1
    print(fac(a))

    
Other score ideas
.................

If you've followed the match 3 and match square code we could support
both and give a higher score for matching squares? You are the game
creator, so you decide!


Time for some fruit
-------------------

*Coming soon...*


       
----

Solutions
---------

Code for adding new tiles
.........................

.. code:: python

   NEW_TILE_PROB = 0.1 # 10% chance of adding a new tile each time 
   
   def add_new_tiles():
       for x in range(TILESW):
           if board[0][x] is None and random.random() < NEW_TILE_PROB:
               board[0][x] = random.randint(1,8)


Code for match 3 game
.....................

Here is the new :code:`check_matches` function with changes to make it a match 3 game: 

.. code:: python

    def check_matches():
        for y in range(TILESH):
            for x in range(TILESW-1):
                if board[y][x] == board[y][x+1] == board[y][x+2]:
                    board[y][x] = None
                    board[y][x+1] = None
                    board[y][x+2] = None
          

Code for match squares
......................

.. code:: python

    def check_matches():
        for y in range(TILESH-1):
            for x in range(TILESW-1):
                if board[y][x] == board[y][x+1] == board[y+1][x] == board[y+1][x+1]:
                    board[y][x] = None
                    board[y][x+1] = None
                    board[y+1][x] = None
                    board[y+1][x+1] = None          

                    
What's next?
------------

Well done! You've made it to the end of the Candy Crush Tutorial! You
are now thinking like a programmer and have many of the skills
required to create your own games.

All you need to do now is come up with some ideas to try out...
