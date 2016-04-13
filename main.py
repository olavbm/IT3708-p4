from multiprocessing import Process

import ea
import getopt
import sys
import visualization

from communication import Shared

def coproc(target, *args):
    Process(target=target, args=args).start()

def main():
    run_type = 'standard'

    options, args = getopt.getopt(sys.argv[1:],"t:")
    for opt, arg in options:
        if opt == '-t':
            run_type = arg
        else:
            print("Usage: %s -t run_type" % sys.argv[0])

    # There can only be one ubernisse.

    current_generation = Shared()
    coproc(visualization.loop, current_generation)

    for generation in ea.run(run_type):
        print(generation)
        current_generation.put(generation)

if __name__ == '__main__':
    main()
