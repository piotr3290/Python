import logging
import logging.config


class Creature(object):
    def __init__(self, x, y, move_dist):
        self._x, self._y, self._move_dist = x, y, move_dist

    def move(self, x, y):
        self._x, self._y = x, y
        logging.debug(f"Function name: move, arguments: x = {x}, y: {y}")

    def get_x(self):
        # logging.debug(f"Function name: get_x, returns: x = {self._x}")
        return self._x

    def get_y(self):
        # logging.debug(f"Function name: get_y, returns: y = {self._y}")
        return self._y

    def get_move_dist(self):
        # logging.debug(f"Function name: get_move_dist, returns: move_dist = {self._move_dist}")
        return self._move_dist

    def __str__(self):
        return "x = " + str(round(self._x, 3)) + " y = " + str(round(self._y, 3))
