from src.block import Block, find_block, find_most_recent_block, 
from secrets import randbits
from hashlib import sha256


def find_difficulty(prev_difficulty, prev_block_timestamp, prev_prev_block_timestamp):

    TARGET_MINE_TIME = 20

    return prev_difficulty * (1 + ((prev_block_timestamp - prev_prev_block_timestamp) / TARGET_MINE_TIME))


def find_target(difficulty):

    target = .01 / difficulty

    if target > .01:

        return .01

    else:

        return target


def get_hash_merkle_root(transactions):

    tx = transactions.copy()

    if len(tx) == 0:

        return []

    temp = []

    while len(tx) > 1:

        concat = tx[len(tx)-1] + tx[len(tx)-2]

        curr_hash = sha256(concat.encode('utf-8')).hexdigest()

        temp.append(curr_hash)

        del tx[len(tx) - 1]

        del tx[len(tx) - 1]

    if len(tx) == 1:

        tx.append(tx[0])

        concat = tx[0] + tx[1]

        curr_hash = sha256(concat.encode('utf-8')).hexdigest()

        temp.append(curr_hash)

        del tx[len(tx) - 1]

        del tx[len(tx) - 1]

    if len(temp) == 1:

        return temp[0]

    else:

        hash_ = get_hash_merkle_root(temp)
        
        return hash_


def structure_new_block(prev_block):

    block = Block(prev_block)

    # The genesis block
    if prev_block is None:

        block.prev_hash = 0x0000000000000000000000000000000000000000000000000000000000000000

        block.block_height = 0

        block.difficulty = 1

    # Any other block than genesis block
    else:

        block.prev_block = prev_block

        block.prev_hash = prev_block.hash

        block.block_height = prev_block.block_height + 1

        block.difficulty = find_difficulty(prev_block.difficulty, prev_block.timestamp, prev_block.prev_block.timestamp)

    
    block.target = find_target(block.difficulty)


def start_mining(genesis_block):

    while True:

        block_mined = False

        prev_block = find_most_recent_block(genesis_block)

        curr_block = structure_new_block(prev_block)

        while block_mined != True:

            hash_merkle_root = get_hash_merkle_root(curr_block)

            nonce = randbits(32)

            block_components_to_be_hashed = [curr_block.timestamp, curr_block.block_height, curr_block.prev_hash, curr_block.difficulty,
                curr_block.target, hash_merkle_root, nonce]

            curr_block_hash = get_hash_merkle_root(block_components_to_be_hashed)

            if curr_block_hash < curr_block.target:
                
                curr_block.hash_merkle_root = hash_merkle_root

                curr_block.nonce = nonce

                curr_block.hash = curr_block_hash

                prev_block.next_block = curr_block

                block_mined = True





