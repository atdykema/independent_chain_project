import time

COINBASE_ADDRESS = 'Coinbase'


def get_coinbase_block_reward(most_recent_block):
    REWARD_DROPOFF_BLOCK = 100
    ORIG_REWARD = 50

    return ORIG_REWARD * (.5 ** most_recent_block.block_height / REWARD_DROPOFF_BLOCK)


class Coinbase:
    def __init__(self):
        self.reward_available = 21000000
        self.genesis_date = time.time()

