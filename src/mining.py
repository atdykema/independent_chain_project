from tools.tools import find_most_recent_block, structure_new_block, get_hash_merkle_root, hash_block
from secrets import randbits


def start_mining(genesis_block, to_cl_queue, to_mine_queue):
    TWO_POWER_256 = 115792089237316195423570985008687907853269984665640564039457584007913129639936
    while True:
        block_mined = False
        prev_block = find_most_recent_block(genesis_block)
        curr_block = structure_new_block(prev_block)

        while block_mined != True:

            while to_mine_queue.empty() is False:
                curr_block.txs.append(to_mine_queue.get())

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

                to_cl_queue.put(curr_block)
                
                #print(f"{curr_block.block_height}: {curr_block.target}, {curr_block.difficulty}")
                #print (f"Prev_block: {curr_block.prev_block} {curr_block.prev_block.hash}, hash: {curr_block.hash}")





