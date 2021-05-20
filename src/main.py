from hashlib import sha256
from coinbase import *
from block import *
from wallet import *


def main():
    #create coinbase
    coinbase = Coinbase()
    print(f"{coinbase.get_reward_available()}" + " " + f"{coinbase.get_genesis_date()}")

    #create genesis block
    genesis_block = Block(123, 123, "genesis block")
    print(f"{genesis_block.get_prev_hash()}" + " " + f"{genesis_block.get_transactions()}")

    #create wallet
    wallet = Wallet()





if __name__ == "__main__":
    main()
