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


    '''def drawlines(self,screen,balls): # draw whatever that helps with debugging, which for now it draws the line from center of ball to closest point on wall
        for side in self.sides:
            #pygame.draw.line(screen, (0,255,0), side[0], side[1], 4)
            for ball in balls:
                side_vector1 = pygame.math.Vector2(self.sides[0][1][0]-self.sides[0][0][0],self.sides[0][1][1]-self.sides[0][0][1])
                side_vector2 = pygame.math.Vector2(self.sides[1][1][0]-self.sides[1][0][0],self.sides[1][1][1]-self.sides[1][0][1])
                side_vector3 = pygame.math.Vector2(self.sides[2][1][0]-self.sides[2][0][0],self.sides[2][1][1]-self.sides[2][0][1])
                side_vector4 = pygame.math.Vector2(self.sides[3][1][0]-self.sides[3][0][0],self.sides[3][1][1]-self.sides[3][0][1])
                ball_to_end1 = [ball.rect.centerx-self.sides[0][0][0], ball.rect.centery-self.sides[0][0][1]]
                ball_to_end2 = [ball.rect.centerx-self.sides[1][0][0], ball.rect.centery-self.sides[1][0][1]]
                ball_to_end3 = [ball.rect.centerx-self.sides[2][0][0], ball.rect.centery-self.sides[2][0][1]]
                ball_to_end4 = [ball.rect.centerx-self.sides[3][0][0], ball.rect.centery-self.sides[3][0][1]]
                dot_product1 = ball_to_end1[0]*side_vector1[0] + ball_to_end1[1]*side_vector1[1]
                dot_product2 = ball_to_end2[0]*side_vector2[0] + ball_to_end2[1]*side_vector2[1]
                dot_product3 = ball_to_end3[0]*side_vector3[0] + ball_to_end3[1]*side_vector3[1]
                dot_product4 = ball_to_end4[0]*side_vector4[0] + ball_to_end4[1]*side_vector4[1]
                side_vector_squared1 = side_vector1[0]**2 + side_vector1[1]**2
                side_vector_squared2 = side_vector2[0]**2 + side_vector2[1]**2
                side_vector_squared3 = side_vector3[0]**2 + side_vector3[1]**2
                side_vector_squared4 = side_vector4[0]**2 + side_vector4[1]**2
                t1 = max(0, min(dot_product1 / side_vector_squared1, 1))
                t2 = max(0, min(dot_product2 / side_vector_squared2, 1))
                t3 = max(0, min(dot_product3 / side_vector_squared3, 1))
                t4 = max(0, min(dot_product4 / side_vector_squared4, 1))
                D1 = [self.sides[0][0][0] + t1*side_vector1[0], self.sides[0][0][1] + t1*side_vector1[1]]
                D2 = [self.sides[1][0][0] + t2*side_vector2[0], self.sides[1][0][1] + t2*side_vector2[1]]
                D3 = [self.sides[2][0][0] + t3*side_vector3[0], self.sides[2][0][1] + t3*side_vector3[1]]
                D4 = [self.sides[3][0][0] + t4*side_vector4[0], self.sides[3][0][1] + t4*side_vector4[1]]
                linelength = dict()
                linelength["D1"] = pygame.math.Vector2(ball.rect.centerx - D1[0], ball.rect.centery - D1[1]).magnitude()
                linelength["D2"] = pygame.math.Vector2(ball.rect.centerx - D2[0], ball.rect.centery - D2[1]).magnitude()
                linelength["D3"] = pygame.math.Vector2(ball.rect.centerx - D3[0], ball.rect.centery - D3[1]).magnitude()
                linelength["D4"] = pygame.math.Vector2(ball.rect.centerx - D4[0], ball.rect.centery - D4[1]).magnitude()
                linelength = sorted(linelength.items(),key=lambda x:x[1])
                if linelength[0][0] == "D1":
                    color = "green"
                    pygame.draw.line(screen, color, ball.rect.center, D1, 1)
                if linelength[0][0] == "D2":
                    color = "red"
                    pygame.draw.line(screen, color, ball.rect.center, D2, 1)
                if linelength[0][0] == "D3":
                    color = "green"
                    pygame.draw.line(screen, color, ball.rect.center, D3, 1)
                if linelength[0][0] == "D4":
                    color = "red"
                    pygame.draw.line(screen, color, ball.rect.center, D4, 1)
                try:
                    pygame.draw.line(screen,"purple",self.side[0],self.side[1],3)
                except:
                    continue'''


    def drawlines(self,screen,balls): # draw whatever that helps with debugging, which for now it draws the line from center of ball to closest point on wall
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

    
    def collision_detection(self,ball):
        collided_sides = list()
        for side in self.sides: # loop through all four sides of the wall
            side_vector = pygame.math.Vector2(side[1][0]-side[0][0],side[1][1]-side[0][1]) # creating vector of side
            ball_to_end = [ball.rect.centerx-side[0][0], ball.rect.centery-side[0][1]] # distance between center of ball and endpoint of side
            dot_product = ball_to_end[0]*side_vector[0] + ball_to_end[1]*side_vector[1]
            side_vector_squared = side_vector[0]**2 + side_vector[1]**2
            t = max(0, min(dot_product / side_vector_squared, 1))
            closest = [side[0][0] + t*side_vector[0], side[0][1] + t*side_vector[1]]
            distance = math.sqrt((ball.rect.centerx-closest[0])**2 + (ball.rect.centery-closest[1])**2) - ball.radius
            if distance <= 0:
                collided_sides.append([side, distance])
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