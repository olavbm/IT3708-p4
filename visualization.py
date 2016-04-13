from time import sleep

import beerworld
import graphics
import neuron

def loop(current_generation):
    painter = graphics.Painter()
    while True:
        generation = current_generation.get()
        for step in simulate(generation):
            painter.draw_board_from_matrix(step)
            sleep(0.2)

def simulate(generation):
    nn = neuron.Neural_net(generation.best_weights)
    beer = beerworld.Beer()

    for _ in range(generation.timesteps):
        stim = beer.sensor_cells()
        output = nn.act_on_input(stim)
        beer.modify_on_action(output)
        yield beer.board
