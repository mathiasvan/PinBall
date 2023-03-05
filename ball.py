import pygame
from math import sqrt, cos, sin, atan2, degrees

class Ball(pygame.sprite.Sprite):
    image_preload = pygame.image.load("basket_ball.png")

    def __init__(self, screen_width, screen_height, pos=[0, 0], startVelocity=[0, 0]):
        """Initialises the Ball class.

        Args:
            screen_width (Int): the width of the pygame window
            screen_height (Int): the height of the pygame window
            pos (List, optional): the start x and y coordinates. Defaults to [0, 0].
            startVelocity (List, optional): the start velocity in the x and y direction. Defaults to [0, 0].
        """

        super().__init__()
        self.image = self.image_preload # Preloads the image so that it does not need to be loaded every single time a new ball is created.

        # Scale the ball according to the width and height of the screen
        if screen_width < screen_height:
            base = screen_width
        else:
            base = screen_height
        ratio = 15
        self.image = pygame.transform.scale(self.image, (base/ratio, base/ratio))
        
        self.rect = self.image.get_rect() # Create rect for the ball
        self.rect.center = pos # TODO: also make the position dynamic
        self.velocity = startVelocity
        self.offScreen = False # The obstacle will be removed from the screen if it is not on it anymore
        self.radius = base/ratio/2 # Dynamically calculate the radius of the obstacle

    def update(self, screen_width, screen_height):
        """Moves the ball based on it's velocity and gravity. Sets the variable offScreen to True if the ball is off the screen.

        Args:
            screen_width (Int): the width of the pygame window
            screen_height (Int): the height of the pygame window
        """

        # TODO: create gravity variable
        self.velocity = [self.velocity[0], self.velocity[1] + 0.3]
        self.move() # Move the ball based on it's new velocity

        if self.rect.right < 0 or self.rect.left > screen_width: # If the ball is not visible on the left or right side of the screen
            self.offScreen = True
        elif self.rect.bottom < 0 or self.rect.top > screen_height: # If the ball is not visible on the top or bottom of the screen
            self.offScreen = True
        else:
            self.offScreen = False

    def move(self):
        """Moves the ball based on it's velocity.
        """        

        self.rect.move_ip(self.velocity)

    def resolve_collision(self, collision_object):
        
        # Get the velocity vector
        v = sqrt(pow(self.velocity[0], 2) + pow(self.velocity[1], 2))
        
        # Get the angle between v and the x-axis
        d = atan2(self.velocity[1], -self.velocity[0])
        
        # Get the angle of the rotation of the collision surface, relative to the x-axis
        if collision_object.__class__.__name__ == "Obstacle":
            b = atan2(collision_object.rect.centerx - self.rect.centerx, collision_object.rect.centery - self.rect.centery)
        
        # Get the angle of collision relative to the collision surface
        a = d - b

        # print(degrees(a), degrees(b), degrees(d))

        # Move out of the ball
        self.rect.move_ip(-(self.velocity[0]), -(self.velocity[1]))
        
        # Calculate new velocity with the calculated angles based on the friction of the collision object
        self.velocity[0] = -v * cos(a-b) * collision_object.friction
        self.velocity[1] = -v * sin(a-b) * collision_object.friction
