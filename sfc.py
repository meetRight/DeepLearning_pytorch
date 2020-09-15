import math
import numpy as np


class ServiceChainEnv(object):
    def __init__(self):
        self.action = np.arange(8)
        # self.action_space = self.action.shape[0]
        self.node_capacity = 100 * np.ones( 16)
        self.bandwidth = 500 * np.ones(15)
        self.vnf = 25 * np.ones(10)
        # self.process_delay = np.random.randint(0, 10, size=(1, 7))
        self.process_delay = np.array([1, 5, 6, 2, 4, 3, 2, 1])
        self.state = None
        # self.seed()
        # self.viewer = None

    def reset(self):
        self.state = np.hstack((self.node_capacity, self.bandwidth))
        return self.state

    def step(self, action, count):
        state = self.state
        vnf = self.vnf
        state[action * 2] = state[action * 2] - vnf[count * 2]
        state[action * 2 + 1] = state[action * 2 + 1] - vnf[count * 2 + 1]
        self.state = state

        reward = self.process_delay[action]

        done = count % 5 == 4
        done = bool(done)

        return self.state, reward, done, {}

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None







