import pygame
import math

class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height, angle = 0, position = [0,0]):
        super().__init__()

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((55, 55, 55))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(topleft = position)

        def collision(self, ball):
            if pygame.sprite.collide_rect(self, ball):
                # Get the center coordinates of the ball and the wall
                ball_center = ball.rect.center
                wall_center = self.rect.center

                # Calculate the angle between the centers of the ball and the wall
                angle = math.atan2(ball_center[1] - wall_center[1], ball_center[0] - wall_center[0])

                # Calculate the new velocity of the ball
                ball_speed = math.sqrt(ball.velocity[0] ** 2 + ball.velocity[1] ** 2)
                new_speed = ball_speed * math.cos(angle)
                new_velocity = [-new_speed * math.cos(angle), -new_speed * math.sin(angle)]

                # Update the ball's velocity
                ball.velocity = new_velocity
