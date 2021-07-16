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


def start_mining(genesis_block):

    while True:

        block_mined = False

        prev_block = find_most_recent_block(genesis_block)

        if prev_block.block_height == 0:

            curr_difficulty = 0

        else:
            
            curr_difficulty = find_difficulty(prev_block.timestamp, prev_block.prev_block.timestamp)

        curr_target = find_target(curr_difficulty)

        while block_mined != True:

            pass

        
    


