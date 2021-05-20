import time


class Coinbase:
    def __init__(self):
        self.reward_available = 1000000
        self.genesis_date = time.time()

    def get_reward_available(self):
        return self.reward_available

    def get_genesis_date(self):
        return self.genesis_date
