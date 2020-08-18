import numpy as np
from ttt.tictactoe_model import TicTacToeModel
from ttt.qlearn.agent import Agent
from ttt.encoding.encoder import encode3

w = 3
h = 3
win_size = 3
player_size = 2
states_size = player_size**(w*h)
actions_size = w*h

model = TicTacToeModel(w, h, win_size)
agents = [Agent(states_size, actions_size) for i in range(player_size)]

def get_available_acts():
    t = np.array([w, 1])
    a = np.argwhere(model.fields == 0)
    return a.dot(t)



parties = 10
for party in range(parties):
    state = encode3(model.fields)
    acts = get_available_acts()
    act = agent1.act(state, acts)
    model.act()

