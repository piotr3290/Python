import argparse
from chase.Simulation import Simulation
import logging.config


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Python zadanie 2: '
    )

    parser.add_argument('-c', '--config', action="store", dest='file', help='choose optional configure file')
    parser.add_argument('-r', '--rounds', action="store", dest='rounds_num', help='simulation amount of rounds',
                        type=int)
    parser.add_argument('-s', '--sheep', action="store", dest='sheeps_num', help='simulation amount of sheeps',
                        type=int)
    parser.add_argument('-w', '--wait', action="store_true", dest='wait', help='programme wait after every round',
                        default=False)
    parser.add_argument('-d', '--dir', action="store", dest='dir', help='directory file')
    parser.add_argument('-l', '--log', action="store", dest='level', help='Set logs level')
    args = parser.parse_args()

    level = 60 if not args.level else int(args.level)
    file = ""
    if args.level:
        file = "chase.log"
        if args.dir:
            file = args.dir + '/' + file
    logging.basicConfig(level=level, filename=file, filemode='w')

    sim = Simulation(args)
    sim.simulate()
