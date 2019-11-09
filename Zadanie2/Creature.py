import random
import math
import sys


class Creature(object):
    def __init__(self, x, y, move_dist):
        self.x, self.y, self.move_dist = x, y, move_dist

    def move(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "x = " + str(self.x) + " y = " + str(self.y)


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


class Simulation(object):

    def __init__(self, init_pos_limit, round_numbers, sheeps_amount, sheep_move_dist, wolf_move_dist):
        self.sheeps = [Sheep(sheep_move_dist, init_pos_limit) for i in range(sheeps_amount)]
        self.wolf = Wolf(wolf_move_dist)
        self.round_numbers = round_numbers
        self.alives_amount = sheeps_amount

    def simulate(self):

        for i in range(self.round_numbers):
            print("Round: ", i + 1)
            for sheep in self.sheeps:
                sheep.move_sheep()
                print(sheep)

            victim_i = self.wolf.move_wolf(self.sheeps)
            print(self.wolf)
            if victim_i != -1:
                self.alives_amount -= 1
                print("Sheep ", victim_i, " has been devoured")

            if self.alives_amount == 0:
                break


if __name__ == "__main__":
    owieczka = Sheep(3, 100)

    sim = Simulation(10, 50, 15, 0.5, 1.0)
    sim.simulate()
    """for _ in range(20):
        print("x = ", owieczka.x, " y = ", owieczka.y)
        owieczka.move_sheep()"""
