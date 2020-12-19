import pygame
from classes import *
from constants import *

pygame.init()

DISPLAY = pygame.display.set_mode(SCREEN, 0, 32)
pygame.display.set_caption("Platformer Game - By Tools With Code")

BLACK = (0, 0, 0)

def Main():
    FPS = 60
    clock = pygame.time.Clock()
    player = Player(WIDTH // 2, HEIGHT // 2)
    while True:
        clock.tick(FPS)
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        DISPLAY.fill(BLACK)
        player.Draw(DISPLAY)
        player.Move(keys)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        pygame.display.update()

Main()