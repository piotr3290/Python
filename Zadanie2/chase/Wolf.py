from chase.Creature import Creature
import math
import sys
import logging
import logging.config


class Wolf(Creature):
    def __init__(self, wolf_move_dist):
        super(Wolf, self).__init__(0, 0, wolf_move_dist)

    def calculate_dist(self, sheep):
        result = math.sqrt((self._x - sheep.get_x()) ** 2 + (self._y - sheep.get_y()) ** 2)
        logging.debug(f"Function name: calculate_dist, returns: randint = {result}")
        return result

    def find_nearest_sheep(self, sheeps):
        smallest_distance = sys.float_info.max
        nearest_sheep = -1
        for i in range(len(sheeps)):
            temp_dist = self.calculate_dist(sheeps[i])
            if sheeps[i].get_alive() and temp_dist < smallest_distance:
                smallest_distance = temp_dist
                nearest_sheep = i
        logging.debug(
            f"Function name: find_nearest_sheep, arguments: sheeps returns: smallest_distance = {smallest_distance} nearest sheep = {nearest_sheep}")

        return nearest_sheep, smallest_distance

    def move_wolf(self, sheeps):
        victim_i, distance = self.find_nearest_sheep(sheeps)
        if distance < self._move_dist:
            sheeps[victim_i].die()
            self.move(sheeps[victim_i].get_x(), sheeps[victim_i].get_y())
            logging.info(
                f"Wolfs move from: {self._x, self._y} to: {sheeps[victim_i].get_x(), sheeps[victim_i].get_y()}")
            index = victim_i
        else:
            new_x = self._x + (sheeps[victim_i].get_x() - self._x) * self._move_dist / distance
            new_y = self._y + (sheeps[victim_i].get_y() - self._y) * self._move_dist / distance
            self.move(new_x, new_y)
            logging.info(
                f"Wolf moves from: {self._x, self._y} to: {new_x, new_y}")

            index = -1
        logging.debug(f"Function name: move_wolf, arguments: sheeps returns: index = {index}")
        return index

    def __str__(self):
        return "Wolf: " + super(Wolf, self).__str__()
