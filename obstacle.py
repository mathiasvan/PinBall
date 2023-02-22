import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, screen):
        super().__init__()

        ball_size = 15

        # Adjust the walls according to the width and height of the window
        if screen_width < screen_height:
            base = screen_width
        else:
            base = screen_height
        ratio = 30

        self.image = pygame.Surface((base/ratio, screen_height))
        self.image.fill((55, 55, 55))
        self.rect = self.image.get_rect()

        # self.right_wall = pygame.Surface((base / ratio, screen_height-ball_size * 3.5))
        # self.right_wall.fill((55, 55, 55))
        # screen.blit(self.right_wall, (screen_width - 1.1 * ball_size, 1.5 * ball_size))

        # self.rightmost_wall = pygame.Surface((base / ratio, screen_height))
        # self.rightmost_wall.fill((55, 55, 55))
        # screen.blit(self.rightmost_wall, (screen_width - screen_width / ratio, 0))

        # self.top_wall = pygame.Surface((screen_width, base / ratio))
        # self.top_wall.fill((55, 55, 55))
        # screen.blit(self.top_wall, (0,0))
        
        