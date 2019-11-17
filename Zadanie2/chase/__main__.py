import json
import csv
import argparse
import os
import configparser
from chase.Wolf import Wolf
from chase.Sheep import Sheep

parser = argparse.ArgumentParser(
    description='Testowy opis: '
)

parser.add_argument('-c', '--config', action="store", dest='file', help='choose optional configure file')
parser.add_argument('-r', '--rounds', action="store", dest='rounds_num', help='simulation amount of rounds', type=int)
parser.add_argument('-s', '--sheep', action="store", dest='sheeps_num', help='simulation amount of sheeps', type=int)
parser.add_argument('-w', '--wait', action="store_true", dest='wait', help='programme wait after every round',
                    default=False)
parser.add_argument('-d', '--dir', action="store", dest='dir', help='directory file')
args = parser.parse_args()


class Simulation(object):

    def __init__(self, round_numbers=50, sheeps_amount=15, init_pos_limit=10.0, sheep_move_dist=0.5,
                 wolf_move_dist=1.0):

        if args.file:
            try:
                config = configparser.ConfigParser()
                config.read(args.file)
                init_pos_limit = float(config['Terrain']['InitPosLimit'])
                sheep_move_dist = float(config['Movement']['SheepMoveDist'])
                wolf_move_dist = float(config['Movement']['WolfMoveDist'])
            except KeyError:
                raise ArgumentError("Wrong configure file")

        self.round_numbers = args.rounds_num if args.rounds_num else round_numbers
        self.sheeps_amount = args.sheeps_num if args.sheeps_num else sheeps_amount

        if self.round_numbers <= 0 or self.sheeps_amount <= 0 or init_pos_limit <= 0 or sheep_move_dist <= 0 \
                or wolf_move_dist <= 0:
            raise ArgumentError("Argument must be positive number")

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


class ArgumentError(Exception):
    pass


if __name__ == "__main__":
    print("hej")
    sim = Simulation()
    sim.simulate()
    """for _ in range(20):
        print("x = ", owieczka.x, " y = ", owieczka.y)
        owieczka.move_sheep()"""
