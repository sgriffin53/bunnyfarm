import copy
import pygame
from classes import Bunny


def drawHealthBar(screen, bunny):


    percentage = bunny.health * 100 / 100
    #centre = (gameinfo.width / 2, gameinfo.height / 2)

    drawX = bunny.x
    drawY = bunny.y + 40

    drawW = (50) * (percentage / 100)
    # draw health bar
    colour = (0, 168, 0)
    if percentage <= 50: colour = (168, 0, 0)
    pygame.draw.rect(screen, colour, (drawX, drawY, drawW, 10), 0)

    # draw border

    pygame.draw.rect(screen, (0, 0 , 128), (drawX, drawY, 50, 10), 2)

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
    if bunny.direction >= 270 or bunny.direction <= 90: bunny_image = pygame.transform.flip(bunny_image, True, False)
    heart_image = images[5]
    screen.blit(bunny_image, drawpos)
    if bunny.state == "mating":
        screen.blit(heart_image, drawpos)

def drawPlants(plants, screen):
    for plant in plants:
        pygame.draw.circle(screen, (0, 255, 0), (plant.x, plant.y), 3)

def renderFrame(screen, images, bunnies, plants):
    screen.fill((0, 64, 0))
    drawPlants(plants, screen)
    for bunny in bunnies:
        drawBunny(bunny, images, screen)
        drawHealthBar(screen, bunny)