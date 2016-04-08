from time import sleep

import flatland
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
    board = generation.board

    for _ in range(generation.timesteps):
        stim = flatland.sensor_cells(board)
        output = nn.act_on_input(stim)
        board, _ = flatland.modify_on_action(board, output)
        yield board
