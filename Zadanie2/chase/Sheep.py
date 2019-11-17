from chase.Creature import Creature
import random


class Sheep(Creature):
    alive = True

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
        return switcher.get(random.randint(1, 4))

    def move_sheep(self):
        if self.alive:
            direction = self.rand_direction()
            self.move(self.x + self.move_dist * direction[0],
                      self.y + self.move_dist * direction[1])

    def die(self):
        self.alive = False

    def __str__(self):
        return "x = " + str(self.x) + " y = " + str(self.y) + " alive = " + str(self.alive)
