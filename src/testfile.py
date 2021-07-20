from multiprocessing.queues import Queue
from src.coinbase import Coinbase
from src.block import Block, find_most_recent_block, find_block_at_height
from src.command_line import update_blockchain, touch_address, touch_wallet, touch_tx, describe_blockchain, describe_wallet, get_addresses, get_wallets
from src.mining import start_mining, structure_new_block
from multiprocessing import Process, Queue
import sys
import os


def test_attributes(wallets):
    touch_wallet(wallets, 'd0')
    touch_wallet(wallets, 'd1')
    touch_wallet(wallets, 'test')
    touch_address(wallets, 'd1')
    touch_address(wallets, 'd0')
    print("--Wallets--")
    get_wallets(wallets)
    print("--Addresses--")
    get_addresses(wallets)