from chase.Creature import Creature
import random
import logging
import logging.config


class Sheep(Creature):
    __alive = True

    def __init__(self, sheep_move_dist, init_pos_limit):
        super(Sheep, self).__init__(random.uniform(-init_pos_limit, init_pos_limit),
                                    random.uniform(-init_pos_limit, init_pos_limit),
                                    sheep_move_dist)

    def rand_direction(self):
        switcher = {
            1: [0, 1],  # North
            2: [1, 0],  # East
            3: [0, -1],  # South
            4: [-1, 0]  # West
        }
        result = switcher.get(random.randint(1, 4))
        logging.debug(f"Function name: rand_direction, returns: randint = {result}")
        return result

    def move_sheep(self):
        if self.__alive:
            direction = self.rand_direction()
            new_x = self._x + self._move_dist * direction[0]
            new_y = self._y + self._move_dist * direction[1]
            self.move(new_x, new_y)
            logging.info(
                f"Sheep moves from: {self._x, self._y} to: {new_x, new_y}")
        logging.debug(f"Function name: move_sheep")

    def die(self):
        self.__alive = False
        logging.debug(f"Function name: die")

    def get_alive(self):
        logging.debug(f"Function name: get_alive, returns: alive = {self.__alive}")
        return self.__alive

    def __str__(self):
        return "x = " + str(self._x) + " y = " + str(self._y) + " alive = " + str(self.__alive)
