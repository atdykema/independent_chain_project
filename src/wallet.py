import time, random, tools.tools, os, hashlib, binascii
from pbkdf2 import PBKDF2
import src.tx as tx
import src.main as m


def find_wallet(identifier):
    for wallet in m.wallets:
        if wallet.label == identifier:
            return wallet
    return 1


class Wallet:
    def __init__(self, label):
        self.label = label
        self.addresses = []

