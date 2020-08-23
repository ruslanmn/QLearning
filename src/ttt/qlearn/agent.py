import numpy as np
from numpy import random

epsilon = 0.2
lr = 0.8
gamma = 0.5


class Agent:
    def __init__(self, states, actions):
        self.q = np.zeros((states, actions))

    # available_actions should be sorted asc
    def act(self, state, available_actions):
        if random.uniform(0, 1) < epsilon:
            return random.choice(available_actions)
        else:
            ind = np.argmax(self.q[state, available_actions])
            return available_actions[ind]

    def update(self, state, action, new_state, reward):
        max_next_reward = np.max(self.q[new_state, :])
        self.q[state, action] += lr * (reward + gamma * max_next_reward - self.q[state, action])
