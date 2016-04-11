from multiprocessing import Process

import ea
import getopt
import sys
import visualization

from communication import Shared

def coproc(target, *args):
    Process(target=target, args=args).start()

def main():
    run_type = 'static'
    num_boards = 1

    options, args = getopt.getopt(sys.argv[1:],"t:n:")
    for opt, arg in options:
        if opt == '-t':
            run_type = arg
        elif opt == '-n':
            num_boards = int(arg)
        else:
            print("Usage: %s -t run_type -n num_board" % sys.argv[0])

    # There can only be one ubernisse.

    current_generation = Shared()
    coproc(visualization.loop, current_generation)

    for generation in ea.run(run_type, num_boards):
        print(generation)
        current_generation.put(generation)

if __name__ == '__main__':
    main()
