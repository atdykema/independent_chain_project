# FIX IMPORTS DUE TO CIRCULAR IMPORTS
from src.coinbase import Coinbase
from src.block import Block
from src.command_line import start_command_line
from src.mining import start_mining
import multiprocessing as mp


def main():
    # initialize wallet list
    wallets = []

    # initiate genesis block
    genesis_block = Block(None)

    # initiate coinbase
    coinbase = Coinbase()

    # initiate mining
    mining = mp.Process(target=start_mining)

    # start command line
    status = start_command_line()


if __name__ == "__main__":
    main()
