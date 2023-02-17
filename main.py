import pygame
import sys
from display import Display

# *** GLOBAL CONSTANTS ***
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialise pygame
pygame.init()

# Set the width and height relative to the user screen so that it always fits
dis = Display(3, 1.1) # ratioWidth, ratioHeight
win = dis.create_display() # Create the display

# Title of display
pygame.display.set_caption("PinBall")

# Clock
clock = pygame.time.Clock()

# Game loop
while True:
    # *** All events happen here (mousemovement, keyboardinput, etc) ***
    for event in pygame.event.get():  # Get all events.
        if event.type == QUIT:  # If the red cross (top right) is pressed.
            # Close the window.
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN: # If a key is pressed
            if event.key == K_ESCAPE: # If the key is the escape key
                # Close the window.
                pygame.quit()
                sys.exit()

    # *** All the drawing stuff comes here ***
    # Background
    win.fill(WHITE) # TODO: Add a draw function to the Display class

    # Update screen
    pygame.display.flip()
    clock.tick(60) # 60fps