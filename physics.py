from bunny import *
import pygame

def physicsTick(time_since_phys_tick, bunnies, images):
    framerate = 8
    for bunny in bunnies:
        if bunny.hopping:
            bunny.frame += framerate * time_since_phys_tick
            realframe = int(bunny.frame)
            if realframe % 4 == 0: bunny.costume = images[1]
            elif realframe % 4 == 1: bunny.costume = images[2]
            elif realframe % 4 == 2: bunny.costume = images[3]
            elif realframe % 4 == 3: bunny.costume = images[4]
        else:
            bunny.costume = images[0]
        #bunny.costume = images[1]