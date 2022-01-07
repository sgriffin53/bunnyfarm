import time
import random
import math
import physics

class Plant:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Bunny:
    def __init__(self, mother = None, father = None, x = 0, y = 0, colour = 0, costume = None, direction = 0):
        self.x = x
        self.y = y
        self.direction = direction
        self.mother = mother
        self.father = father
        self.colour = colour
        self.frame = 0
        self.costume = costume
        self.hopping = False
        self.state = "sitting"
        self.birthtime = time.time()
        self.actionstart = time.time()
        self.sittime = random.randint(2, 6)
        self.hoptime = random.randint(2, 6)
        self.speed = random.randint(30, 120)
        self.health = 100.0
        self.turnangle = 30
        self.lastate = time.time()
        self.parenttype = None
        self.mate = None
        self.lastmated = 0
        self.mother = None
        self.father = None
        self.mothergeneration = 1
        self.fathergeneration = 1
        if direction == -1:
            self.direction = random.randint(0, 360)
        pass

def spawnPlantsGroup(plants, plants_per_group, width, height):
    spawn_pos = (random.randint(50, width - 50), random.randint(50, height - 50))
    for i in range(plants_per_group):
        ang = random.randint(0, 360)
        rads = ang * math.pi / 180
        x = spawn_pos[0] + math.cos(rads) * random.randint(20, 90)
        y = spawn_pos[1] + math.sin(rads) * random.randint(20, 90)
        plants.append(Plant(x=x, y=y))


def bunnyTick(bunny, bunnies, images):
    if bunny.direction > 360: bunny.direction -= 360
    elif bunny.direction < 0: bunny.direction += 360
    duration = time.time() - bunny.actionstart
    age = time.time() - bunny.birthtime
    if bunny.state == "sitting":
        if duration >= bunny.sittime:
            bunny.state = "hopping"
            bunny.hopping = True
            bunny.direction += bunny.turnangle
            bunny.actionstart = time.time()
            return
        for bunnycand in bunnies:
            if bunnycand == bunny: continue
            if bunnycand.state == "sitting":
                lastmated_dur = time.time() - bunny.lastmated
                lastmated_dur_cand = time.time() - bunnycand.lastmated
                if physics.distance(bunny, bunnycand) < 50 and age > 20 and lastmated_dur > 60 and lastmated_dur_cand > 60 and bunny.health > 60 and bunnycand.health > 60:
                    bunny.state = "mating"
                    bunnycand.state = "mating"
                    bunny.parenttype = "mother"
                    bunnycand.parenttype = "father"
                    bunny.mate = bunnycand
                    bunnycand.mate = bunny
    elif bunny.state == "hopping":
        if duration >= bunny.hoptime:
            bunny.state = "sitting"
            bunny.hopping = False
            bunny.actionstart = time.time()
    elif bunny.state == "mating":
        if duration >= 4.0:
            if bunny.parenttype == "mother":
                birthLitter(bunnies, bunny, bunny.mate, images, random.randint(2, 5))
                if bunny.health > 25: bunny.health -= 25
                else: bunny.health = 1
            bunny.state = "sitting"
            bunny.mate.state = "sitting"
            bunny.mate.actionstart = time.time()
            bunny.actionstart = time.time()
            bunny.lastmated = time.time()
            bunny.mate.lastmated = time.time()

def spawnBunnyGroups(bunnies, width, height, images, num_groups = 10, bunnies_per_group = 6):
    bunny_idx = -1
    for i in range(num_groups):
        spawn_pos = (random.randint(50, width - 50), random.randint(50, height - 50))
        colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turn_angle = random.randint(0, 360)
        speed = random.randint(10, 50)
        sit_time = random.randint(2, 6)
        hop_time = random.randint(2, 6)
        for i in range(bunnies_per_group):
            ang = random.randint(0, 360)
            rads = ang * math.pi / 180
            x = spawn_pos[0] + math.cos(rads) * random.randint(20, 60)
            y = spawn_pos[1] + math.sin(rads) * random.randint(20, 60)
            bunnies.append(Bunny(x=x, y=y, costume=images[0], colour=colour, direction=-1))
            bunny_idx += 1
            bunnies[bunny_idx].speed = speed
            bunnies[bunny_idx].turnangle = turn_angle
            bunnies[bunny_idx].hoptime = hop_time
            bunnies[bunny_idx].sittime = sit_time

def birthLitter(bunnies, mother, father, images, bunnies_per_litter):
    spawn_pos = (mother.x, mother.y)
    red = int((mother.colour[0] + father.colour[0]) / 2)
    green = int((mother.colour[1] + father.colour[1]) / 2)
    blue = int((mother.colour[2] + father.colour[2]) / 2)
    hop_time = (mother.hoptime + father.hoptime) / 2
    speed = (mother.speed + father.speed) / 2
    sit_time = (mother.sittime + father.sittime) / 2
    turn_angle = (mother.turnangle + father.turnangle) / 2
    bunny_idx = len(bunnies) - 1
    for i in range(bunnies_per_litter):
        red *= random.uniform(0.9500, 1.0500)
        green *= random.uniform(0.9500, 1.0500)
        blue *= random.uniform(0.9500, 1.0500)
        if red < 0: red = 0
        if blue < 0: blue = 0
        if green < 0: green = 0
        if red > 255: red = 255
        if blue > 255: blue = 255
        if green > 255: green = 255
        turn_angle *= random.uniform(0.8500, 1.1500)
        sit_time *= random.uniform(0.8500, 1.1500)
        hop_time *= random.uniform(0.8500, 1.1500)
        speed *= random.uniform(0.8500, 1.1500)
        colour = (red, green, blue)
        ang = random.randint(0, 360)
        rads = ang * math.pi / 180
        x = spawn_pos[0] + math.cos(rads) * random.randint(20, 60)
        y = spawn_pos[1] + math.sin(rads) * random.randint(20, 60)
        bunnies.append(Bunny(x=x, y=y, costume=images[0], colour=colour, direction=-1))
        bunny_idx += 1
        bunnies[bunny_idx].speed = speed
        bunnies[bunny_idx].turnangle = turn_angle
        bunnies[bunny_idx].hoptime = hop_time
        bunnies[bunny_idx].sittime = sit_time
        bunnies[bunny_idx].mother = mother
        bunnies[bunny_idx].mother = father
        bunnies[bunny_idx].mothergeneration = mother.mothergeneration + 1
        bunnies[bunny_idx].fathergeneration = father.fathergeneration + 1

def showStats(bunnies, highest_pop, age_record, starttime):
    tot_age = 0
    highest_gen = 0
    highest_age = 0
    for bunny in bunnies:
        age = time.time() - bunny.birthtime
        age = int(age)
        tot_age += age
        if age > highest_age:
            highest_age = age
        if age > age_record:
            age_record = age
        if bunny.mothergeneration > highest_gen:
            highest_gen = bunny.mothergeneration
        if bunny.fathergeneration > highest_gen:
            highest_gen = bunny.fathergeneration
    avg_age = tot_age / len(bunnies)
    avg_age = int(avg_age)
    highest_age = int(highest_age)
    if len(bunnies) > highest_pop: highest_pop = len(bunnies)
    time_running = time.time() - starttime
    time_running = int(time_running)
    print("---")
    print("Time running: ", time_running)
    print("Old age record: ", age_record)
    print("Oldest bunny: ", highest_age)
    print("Highest generation: ", highest_gen)
    print("Average age: ", avg_age)
    print("Population: ", len(bunnies))
    print("Highest population: ", highest_pop)
    return highest_pop, age_record