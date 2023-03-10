import pygame
import math
from random import randint

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

    # calculate the location of vertices after rotation
    def rotated_vertices(self, width, height, angle, position):
        # Get the coordinates of the four vertices of the rectangle before rotation
        x1, y1 = position[0] - width/2, position[1] - height/2
        x2, y2 = position[0] + width/2, position[1] - height/2
        x3, y3 = position[0] + width/2, position[1] + height/2
        x4, y4 = position[0] - width/2, position[1] + height/2

        # Convert the angle from degrees to radians and make it negative
        angle = -math.radians(angle)
        # Rotate each vertices around the center of the the wall
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        cx, cy = position
        x1, y1 = (x1 - cx) * cos_theta - (y1 - cy) * sin_theta + cx, (x1 - cx) * sin_theta + (y1 - cy) * cos_theta + cy
        x2, y2 = (x2 - cx) * cos_theta - (y2 - cy) * sin_theta + cx, (x2 - cx) * sin_theta + (y2 - cy) * cos_theta + cy
        x3, y3 = (x3 - cx) * cos_theta - (y3 - cy) * sin_theta + cx, (x3 - cx) * sin_theta + (y3 - cy) * cos_theta + cy
        x4, y4 = (x4 - cx) * cos_theta - (y4 - cy) * sin_theta + cx, (x4 - cx) * sin_theta + (y4 - cy) * cos_theta + cy

        # Update vertices of wall
        self.vertices = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

        # 4 sides of the wall in endpoint coordinates
        self.sides = (((self.vertices[0]),(self.vertices[1])),((self.vertices[1]),(self.vertices[2])),((self.vertices[2]),(self.vertices[3])),((self.vertices[3]),(self.vertices[0])))

    # Draw whatever that helps with debugging
    def drawlines(self,screen,balls): 
        # Draws the colliding side
        for side in self.sides:
            for ball in balls:
                side_vector = pygame.math.Vector2(side[1][0]-side[0][0],side[1][1]-side[0][1])
                ball_to_end = [ball.rect.centerx-side[0][0], ball.rect.centery-side[0][1]]
                dot_product = ball_to_end[0]*side_vector[0] + ball_to_end[1]*side_vector[1]
                side_vector_squared = side_vector[0]**2 + side_vector[1]**2
                t = max(0, min(dot_product / side_vector_squared, 1))
                closest = [side[0][0] + t*side_vector[0], side[0][1] + t*side_vector[1]]
            try:
                pygame.draw.line(screen,"green",self.side[0],self.side[1],5)
            except:
                continue

    # Checks for collision and determine the side of collision
    def collision_detection(self,ball): 
        # For the ball potentially colliding with 2 walls at once (corner)
        collided_sides = list() 
        # Checking for collision with each sides and append all colliding sides to the list collided_sides
        for side in self.sides:
            side_vector = pygame.math.Vector2(side[1][0]-side[0][0],side[1][1]-side[0][1])
            ball_to_end = [ball.rect.centerx-side[0][0], ball.rect.centery-side[0][1]]
            dot_product = ball_to_end[0]*side_vector[0] + ball_to_end[1]*side_vector[1]
            side_vector_squared = side_vector[0]**2 + side_vector[1]**2
            t = max(0, min(dot_product / side_vector_squared, 1))
            closest = [side[0][0] + t*side_vector[0], side[0][1] + t*side_vector[1]]
            distance = math.sqrt((ball.rect.centerx-closest[0])**2 + (ball.rect.centery-closest[1])**2) - ball.radius
            if distance <= 0:
                collided_sides.append([side, distance])
        # Determine side of collision to use for calculating bouncing
        for side in collided_sides:
            if len(collided_sides) > 1 and collided_sides[0][1] == collided_sides[1][1]:
                if collided_sides[0][0][0] == collided_sides[1][0][0] or collided_sides[0][0][0] == collided_sides[1][0][1]:
                    corner = collided_sides[0][0][0]
                    p1 = collided_sides[0][0][1]
                    p2 = collided_sides[1][0][0]
                else:
                    corner = collided_sides[0][0][1]
                    p1 = collided_sides[0][0][0]
                    p2 = collided_sides[1][0][1]
                normal1 = pygame.math.Vector2(corner[0] - p1[0], corner[1] - p1[1]).normalize()
                normal2 = pygame.math.Vector2(corner[0] - p2[0], corner[1] - p2[1]).normalize()
                self.side = ((corner[0] + normal1[0],corner[1] + normal1[1]),(corner[0] + normal2[0],corner[1] + normal2[1]))
                return True
            elif len(collided_sides) > 1 and collided_sides[0][1] != collided_sides[1][1]:
                self.side = collided_sides[0][0] if collided_sides[0][1] < collided_sides[1][1] else collided_sides[1][0]
                return True
            else:
                self.side = collided_sides[0][0]
                return True