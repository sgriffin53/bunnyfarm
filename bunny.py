class Bunny:
    def __init__(self, mother = None, father = None, x = 0, y = 0, colour = 0, costume = None):
        self.x = x
        self.y = y
        self.speed = 0
        self.direction = 0
        self.mother = mother
        self.father = father
        self.colour = colour
        self.frame = 0
        self.costume = costume
        self.hopping = False
        pass