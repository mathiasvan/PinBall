import pygame
import sys
import math
from random import randint
from display import Display
from ball import Ball
from wall import Wall

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
    MOUSEBUTTONDOWN,
    QUIT,
)

# Initialise pygame
pygame.init()

# Set the width and height relative to the user screen so that it always fits
dis = Display(3, 1.1) # ratioWidth, ratioHeight -> 
# width = 1/3 of the total screen width of the user
# height = a bit less than the full height of the user screen
screen = dis.create_display() # Create the display

# Title of display
pygame.display.set_caption("PinBall")

# Clock
clock = pygame.time.Clock()

# Ball
# ball = Ball(dis.w, dis.h, [100, 200], [3, -6])
ball_group = pygame.sprite.Group()
# ball_group.add(ball)

test_wall = Wall(420,30,240,[450,450])
wall_group = pygame.sprite.Group()
wall_group.add(test_wall)

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

        if event.type == MOUSEBUTTONDOWN:
            for n in range(1):
                #ball_group.add(Ball(dis.w, dis.h, (590,385), [-2,-0]))
                velocity = [randint(-4,4), randint(-4,4)]
                ball_group.add(Ball(dis.w, dis.h, pygame.mouse.get_pos(), velocity))
                #ball_group.add(Ball(dis.w, dis.h, (590,385), velocity))
                print(pygame.mouse.get_pos())
                print(velocity)
    
    # *** Updates ***
    ball_group.update(dis.w, dis.h)

    # check for collision between balls and walls
    for ball in ball_group:
        for wall in wall_group:
            if wall.collision_detection(ball):
                ball.resolve_collision(wall)

    # If ball moved off the screen
    for b in ball_group:
        if b.offScreen == True:
            b.remove(ball_group) # Remove the ball from the screen

    # *** All the drawing stuff comes here ***
    # Background
    screen.fill(WHITE) # TODO: Add a draw function to the Display class
    ball_group.draw(screen)
    wall_group.draw(screen)

    # Draw things to help with debugging
    for wall in wall_group:
        wall.drawlines(screen, ball_group)

    # Update screen
    pygame.display.flip()
    clock.tick(60) # 60fps
