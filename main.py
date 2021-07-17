from src.coinbase import Coinbase
from src.block import Block
from src.command_line import start_command_line
from src.mining import start_mining, structure_new_block
from multiprocessing import Process
import sys
import os


def main():
    # initialize wallet list
    wallets = []

    # initiate genesis block
    genesis_block = structure_new_block(None)

    # initiate coinbase
    coinbase = Coinbase()

    # initiate mining
    mining = Process(target=start_mining, args=(genesis_block,))
    mining.start()
   
    #start_command_line(wallets, genesis_block, coinbase)


if __name__ == "__main__":
    main()
