import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, pos, diameter, friction):
        """Initialise the Obstacle class

        Args:
            screen_width (Int): the width of the pygame window
            screen_height (Int): the height of the pygame window
            pos (List): x and y coordinates of the obstacle
            diameter (Int): diameter of the obstacle, relative to the ball: 1 is the same diameter as the ball
            friction (Float): number between 1 and 0. The velocity will not be changed if friction is 1. If friction is 0, all the kinetic energy of the ball will be lost.
        """
        super().__init__()

        # Scale the obstacle according to the width and height of the screen
        if screen_width < screen_height:
            base = screen_width
        else:
            base = screen_height
        self.radius = (base/15) * diameter / 2

        self.image = pygame.Surface([self.radius*2, self.radius*2])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        
        pygame.draw.circle(self.image, (0, 0, 0), (self.radius, self.radius), self.radius)

        self.rect = self.image.get_rect()
        self.rect.center = pos # TODO: Also make this dynamic

        self.friction = friction
