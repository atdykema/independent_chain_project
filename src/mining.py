from src.block import Block, find_block, find_most_recent_block, print_blockchain
from time import sleep
from random import randrange
# TODO: find difficulty


def start_mining(genesis_block):

    while True:
        n = randrange(0,2)
        if n == 1:
            print("found")
            curr_block = find_most_recent_block(genesis_block)
            curr_block.block_hash = n
            new_block = Block(curr_block)
            new_block.prev_block = curr_block
            curr_block.next_block = new_block

        sleep(.5)


