from multiprocessing import Process
from src.coinbase import Coinbase
from src.block import Block
from src.command_line import start_command_line
from src.command_line import touch_wallet, touch_tx, touch_address, get_wallets, get_addresses
from src.mining import start_mining



def main():
    # initialize wallet list
    wallets = []

    # initiate genesis block
    genesis_block = Block(None)

    # initiate coinbase
    coinbase = Coinbase()

    # start command line
    touch_wallet(wallets)
    touch_wallet(wallets)
    touch_wallet(wallets)
    touch_address(wallets)
    touch_address(wallets)
    print("--Wallets--")
    get_wallets(wallets)
    print("--Addresses--")
    get_addresses(wallets)

    Process(target=start_mining(genesis_block))

    start_command_line(wallets, genesis_block, coinbase)





if __name__ == "__main__":
    main()
