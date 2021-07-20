import time


class Block:
    def __init__(self, prev_block):
        self.timestamp = time.time()
        self.block_height = None
        self.prev_hash = None
        self.difficulty = None
        self.target = None
        self.next_block = None
        self.prev_block = prev_block

        self.hash_merkle_root = None
        self.hash = None
        self.nonce = None

        self.txs = []

