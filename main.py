import pygame
from classes import *
from constants import *

pygame.init()

DISPLAY = pygame.display.set_mode(SCREEN, 0, 32)
pygame.display.set_caption("Platformer Game - By Tools With Code")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

STDFONT = pygame.font.SysFont("comicsans", 60)

def Main():
    FPS = 60
    clock = pygame.time.Clock()
    player = Player(WIDTH // 2, HEIGHT // 2)
    coin = Coin(300, HEIGHT // 2)
    score = 0
    while True:
        clock.tick(FPS)
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        DISPLAY.fill(BLACK)
        player.Draw(DISPLAY)
        player.Move(keys)
        coin.Draw(DISPLAY)
        if coin.CollideWithPlayer(player):
            score += 1
        scoreText = STDFONT.render(str(score), 1, WHITE)
        DISPLAY.blit(scoreText, (20, 20))

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        pygame.display.update()

Main()