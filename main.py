# Import and initialize the pygame library
import render
import keypresses
import pygame
import os
import time
import random
import physics
from bunny import *

pygame.init()
pygame.font.init()  # you have to call this at the start,
pygame.display.set_caption('Bunny Farm')

fullscreen = False

width = 1260
height = 768

screen = pygame.display.set_mode([width, height]) # don't set full screen mode to start or it messes up switching resolutions

images = []
images.append(pygame.image.load(os.path.join('images','bunny_idle_trans.png')).convert_alpha())
images.append(pygame.image.load(os.path.join('images','bunny_hop1_trans.png')).convert_alpha())
images.append(pygame.image.load(os.path.join('images','bunny_hop2_trans.png')).convert_alpha())
images.append(pygame.image.load(os.path.join('images','bunny_hop3_trans.png')).convert_alpha())
images.append(pygame.image.load(os.path.join('images','bunny_hop4_trans.png')).convert_alpha())

# Set up the drawing window
if not fullscreen:
    pass
#    screen = pygame.display.set_mode([width, height])
else:
    screen = pygame.display.set_mode([width, height], pygame.FULLSCREEN)

running = True

game_clock = pygame.time.Clock()

bunnies = []
for i in range(200):
    x = random.randint(100, 1200)
    y = random.randint(100, 700)
    colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    bunnies.append(Bunny(x=x, y=y, costume=images[0], colour=colour))

last_phys_tick = time.time()
starttime = time.time()

# main game loop

while running:

    if time.time() - starttime >= 3:
        for bunny in bunnies:
            bunny.hopping = True

    event_get = pygame.event.get()
    keypresses.detectKeyPresses(event_get, running)

    curtime = time.time()
    time_since_phys_tick = curtime - last_phys_tick
    physics.physicsTick(time_since_phys_tick, bunnies, images)
    last_phys_tick = curtime

    render.renderFrame(screen, images, bunnies)
    game_clock.tick(165000)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()