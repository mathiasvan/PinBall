import pygame
import sys

# *** GLOBAL CONSTANTS ***
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialise pygame
pygame.init()

win = pygame.display.set_mode((500, 500)) # (width, height)

# Title of display
pygame.display.set_caption("PinBall")

# Clock
clock = pygame.time.Clock()

# Game variables
game_active = True

# Game loop
while True:
    # All events happen here (mousemovement, keyboardinput, etc)
    for event in pygame.event.get():  # Get all events.
        if event.type == pygame.QUIT:  # If the red cross (top right) is pressed.
            # Close the window.
            pygame.quit()
            sys.exit()

    # All the drawing stuff comes here
    rect = pygame.Rect(250, 100, 100, 100) # x, y, w, h
    pygame.draw.rect(win, WHITE, rect) # See colors defined above

    # Update screen
    pygame.display.update()
    clock.tick(60) # 60fps