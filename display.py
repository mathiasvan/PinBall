import pygame

class Display():
    def __init__(self, rw, rh):
        """
        Set the width and height of the window relative to the user screen.
        Input:  - rw: ratioWidth, screenWidth / ratioWidth = displayWidth
                - rh: ratioHeight, screenHeight / ratioHeight = displayHeight
        """
        # Get the width of the user display
        display_width, display_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.w = float(display_width / rw) # Set the width of the pygame display relative the the user display
        self.h = float(display_height / rh)
    
    def create_display(self):
        """Creates a display with a set width and height"""
        return pygame.display.set_mode((self.w, self.h))