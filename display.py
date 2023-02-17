import pygame

class Display():
    def __init__(self, rw, rh):
        """
        Set the width and height of the window relative to the user screen.
        Input:  - rw: (ratioWidth): screenWidth / ratioWidth = displayWidth
                - rh: (ratioHeight): screenHeight / ratioHeight = displayHeight
        """
        # Get the width of the user display
        self.w = round(pygame.display.get_desktop_sizes()[0][0] / rw)
        self.h = round(pygame.display.get_desktop_sizes()[0][1] / rh)
    
    def create_display(self):
        """Creates a display with a set width and height"""
        return pygame.display.set_mode((self.w, self.h))