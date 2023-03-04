import pygame
import sys
import random
from display import Display
from ball import Ball
from obstacle import Obstacle

import time

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
ball_group = pygame.sprite.Group()
# ball = Ball(dis.w, dis.h, [100, 200], [3, -6])
# ball_group.add(ball)

# Obstacle
obstacle_group = pygame.sprite.Group()

for i in range(15):
    obstacle_group.add(Obstacle(dis.w, dis.h, [random.randint(0, dis.w), random.randint(0, dis.h)], (random.random()*3+0.5)+0.5, random.random()+0.5))
    

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
            err = False
            temp_ball = Ball(dis.w, dis.h, pygame.mouse.get_pos(), [0, 0])
            for o in obstacle_group.sprites():
                if pygame.sprite.collide_circle(temp_ball, o):
                    err = True
                    break
            if not err:    
                ball_group.add(temp_ball)
    
    # *** Updates ***
    ball_group.update(dis.w, dis.h)
    # If ball moved off the screen
    for b in ball_group:
        if b.offScreen == True:
            b.remove(ball_group) # Remove the ball from the screen
    
    # Ball collisions with obstacles
    ball_obs_collisions = pygame.sprite.groupcollide(ball_group, obstacle_group, False, False, pygame.sprite.collide_circle)
    for b in ball_obs_collisions:
        b.resolve_collision(ball_obs_collisions[b][0])
    
    # TODO: Ball collisions with other balls
    # Some starter code but not yet finished:
    # balls = pygame.sprite.Group.sprites(ball_group)
    # for i, ball1 in enumerate(balls):
    #     for ball2 in balls[i+1:]:
    #         if(pygame.sprite.collide_circle(ball1, ball2)):
    #             ball1.resolve_collision(ball2)

    # *** All the drawing stuff comes here ***
    # Background
    screen.fill(WHITE) # TODO: Add a draw function to the Display class
    obstacle_group.draw(screen)
    ball_group.draw(screen)
    
    # Update screen
    pygame.display.flip()
    clock.tick(60) # 60fps