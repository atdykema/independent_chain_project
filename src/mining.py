from src.block import Block, find_block, find_most_recent_block


def find_difficulty(prev_difficulty, prev_block_timestamp, prev_prev_block_timestamp):

    TARGET_MINE_TIME = 20

    return prev_difficulty * (1 + ((prev_block_timestamp - prev_prev_block_timestamp) / TARGET_MINE_TIME))


def find_target(difficulty):

    target = .01 / difficulty

    if target > .01:

        return .01

    else:

        return target


def structure_new_block(prev_block):

    block = Block(prev_block)

    # The genesis block
    if prev_block is None:

        block.prev_hash = 0x0000000000000000000000000000000000000000000000000000000000000000

        block.block_height = 0

        block.difficulty = 1

    # Any other block than genesis block
    else:

        block.prev_hash = prev_block.hash

        block.block_height = prev_block.block_height + 1

        block.difficulty = find_difficulty(prev_block.difficulty, prev_block.timestamp, prev_block.prev_block.timestamp)

    
    block.target = find_target(block.difficulty)


def start_mining(genesis_block):

    while True:

        block_mined = False

        prev_block = find_most_recent_block(genesis_block)

        structure_new_block(prev_block)

        while block_mined != True:

            pass

        
    


