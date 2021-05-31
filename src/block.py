import time
from hashlib import sha256


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
    def __init__(self, prev_hash, nonce):
        self.prev_hash = prev_hash
        #self.merkle_hash = get_hash_merkle_root()
        self.timestamp = time.time()
        self.nonce = nonce
        self.txs = []

    def add_tx(self, tx):
        self.txs.append(tx)

    def get_txs(self):
        self.txs

    def get_prev_hash(self):
        return self.prev_hash

    def get_merkle_hash(self):
        return self.merkle_hash

    def get_timestamp(self):
        return self.timestamp

    def get_nonce(self):
        return self.nonce

    #def get_transactions(self):
        #return self.transactions

