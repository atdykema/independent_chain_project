from src.coinbase import Coinbase
from src.block import Block
from src.command_line import start_command_line
from src.mining import start_mining
from multiprocessing import Process
import sys
import os


def main():
    # initialize wallet list
    wallets = []

    # initiate genesis block
    genesis_block = Block(None)

    # initiate coinbase
    coinbase = Coinbase()

    # initiate mining
    p1 = Process(target=start_mining(genesis_block))
    p1.start()
    # start command line
    p2 = Process(target=start_command_line(wallets, genesis_block, coinbase))
    p2.start()


if __name__ == "__main__":
    main()
