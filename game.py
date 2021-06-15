import pygame, sys
from pygame.locals import *

pygame.init()
wind = pygame.display.set_mode((400,400))
pygame.display.set_caption("Distance Software")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    pygame.display.update()