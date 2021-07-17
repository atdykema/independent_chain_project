from src.block import Block, find_block, find_most_recent_block, print_blockchain
from secrets import randbits
from hashlib import sha256


def find_difficulty(prev_difficulty, prev_block_timestamp, prev_prev_block_timestamp):

    TARGET_MINE_TIME = 1

    return prev_difficulty * (1 + (((prev_block_timestamp - prev_prev_block_timestamp) *10) / TARGET_MINE_TIME))


def find_target(difficulty):
    target = .001 / difficulty
    if target > .001:
        return .001
    else:
        return target


def hash_block(contents):
    block_contents = contents.copy()
    temp = []
    while len(block_contents) > 1:
        concat = str(block_contents[len(block_contents)-1]) + str(block_contents[len(block_contents)-2])
        curr_hash = sha256(concat.encode('utf-8')).hexdigest()
        temp.append(curr_hash)
        del block_contents[len(block_contents) - 1]
        del block_contents[len(block_contents) - 1]
    return temp[0]

# remake taking each characteristic out of each tx and hashing, then hashing tx together
def get_hash_merkle_root(transactions):
    tx = transactions.copy()
    if len(tx) == 0:
        return 0
    
    tx_hashes = []

    for trans in tx:
        str(trans.sending_address + trans.receiving_address + trans.unit_exchanged).encode().append(tx_hashes)

    temp = []

    while len(tx_hashes) > 1:
        concat = tx_hashes[len(tx_hashes)-1] + tx_hashes[len(tx_hashes)-2]
        curr_hash = sha256(concat.encode('utf-8')).hexdigest()
        temp.append(curr_hash)
        del tx_hashes[len(tx_hashes) - 1]
        del tx_hashes[len(tx_hashes) - 1]

    if len(tx_hashes) == 1:
        tx_hashes.append(tx_hashes[0])
        concat = tx_hashes[0] + tx_hashes[1]
        curr_hash = sha256(concat.encode('utf-8')).hexdigest()
        temp.append(curr_hash)
        del tx_hashes[len(tx_hashes) - 1]
        del tx_hashes[len(tx_hashes) - 1]

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
    elif prev_block.prev_block is None:
        block.prev_hash = prev_block.hash
        block.difficulty = 1
        block.block_height = 1

    # Any other block than genesis block
    else:
        block.prev_block = prev_block
        block.prev_hash = prev_block.hash
        block.block_height = prev_block.block_height + 1
        block.difficulty = find_difficulty(prev_block.difficulty, prev_block.timestamp, prev_block.prev_block.timestamp)

    
    block.target = find_target(block.difficulty)

    return block


def start_mining(genesis_block):
    TWO_POWER_256 = 115792089237316195423570985008687907853269984665640564039457584007913129639936
    test_dict = dict()
    while True:
        block_mined = False
        prev_block = find_most_recent_block(genesis_block)
        curr_block = structure_new_block(prev_block)

        while block_mined != True:

            hash_merkle_root = get_hash_merkle_root(curr_block.txs)

            nonce = randbits(32)

            block_components_to_be_hashed = [curr_block.timestamp, curr_block.block_height, curr_block.prev_hash, curr_block.difficulty,
                curr_block.target, hash_merkle_root, nonce]

            curr_block_hash = hash_block(block_components_to_be_hashed)

            output_number = int(curr_block_hash, 16)/TWO_POWER_256

            #print(f'{curr_block.target}')
            #print(f'{output_number}: {output_number < curr_block.target}')

            if output_number < curr_block.target:     
                curr_block.hash_merkle_root = hash_merkle_root
                curr_block.nonce = nonce
                curr_block.hash = curr_block_hash
                prev_block.next_block = curr_block
                block_mined = True
                print(f"{curr_block.block_height}: {curr_block.target}, {curr_block.difficulty}")





