from classes import *
import pygame
import math
import time
import classes

def distance(item1, item2):
    return math.sqrt((abs(item1.x - item2.x) ** 2) + (abs(item1.y - item2.y) ** 2))

def physicsTick(time_since_phys_tick, bunnies, plants, images, width, height):
    framerate = 8
    for j, bunny in enumerate(bunnies):
        bunny.health -= 1.5 * time_since_phys_tick
        if bunny.health <= 0:
            bunnies.pop(j)
            continue
        if bunny.hopping:
            bunny.frame += framerate * time_since_phys_tick
            realframe = int(bunny.frame)
            if realframe % 4 == 0: bunny.costume = images[1]
            elif realframe % 4 == 1: bunny.costume = images[2]
            elif realframe % 4 == 2: bunny.costume = images[3]
            elif realframe % 4 == 3: bunny.costume = images[4]
            rads = bunny.direction * math.pi / 180
            bunny.x += bunny.speed * math.cos(rads) * time_since_phys_tick
            bunny.y += bunny.speed * math.sin(rads) * time_since_phys_tick
            if bunny.x > width - 40:
                bunny.x = width - 40
            elif bunny.x < 20:
                bunny.x = 20
            if bunny.y < 20:
                bunny.y = 20
            elif bunny.y > height - 30:
                bunny.y = height - 30
        else:
            bunny.costume = images[0]
        for i, plant in enumerate(plants):
            dist = distance(bunny, plant)
            time_since_ate = time.time() - bunny.lastate
            if dist < 15 and time_since_ate > 0.5:
                bunny.health += 5
                bunny.lastate = time.time()
                if bunny.health > 100: bunny.health = 100
                plants.pop(i)
        #bunny.costume = images[1]
    #if len(plants) < 50 * 50 - 50:
        #classes.spawnPlantsGroup(plants, 50, width, height)