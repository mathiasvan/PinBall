import pygame
import math
from ball import Ball

class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height, angle = 0, position = [0,0]):
        super().__init__()

        # Draw/setup the wall
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((55, 55, 55))
        self.rotated_image = pygame.transform.rotate(self.image, angle)
        self.rect = self.rotated_image.get_rect(center = self.image.get_rect(center = position).center)
        self.rect.center = position
        self.image = self.rotated_image
        self.rotated_vertices(width, height, angle, position)


    def rotated_vertices(self, width, height, angle, position):
        # Get the coordinates of the four vertices of the rectangle before rotation
        x1, y1 = position[0] - width/2, position[1] - height/2
        x2, y2 = position[0] + width/2, position[1] - height/2
        x3, y3 = position[0] + width/2, position[1] + height/2
        x4, y4 = position[0] - width/2, position[1] + height/2

        # Convert the angle from degrees to radians
        angle = math.radians(angle)
        # Rotate each vertices around the center of the the wall
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        cx, cy = position
        x1, y1 = (x1 - cx) * cos_theta - (y1 - cy) * sin_theta + cx, (x1 - cx) * sin_theta + (y1 - cy) * cos_theta + cy
        x2, y2 = (x2 - cx) * cos_theta - (y2 - cy) * sin_theta + cx, (x2 - cx) * sin_theta + (y2 - cy) * cos_theta + cy
        x3, y3 = (x3 - cx) * cos_theta - (y3 - cy) * sin_theta + cx, (x3 - cx) * sin_theta + (y3 - cy) * cos_theta + cy
        x4, y4 = (x4 - cx) * cos_theta - (y4 - cy) * sin_theta + cx, (x4 - cx) * sin_theta + (y4 - cy) * cos_theta + cy

        # Update vertices of wall
        self.rvertices = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        print(self.rvertices)

    def collision_detection(self, balls):
        for ball in balls:
            p_axis = pygame.math.Vector2(self.rect.centerx - ball.rect.centerx, self.rect.centery - ball.rect.centery)
            projection_min = None
            projection_max = None
            for vertice in self.rvertices:
                vector = pygame.math.Vector2(vertice[0] - self.rect.centerx, vertice[1] - self.rect.centery)
                projection = vector.dot(p_axis.normalize())
                if projection_min is None or projection < projection_min:
                    projection_min = projection
                if projection_max is None or projection > projection_max:
                    projection_max = projection
            p_radius = ball.radius * p_axis.normalize()
            p_length = p_axis.magnitude() - p_radius.magnitude()
            if p_length > 0 or projection_max < -p_radius.magnitude() or projection_min > p_radius.magnitude():
                continue
            print("collision")
            return True
