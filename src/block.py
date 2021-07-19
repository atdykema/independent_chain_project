import time


def find_block(identifier, genesis_block):
    block = genesis_block
    while block.block_hash != identifier:
        block = block.next_block
        if block is None:
            print("block not found")
            return 1
    return block


def find_block_at_height(height, genesis_block):
    block = genesis_block
    while block.block_height != height:
        block = block.next_block
    return block


def find_most_recent_block(genesis_block):
    block = genesis_block
    while block.next_block is not None:
        block = block.next_block
    return block


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

