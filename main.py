from multiprocessing.queues import Queue
from src.coinbase import Coinbase
from tools.tools import find_most_recent_block, find_block_at_height
from src.command_line import update_blockchain, touch_address, touch_wallet, touch_tx, describe_blockchain, describe_wallet, get_addresses, get_wallets
from src.mining import start_mining, structure_new_block
from multiprocessing import Process, Queue
from tools.testfile import test_attributes
import sys
import os


def main():
    # initialize wallet list
    wallets = []

    # test additions
    test_attributes(wallets)

    # initiate genesis block
    genesis_block = structure_new_block(None)

    # initiate coinbase
    coinbase = Coinbase()

    # initiate mining
    to_cl_queue = Queue()
    to_mine_queue = Queue()
    mining = Process(target=start_mining, args=(genesis_block, to_cl_queue, to_mine_queue,))
    mining.start()
   
    while True:

        c = input().split()

        update_blockchain(genesis_block, to_cl_queue)

        if len(c) == 0:
            continue


        elif c[0] in ("help", "h"):
            print("Commands:")
            print("\ttouch")
            print("\t\twallet, w")
            print("\t\ttx, t")
            print("\t\taddress, a")
            print("\tget")
            print("\t\twallets, w")
            print("\t\taddresses, a")
            print("\tdescribe")
            print("\t\twallet, w")
            print("\t\tmrb")


        elif c[0] in ("touch", "t"):
            if len(c) == 1:
                print("invalid command")
                pass
            elif c[1] in ("wallet", "w"):
                if len(c) == 3:
                    touch_wallet(wallets, c[2])
            elif c[1] in ("tx", "t"):
                if len(c) < 3:
                    touch_tx(wallets, to_mine_queue)
                elif len(c) == 3:
                    touch_tx(wallets, to_mine_queue, c[2])
                elif len(c) == 4:
                    touch_tx(wallets, to_mine_queue, c[2], c[3])
                elif len(c) == 5:
                    touch_tx(wallets, to_mine_queue, c[2], c[3], c[4])
                elif len(c) == 6:
                    touch_tx(wallets, to_mine_queue, c[2], c[3], c[4], c[5])
                elif len(c) == 7:
                    touch_tx(wallets, to_mine_queue, c[2], c[3], c[4], c[5], c[6])
                else:
                    touch_tx(wallets, to_mine_queue)
            elif c[1] in ("address", "a"):
                if len(c) == 3:
                    touch_address(wallets, c[2])
            else:
                print("unknown command")


        elif c[0] in ("describe", "d"):
            if len(c) == 1:
                print("invalid command")
                pass
            elif c[1] in ("wallet", "w"):
                if len(c) == 3:
                    describe_wallet(c[2], wallets)
                else:
                    print("missing wallet identifier\n")
            elif c[1] in ("block", "b"):
                if len(c) == 3:
                    find_block_at_height(c[2], genesis_block)
                else:
                    print("missing block height\n")
            elif c[1] in ("mrb"):
                mrb = find_most_recent_block(genesis_block)
                print("Block number: " + str(mrb.block_height))
                print("Block hash: " + str(mrb.hash))
                if len(mrb.txs) == 0:
                    print("No txs")
                for tx in mrb.txs:
                    print("---")
                    print("Tx: " + str(mrb.txs.index(tx)))
                    print("To: " + str(tx.sending_address))
                    print("From: " + str(tx.receiving_address))
                    print("Amount: " + str(tx.unit_exchanged))
                    print("---")
            elif c[1] in ("blockchain", "bc"):
                describe_blockchain(genesis_block)
            else:
                print("unknown command")


        elif c[0] in ("get", "g"):
            if len(c) == 1:
                print("invalid command")
                pass
            elif c[1] in ("wallets", "w"):
                get_wallets(wallets)
            elif c[1] in ("addresses", "a"):
                get_addresses(wallets)
            else:
                print("unknown command")


        elif c[0] in ("exit", "quit", "q"):
            break


        else:
            print("unknown command")


if __name__ == "__main__":
    main()
