import pygame
import neat
import random
import time
import os
pygame.init()
pygame.font.init()
WIN_H = 600
WIN_W = 600

BG_IMG = pygame.image.load(os.path.join("IMG", "BG.png"))
PLAYER_IMG = pygame.image.load(os.path.join("IMG", "rocket.png"))
def player(window,x,y):
    window.blit(PLAYER_IMG, (x,y))

def main():
    clock = pygame.time.Clock()
    run = True
    player_x = 300
    player_y = 450
    player_x_change = 0

    while run:
        clock.tick(30)
        win = pygame.display.set_mode((WIN_W,WIN_H))
        win.fill((240,240,240))
        player(win,player_x,player_y)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -5

                if event.key == pygame.K_RIGHT:
                    player_x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        



main()
