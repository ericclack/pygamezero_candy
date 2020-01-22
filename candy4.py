import random

# The size of the board in tiles
TILESW = 20
TILESH = 14
# The pixel size of the screen
WIDTH = TILESW * 40
HEIGHT = (TILESH+1) * 40

# How likely is a new tile each tick?
NEW_TILE_PROB = 0.9

TITLE = 'Candy Crush'
last_dt = 0

cursor = Actor('selected', topleft=(0,0))
score = 0

board = []
for row in range(TILESH):
    # Make a list of 10 random tiles
    tiles = [random.randint(1,8) for _ in range(TILESW)]
    board.append(tiles)

def draw():
    screen.clear()
    for y in range(TILESH):
        for x in range(TILESW):
            tile = board[y][x]
            if tile:
                screen.blit(str(tile), (x * 40, y * 40))
    cursor.draw()
    screen.draw.text("Score: %s" % score, bottomleft=(0,HEIGHT), fontsize=60)

def cursor_tile_pos():
    return (int(cursor.x // 40)-1, int(cursor.y // 40))

def drop_tiles(x,y):
    # Loop backwards through the rows from x,y to the top
    for row in range(y,0,-1):
        # Copy the tile above down
        board[row][x] = board[row-1][x]
    # Finally blank the tile at the top
    board[0][x] = None

def check_matches():
    global score
    for y in range(TILESH-1):
        for x in range(TILESW-1):
            if board[y][x] == board[y][x+1] == board[y+1][x] == board[y+1][x+1]:
                board[y][x] = None
                board[y][x+1] = None
                board[y+1][x] = None
                board[y+1][x+1] = None
                score += 50

def check_gaps():
    # Work from the bottom up
    for y in range(TILESH-1,-1,-1):
        for x in range(TILESW):
            if board[y][x] is None:
                drop_tiles(x,y)

def on_key_up(key):
    global score
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
        score += -1
        board[y][x], board[y][x+1] = board[y][x+1], board[y][x]

def add_new_tiles():
    for x in range(TILESW):
        if board[0][x] is None and random.random() < NEW_TILE_PROB:
            board[0][x] = random.randint(1,8)

def every_second():
    check_matches()
    check_gaps()
    add_new_tiles()

clock.schedule_interval(every_second, 0.25)