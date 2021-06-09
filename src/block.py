import time
from hashlib import sha256


def find_block(identifier, most_recent_block):
    block = most_recent_block
    while block.block_hash != identifier:
        block = block.prev_block
        if block is None:
            print("block not found")
            return 1
    return block


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
        # self.difficulty =
        self.prev_block = prev_block
        if prev_block is not None:
            self.block_height = prev_block.block_height + 1
            self.prev_hash = prev_block.hash
        else:
            self.prev_hash = 0x0000000000000000000000000000000000000000000000000000000000000000
            self.block_height = 0
        # block merkle_hash, hash, and nonce are all determined after
        # addition of tcs and the confirmation of the block

        # self.merkle_hash = None
        # self.hash = None
        # self.nonce = None
        self.txs = []

