import random


# The size of the board in tiles
TILESW = 10
TILESH = 4
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