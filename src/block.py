import time
from hashlib import sha256


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


def print_blockchain(genesis_block):
    block = genesis_block
    while block.next_block is not None:
        print(block.block_height)
        block = block.next_block


def get_hash_merkle_root(transactions):
    tx = transactions.copy()
    if len(tx) == 0:
        return []
    temp = []
    while len(tx) > 1:
        concat = tx[len(tx)-1] + tx[len(tx)-2]
        curr_hash = sha256(concat.encode('utf-8')).hexdigest()
        temp.append(curr_hash)
        del tx[len(tx) - 1]
        del tx[len(tx) - 1]
    if len(tx) == 1:
        tx.append(tx[0])
        concat = tx[0] + tx[1]
        curr_hash = sha256(concat.encode('utf-8')).hexdigest()
        temp.append(curr_hash)
        del tx[len(tx) - 1]
        del tx[len(tx) - 1]
    if len(temp) == 1:
        return temp[0]
    else:
        hash_ = get_hash_merkle_root(temp)
        return hash_


class Block:
    def __init__(self, prev_block):
        self.timestamp = time.time()
        self.block_height = None
        self.prev_hash = None
        self.block_hash = None
        self.difficulty = None
        self.target = None
        self.next_block = None
        self.prev_block = prev_block
        
        # block merkle_hash, hash, and nonce are all determined after addition of txs and the confirmation of the block

        self.merkle_hash = None
        self.hash = None
        self.nonce = None

        self.txs = []

