import numpy as np
from numpy import random

epsilon = 0.5
lr = 0.8
gamma = 0.5


class Agent:
    def __init__(self, states, actions):
        self.q = np.zeros((states, actions))
        self.last_state = None
        self.last_act = None

    # available_actions should be sorted asc
    def act(self, state, available_actions):
        if random.uniform(0, 1) < epsilon:
            act = random.choice(available_actions)
        else:
            ind = np.argmax(self.q[state, available_actions])
            act = available_actions[ind]
        self.last_state = state
        self.last_act = act
        return act

    def play(self, state, available_actions):
        ind = np.argmax(self.q[state, available_actions])
        act = available_actions[ind]
        return act

    def update(self, state, action, new_state, reward):
        max_next_reward = np.max(self.q[new_state, :])
        self.q[state, action] += lr * (reward + gamma * max_next_reward - self.q[state, action])

    def update_last(self, new_state, reward):
        if self.last_act and self.last_state:
            self.update(self.last_state, self.last_act, new_state, reward)

    def load(self, file):
        self.q = np.load(file)

    def save(self, file):
        np.save(file, self.q)
