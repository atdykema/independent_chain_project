import time


class Wallet:
    def __init__(self, label):
        self.label = label
        self.timestamp = time.time()
        self.addresses = []

