import random
import math
import sys
import json
import csv
import argparse
import os
import logging
import configparser
import msvcrt as m

parser = argparse.ArgumentParser(
    description='Testowy opis: '
)

parser.add_argument('-c', '--config', action="store", dest='file', help='choose optional configure file')
parser.add_argument('-r', '--rounds', action="store", dest='rounds_num', help='simulation amount of rounds', type=int)
parser.add_argument('-s', '--sheep', action="store", dest='sheeps_num', help='simulation amount of sheeps', type=int)
parser.add_argument('-w', '--wait', action="store_true", dest='wait', help='programme wait after every round',
                    default=False)
parser.add_argument('-d', '--dir', action="store", dest='dir', help='directory file')
# parser.add_argument('-h', '--help', action="store_true", dest='help', default=False)
args = parser.parse_args()


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

    def __init__(self, round_numbers=50, sheeps_amount=15, init_pos_limit=10.0, sheep_move_dist=0.5,
                 wolf_move_dist=1.0):

        if args.file:
            config = configparser.ConfigParser()
            config.read(args.file)
            init_pos_limit = float(config['Terrain']['InitPosLimit'])
            sheep_move_dist = float(config['Movement']['SheepMoveDist'])
            wolf_move_dist = float(config['Movement']['WolfMoveDist'])

        self.round_numbers = args.rounds_num if args.rounds_num else round_numbers
        self.sheeps_amount = args.sheeps_num if args.sheeps_num else sheeps_amount
        self.sheeps = [Sheep(sheep_move_dist, init_pos_limit) for i in range(sheeps_amount)]
        self.wolf = Wolf(wolf_move_dist)
        self.alives_amount = sheeps_amount

    def simulate(self):
        json_data = [self.get_dict_sim(0)]
        csv_data = [[0, self.alives_amount]]
        for i in range(self.round_numbers):
            # print("Round: ", i + 1)
            for sheep in self.sheeps:
                sheep.move_sheep()
                # print(sheep)

            victim_i = self.wolf.move_wolf(self.sheeps)
            # print(self.wolf)

            if victim_i != -1:
                self.alives_amount -= 1

            json_data.append(self.get_dict_sim(i + 1))
            csv_data.append([i + 1, self.alives_amount])
            # print("Sheep ", victim_i, " has been devoured")

            if self.alives_amount == 0:
                break
            if args.wait:
                input("Press key to continue")
                # os.system("pause")

        self.save_to_json(json_data)
        self.save_to_csv(csv_data)

    def get_dict_sim(self, round_no):
        sheep_pos = []
        for sheep in self.sheeps:
            if sheep.alive:
                sheep_pos.append([round(sheep.x, 3), round(sheep.y, 3)])
            else:
                sheep_pos.append(None)

        return {
            "round_no": round_no,
            "wolf_pos": [round(self.wolf.x, 3), round(self.wolf.y, 3)],
            "sheep_pos": sheep_pos
        }

    def save_to_json(self, json_data):
        file = 'pos.json'
        if args.dir:
            os.makedirs(args.dir, exist_ok=True)
            file = args.dir + '/' + file
        with open(file, 'w') as json_file:
            json.dump(json_data, json_file, indent=2)

    def save_to_csv(self, csv_data):
        file = 'alive.csv'
        if args.dir:
            os.makedirs(args.dir, exist_ok=True)
            file = args.dir + '/' + file
        with open(file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            for row in csv_data:
                csv_writer.writerow(row)


if __name__ == "__main__":
    owieczka = Sheep(3, 100)
    sim = Simulation()
    sim.simulate()
    """for _ in range(20):
        print("x = ", owieczka.x, " y = ", owieczka.y)
        owieczka.move_sheep()"""