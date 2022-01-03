import copy
import pygame
from bunny import Bunny

def colourBunny(bunny_image, new_colour):
    brown = (171, 122, 68)
    thresh = (50, 50, 50)
    new_colour = new_colour
    pygame.transform.threshold(bunny_image, bunny_image, brown, thresh, new_colour,
                               1, None, True)

def drawBunny(bunny, images, screen):
    bunny_image = copy.copy(bunny.costume)
    drawpos = [bunny.x, bunny.y]
    colourBunny(bunny_image, bunny.colour)
    screen.blit(bunny_image, drawpos)


def renderFrame(screen, images, bunnies):
    screen.fill((0, 64, 0))
    for bunny in bunnies:
        drawBunny(bunny, images, screen)