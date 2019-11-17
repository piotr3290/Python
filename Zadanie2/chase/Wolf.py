from chase.Creature import Creature
import math
import sys


class Wolf(Creature):
    def __init__(self, wolf_move_dist):
        super(Wolf, self).__init__(0, 0, wolf_move_dist)

    def calculate_dist(self, sheep):
        return math.sqrt((self.x - sheep.x) ** 2 + (self.y - sheep.y) ** 2)

    def find_nearest_sheep(self, sheeps):
        smallest_distance = sys.float_info.max
        nearest_sheep = -1
        for i in range(len(sheeps)):
            temp_dist = self.calculate_dist(sheeps[i])
            if sheeps[i].alive and temp_dist < smallest_distance:
                smallest_distance = temp_dist
                nearest_sheep = i
        return nearest_sheep, smallest_distance

    def move_wolf(self, sheeps):
        victim_i, distance = self.find_nearest_sheep(sheeps)
        if distance < self.move_dist:
            sheeps[victim_i].die()
            self.move(sheeps[victim_i].x, sheeps[victim_i].y)
            return victim_i
        else:
            new_x = self.x + (sheeps[victim_i].x - self.x) * self.move_dist / distance
            new_y = self.y + (sheeps[victim_i].y - self.y) * self.move_dist / distance
            self.move(new_x, new_y)
            return -1

    def __str__(self):
        return "Wolf: " + super(Wolf, self).__str__()
