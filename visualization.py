from time import sleep

import beerworld
import graphics
import neuralnet

NeuralNet = neuralnet.make_CTRNN()

def loop(current_generation):
    painter = graphics.Painter()
    while True:
        generation = current_generation.get()
        print("START")
        for i, step in enumerate(simulate(generation)):
            painter.draw_board_from_matrix(step)
            sleep(0.05)
            if i > 50:
                break

def simulate(generation):
    nn = NeuralNet(generation.best_parameters)
    beer = beerworld.Beer()

    for _ in range(generation.timesteps):
        stim = beer.sensor_cells()
        output = nn.act_on_input(stim)
        output = round((output[0] - output[1]) * 8.0 - 4.0)
        beer.modify_on_action(output)
        yield beer.board
