import numpy as np

from ttt.tictactoe_ai.utils import action_to_field, get_available_acts
from ttt.tictactoe_model import TicTacToeModel
from ttt.qlearn.agent import Agent
from ttt.encoding.encoder import encode

LOAD = False
FILEMASK = 'agent_%d.npy'

REWARD = 10
W = 3   
H = 3
WIN_SIZE = 3
PLAYERS_SIZE = 2
GAMES = 500000

states_size = (PLAYERS_SIZE + 1) ** (W * H)
actions_size = W * H

def init_agent(file = None):
    agent = Agent(states_size, actions_size)
    if file:
        agent.load(file)
    return agent


def load_agents():
    return [init_agent(FILEMASK % i) for i in range(PLAYERS_SIZE)]


def update_win_rewards(agents, new_state, win_agent):
    for i in range(len(agents)):
        reward = REWARD if i == win_agent else -REWARD
        agents[i].update_last(new_state, reward)


def update_rewards(agents, new_state):
    for agent in agents:
        agent.update_last(new_state, 0)


def train_agents():
    model = TicTacToeModel(W, H, WIN_SIZE)
    if LOAD:
        agents = load_agents()
    else:
        agents = [init_agent() for i in range(PLAYERS_SIZE)]

    for game in range(GAMES):
        print('Simulating game #%d' % game)
        res = 0
        model.reset()
        while not res:
            for i in range(len(agents)):
                agent = agents[i]
                state = encode(model.fields, PLAYERS_SIZE + 1)
                acts = get_available_acts(model)
                act = agent.act(state, acts)
                x, y = action_to_field(act, W)
                res = model.act(x, y)
                if res == -1:
                    raise Exception('Agent act is unavailable')
                # draw
                elif res == 2:
                    win_agent = -1
                    break
                # player won
                elif res == 1:
                    win_agent = i
                    break
            new_state = encode(model.fields, PLAYERS_SIZE + 1)
            if res == 1:
                update_win_rewards(agents, new_state, win_agent)
            else:
                update_rewards(agents, new_state)

    for i in range(len(agents)):
        agents[i].save(FILEMASK % i)


if __name__ == "__main__":
    train_agents()
