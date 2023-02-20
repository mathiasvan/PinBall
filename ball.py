import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, screen_width, pos=[0, 0], startVelocity=[0, 0]):
        super().__init__()
        self.image = pygame.image.load("ball.png")
        # TODO: Fix the scale of the ball
        self.image = pygame.transform.scale(self.image, (screen_width/15, screen_width/15))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.velocity = startVelocity
        self.offScreen = False

    def update(self, screen_width, screen_height):
        # TODO: create gravity variable
        self.velocity = [self.velocity[0], self.velocity[1] + 0.1]
        self.rect.move_ip(self.velocity)

        if self.rect.right < 0 or self.rect.left > screen_width:
            self.offScreen = True
            return
        elif self.rect.bottom < 0 or self.rect.top > screen_height:
            self.offScreen = True
            return
        else:
            self.offScreen = False
