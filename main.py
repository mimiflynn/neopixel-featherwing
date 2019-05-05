import board
import neopixel
import time

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (80, 200, 175)
WHITE = (255, 255, 255)

colors = [RED, YELLOW, GREEN,
          CYAN, PURPLE, BLUE, LIGHT_BLUE, WHITE]

# NeoPixel setup
pixels = neopixel.NeoPixel(board.D6, 32, brightness=.01)

print('hello world')

while True:
    for x in range(8):
        for i in range(4):    
            col = x
            d = i * 8
            e = d + col
            pixels[e] = colors[x]
        time.sleep(1)
        pixels.fill(BLACK)
    