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

    wallet = Wallet("default")
    # while True:
    #     command = input()
    #     #create wallet
    #     if command == "touch wallet" or "touch w":
    #         label_input = input("Label (leave blank for default)")
    #         if label_input == '':
    #             label = "default"
    #         else:
    #             label = label_input
    #         wallet = Wallet(label)





if __name__ == "__main__":
    main()
