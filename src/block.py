import time
from hashlib import sha256
import src.main as m


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


def find_block(identifier):
    block = m.most_recent_block
    while block.block_hash != identifier:
        block = block.prev_block
        if block is None:
            print("block not found")
            return 1
    return block


class Block:
    def __init__(self, prev_block):
        self.timestamp = time.time()
        self.block_height = find_block(self.prev_hash).block_number + 1
        #self.difficulty =
        self.prev_block = prev_block
        self.prev_hash = prev_block.hash
        #self.merkle_hash = None
        #self.hash =
        #self.nonce =
        self.txs = []


