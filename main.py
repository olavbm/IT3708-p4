from multiprocessing import Process

import ea
import visualization

from communication import Shared

def coproc(target, *args):
    Process(target=target, args=args).start()

def main():

    # There can only be one ubernisse.

    current_generation = Shared()
    coproc(visualization.loop, current_generation)

    for generation in ea.run():
        print(generation)
        current_generation.put(generation)

if __name__ == '__main__':
    main()
