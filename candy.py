import random

WIDTH = 400
HEIGHT = 560
TITLE = 'Candy Crush'

cursor = Actor('selected', topleft=(0,0))

board = []
for row in range(14):
    # Make a list of 10 random tiles
    tiles = [random.randint(1,8) for x in range(10)]
    board.append(tiles)

def draw():
     for y in range(14):
        for x in range(10):
            tile = board[y][x]
            screen.blit(str(tile), (x * 40, y * 40))
     cursor.draw()

def on_key_up(key):
    if key == keys.LEFT:
        cursor.x -= 40
    if key == keys.RIGHT:
        cursor.x += 40
    if key == keys.UP:
        cursor.y -= 40
    if key == keys.DOWN:
        cursor.y += 40