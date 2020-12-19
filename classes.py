import pygame
import math

pygame.init()

class Player:
    WIDTH = 40
    HEIGHT = 80
    VEL = 5
    JUMP_HEIGHT = math.sqrt(49)
    NGTV_JUMP_HEIGHT = 0 - JUMP_HEIGHT
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)

    def Draw(self, display):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.WIDTH, self.HEIGHT))

    def Move(self, keys):
        jump = False
        if not jump:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.x -= self.VEL
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.x += self.VEL
            if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
                jump = True
        else:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.x -= self.VEL
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.x += self.VEL
            if self.JUMP_HEIGHT >= self.NGTV_JUMP_HEIGHT:
                
                neg = 1
                if self.JUMP_HEIGHT < 0:
                    neg = -1
                self.y -= (self.JUMP_HEIGHT ** 2) * neg
                self.JUMP_HEIGHT -= 1
            else:
                self.jump = False
                self.JUMP_HEIGHT = math.sqrt(49)