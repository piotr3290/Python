import json
import csv
import os
import configparser
import logging
from chase.Wolf import Wolf
from chase.Sheep import Sheep


class Simulation(object):

    def __init__(self, args=None, round_numbers=50, sheeps_amount=15, init_pos_limit=10.0, sheep_move_dist=0.5,
                 wolf_move_dist=1.0):
        self.__args = args
        """if self.__args.file:
            try:
                config = configparser.ConfigParser()
                config.read(self.__args.file)
                init_pos_limit = float(config['Terrain']['InitPosLimit'])
                sheep_move_dist = float(config['Movement']['SheepMoveDist'])
                wolf_move_dist = float(config['Movement']['WolfMoveDist'])
            except KeyError:
                raise ArgumentError("Wrong configure file")"""

        """self.__round_numbers = self.__args.rounds_num if self.__args.rounds_num else round_numbers
        self.__sheeps_amount = self.__args.sheeps_num if self.__args.sheeps_num else sheeps_amount"""
        self.__round_numbers = round_numbers
        self.__sheeps_amount = sheeps_amount

        if self.__round_numbers <= 0 or self.__sheeps_amount < 0 or init_pos_limit <= 0 or sheep_move_dist <= 0 \
                or wolf_move_dist <= 0:
            raise ArgumentError("Argument must be positive number")

        self.__sheeps = [Sheep(sheep_move_dist, init_pos_limit) for i in range(sheeps_amount)]
        self.__wolf = Wolf(wolf_move_dist)
        self.__alives_amount = sheeps_amount
        self.__sheep_move_dist = sheep_move_dist
        self.__no_round = 0

    def simulate(self):
        #  self.json_data = [self.get_dict_sim(0)]
        """self.csv_data = [[0, self.__alives_amount]]"""
        # for i in range(self.__round_numbers):

        for sheep in self.__sheeps:
            sheep.move_sheep()

        victim_i = self.__wolf.move_wolf(self.__sheeps)
        # print(self.wolf)

        # devouring_str = ""
        if victim_i != -1:
            self.__alives_amount -= 1
            devouring_str = " Sheep " + str(victim_i) + " has been devoured"
            # logging.info(devouring_str)
        self.__no_round += 1

        # self.json_data.append(self.get_dict_sim(self.__no_round + 1))
        """self.csv_data.append([self.__no_round + 1, self.__alives_amount])

        self.show_sim_info(self.__no_round + 1, devouring_str)
        if not self.__alives_amount:
            break
        if self.__args.wait:
            input("Press key to continue")
        self.save_to_json(self.json_data)
        self.save_to_csv(self.csv_data)
        logging.debug("Function name: simulate")"""
        # self.save_to_json(self.json_data)

    def show_sim_info(self, round_number, devouring_str):
        print("Round:", round_number, self.__wolf, " alives amount:", self.__alives_amount, devouring_str)
        logging.debug(
            f"Function name: show_sim_info, arguments: round_number = {round_number} devouring_str = {devouring_str}")

    def get_dict_sim(self):
        sheep_pos = []
        for sheep in self.__sheeps:
            sheep_pos.append({"x": sheep.get_x(), "y": sheep.get_y(), "alive": sheep.get_alive()})

        result = {
            "wolf": {"x": self.__wolf.get_x(), "y": self.__wolf.get_y()},
            "sheeps": sheep_pos
        }

        return result

    def save_to_json(self, file):
        with open(file, 'w') as json_file:
            json.dump(self.get_dict_sim(), json_file, indent=2)

    def read_from_json(self, file):

        with open(file, 'r') as json_file:
            data = json.load(json_file)
            self.set_sheeps(data["sheeps"])
            self.set_wolf(data["wolf"])

    def save_to_csv(self, csv_data):
        file = 'alive.csv'
        if self.__args.dir:
            os.makedirs(self.__args.dir, exist_ok=True)
            file = self.__args.dir + '/' + file
        with open(file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            for row in csv_data:
                csv_writer.writerow(row)

    def add_sheep(self, x, y):
        self.__sheeps.append(Sheep(self.__sheep_move_dist, x, y))
        self.__alives_amount += 1

    def get_sheeps(self):
        return self.__sheeps

    def set_wolf_position(self, x, y):
        self.__wolf.move(x, y)

    def get_wolf(self):
        return self.__wolf

    def get_alive_amount(self):
        return self.__alives_amount

    def set_sheeps(self, sheeps_data):
        for sheep_data in sheeps_data:
            sheep = Sheep(self.__sheep_move_dist, sheep_data["x"], sheep_data["y"])
            if not sheep_data["alive"]:
                sheep.die()
            self.__sheeps.append(sheep)

    def set_wolf(self, wolf_data):
        self.__wolf.move(wolf_data['x'], wolf_data["y"])


class ArgumentError(Exception):
    def __init__(self, message):
        logging.error(message)
        super(ArgumentError, self).__init__(message)
