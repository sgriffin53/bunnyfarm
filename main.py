# Import and initialize the pygame library
import render
import keypresses
import pygame
import os
import time
import random
import physics
from classes import *

pygame.init()
pygame.font.init()  # you have to call this at the start,
pygame.display.set_caption('Bunny Farm')

fullscreen = False

width = 1260
height = 768

screen = pygame.display.set_mode([width, height]) # don't set full screen mode to start or it messes up switching resolutions

images = []
images.append(pygame.image.load(os.path.join('images','bunny_idle_trans.png')).convert_alpha())
images.append(pygame.image.load(os.path.join('images','bunny_hop1_trans.png')).convert_alpha()) # 1
images.append(pygame.image.load(os.path.join('images','bunny_hop2_trans.png')).convert_alpha()) # 2
images.append(pygame.image.load(os.path.join('images','bunny_hop3_trans.png')).convert_alpha()) # 3
images.append(pygame.image.load(os.path.join('images','bunny_hop4_trans.png')).convert_alpha()) # 4
images.append(pygame.image.load(os.path.join('images','heart.png')).convert_alpha()) # 5

# Set up the drawing window
if not fullscreen:
    pass
#    screen = pygame.display.set_mode([width, height])
else:
    screen = pygame.display.set_mode([width, height], pygame.FULLSCREEN)

running = True

game_clock = pygame.time.Clock()

bunnies = []
'''
for i in range(50):
    x = random.randint(100, 1200)
    y = random.randint(100, 700)
    colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
   # bunnies.append(Bunny(x=x, y=y, costume=images[0], colour=colour, direction = -1))
'''
plants = []
spawnBunnyGroups(bunnies, width, height, images)
for i in range(50):
    spawnPlantsGroup(plants, 50, width, height)

last_phys_tick = time.time()
starttime = time.time()

laststats = time.time()
highest_pop = 0
age_record = 0
lastplantspawn = time.time()

# main game loop

while running:

    event_get = pygame.event.get()
    keypresses.detectKeyPresses(event_get, running)

    curtime = time.time()
    time_since_phys_tick = curtime - last_phys_tick
    physics.physicsTick(time_since_phys_tick, bunnies, plants, images, width, height)
    last_phys_tick = curtime
    for bunny in bunnies:
        bunnyTick(bunny, bunnies, images)
    laststats_dur = time.time() - laststats
    if laststats_dur > 5:
        highest_pop, age_record = showStats(bunnies, highest_pop, age_record, starttime)
        laststats = time.time()
    planttime = time.time() - lastplantspawn
    if planttime > 25:
        spawnPlantsGroup(plants, 100, width, height)
        lastplantspawn = time.time()
    render.renderFrame(screen, images, bunnies, plants)
    game_clock.tick(165000)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()