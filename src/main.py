from hashlib import sha256
from coinbase import *
from block import *



def main():
    #create coinbase
    coinbase = Coinbase()
    print(f"{coinbase.get_reward_available()}" + " " + f"{coinbase.get_genesis_date()}")

    #create genesis block
    genesis_block = Block(123, 123)
    print(f"{genesis_block.get_prev_hash()}" + " " + f"{genesis_block.get_transactions()}")

    #start mining





if __name__ == "__main__":
    main()
