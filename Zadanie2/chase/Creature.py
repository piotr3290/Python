class Creature(object):
    def __init__(self, x, y, move_dist):
        self.x, self.y, self.move_dist = x, y, move_dist

    def move(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "x = " + str(self.x) + " y = " + str(self.y)