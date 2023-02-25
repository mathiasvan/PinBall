import pygame
from math import sqrt, cos, sin, atan2, degrees

class Ball(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, pos=[0, 0], startVelocity=[0, 0]):
        super().__init__()
        self.image = pygame.image.load("ball.png")

        # Scale the ball according to the width and height of the screen
        if screen_width < screen_height:
            base = screen_width
        else:
            base = screen_height
        ratio = 15
        self.image = pygame.transform.scale(self.image, (base/ratio, base/ratio))
        # self.image = pygame.Surface([base/ratio, base/ratio])
        # self.image.fill((255, 255, 255))
        # self.image.set_colorkey((255, 255, 255))
        # pygame.draw.circle(self.image, (0, 0, 0), (base/ratio/2, base/ratio/2), base/ratio/2)

        self.rect = self.image.get_rect()
        self.rect.center = pos # TODO: also make the position dynamic
        self.velocity = startVelocity
        self.offScreen = False
        self.radius = base/ratio/2

    def update(self, screen_width, screen_height):
        # TODO: create gravity variable
        self.velocity = [self.velocity[0], self.velocity[1]]
        self.move()

        if self.rect.right < 0 or self.rect.left > screen_width:
            self.offScreen = True
        elif self.rect.bottom < 0 or self.rect.top > screen_height:
            self.offScreen = True
        else:
            self.offScreen = False

    def move(self):
        self.rect.move_ip(self.velocity)

    def resolve_collision(self, collision_object):
        
        v = sqrt(pow(self.velocity[0], 2) + pow(self.velocity[1], 2))
        if collision_object.__class__.__name__ == "Obstacle":
            d = atan2(self.velocity[1], -self.velocity[0])
            b = atan2(collision_object.rect.centerx - self.rect.centerx, collision_object.rect.centery - self.rect.centery)
            a = d - b

            print(degrees(a), degrees(b), degrees(d))

            # Move out of the ball
            self.rect.move_ip(-(self.velocity[0]), -(self.velocity[1]))
            # Calculate new velocity
            self.velocity[0] = -v * cos(a-b)
            self.velocity[1] = -v * sin(a-b)

            self.move()

            

            
