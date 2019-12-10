import random

# The size of the board in tiles
TILESW = 14
TILESH = 14
# The pixel size of the screen
WIDTH = TILESW * 40
HEIGHT = TILESH * 40

TITLE = 'Candy Crush'
last_dt = 0

cursor = Actor('selected', topleft=(0,0))

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

def cursor_tile_pos():
    return (int(cursor.x // 40)-1, int(cursor.y // 40))

def drop_tiles(x,y):
    # Loop backwards through the rows from x,y to the top
    for row in range(y,0,-1):
        # Copy the tile above down
        board[row][x] = board[row-1][x]
    # Finally blank the tile at the top
    board[0][x] = None

def check_tiles_for_matches():
    for y in range(TILESH):
        for x in range(TILESW-1):
            if board[y][x] == board[y][x+1]:
                board[y][x] = None
                board[y][x+1] = None

def check_tiles_for_gaps():
    # Work from the bottom up
    for y in range(TILESH-1,-1,-1):
        for x in range(TILESW):
            if board[y][x] is None:
                drop_tiles(x,y)

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

def every_second():
    check_tiles_for_matches()
    check_tiles_for_gaps()

clock.schedule_interval(every_second, 1.0)