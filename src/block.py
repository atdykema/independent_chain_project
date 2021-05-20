import time


class Block:
    def __init__(self, prev_hash, transactions, message):
        self.prev_hash = prev_hash
        self.transactions = transactions

    def get_prev_hash(self):
        return self.prev_hash

    def get_transactions(self):
        return self.transactions

    def get_message(self):
        return self.message
