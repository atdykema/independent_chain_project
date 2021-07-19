import multiprocessing
from multiprocessing.queues import Queue
from src.coinbase import Coinbase
from src.block import Block
from src.command_line import start_command_line
from src.mining import start_mining, structure_new_block
from multiprocessing import Process, Queue
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
    to_cl_queue = Queue()
    to_mine_queue = Queue()
    mining = Process(target=start_mining, args=(genesis_block, to_cl_queue, to_mine_queue,))
    mining.start()
   
    start_command_line(wallets, genesis_block, coinbase, to_cl_queue, to_mine_queue)


if __name__ == "__main__":
    main()
