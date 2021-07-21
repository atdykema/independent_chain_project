from tools.tools import find_address, find_most_recent_block, find_wallet, structure_new_block, get_hash_merkle_root, hash_block, find_address_without_wallet_specified, get_coinbase_block_reward
from secrets import randbits
from src.tx import Tx
from src.address import Address


def start_mining(genesis_block, to_cl_queue_blocks, to_mine_queue_txs, to_cl_queue_wallets, to_mine_queue_wallets, wallets):
    TWO_POWER_256 = 115792089237316195423570985008687907853269984665640564039457584007913129639936
    coinbase = Address()
    coinbase.private_key = 'Coinbase'
    coinbase.total_unspent = 21000000
    while True:
        block_mined = False
        prev_block = find_most_recent_block(genesis_block)
        curr_block = structure_new_block(prev_block)

        if to_mine_queue_wallets.empty is False:
            wallets = to_mine_queue_wallets.get()

        curr_block.txs.append(Tx(coinbase, find_wallet('default', wallets).addresses[0], get_coinbase_block_reward(find_most_recent_block(genesis_block))))

        while block_mined != True:

            if to_mine_queue_wallets.empty is False:
                wallets = to_mine_queue_wallets.get()

            while to_mine_queue_txs.empty() is False:
                curr_block.txs.append(to_mine_queue_txs.get())


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

                to_cl_queue_blocks.put(curr_block)

                #TODO: complete txs

                for tx in curr_block.txs:
                    if tx.sending_address.private_key == 'Coinbase':
                        receiving_address_obj = find_address_without_wallet_specified(tx.receiving_address.private_key, wallets)
                        receiving_address_obj.total_unspent += tx.unit_exchanged
                        coinbase.total_unspent -= tx.unit_exchanged
                    else:
                        sending_address_obj = find_address_without_wallet_specified(tx.sending_address.private_key, wallets)
                        receiving_address_obj = find_address_without_wallet_specified(tx.receiving_address.private_key, wallets)
                        
                        sending_address_obj.total_unspent -= tx.unit_exchanged
                        receiving_address_obj.total_unspent += tx.unit_exchanged

                #TODO: to_cl_queue_wallets.put()

                while to_cl_queue_wallets.empty() == False:
                    to_cl_queue_wallets.get()
                to_cl_queue_wallets.put(wallets)
                
                #print(f"{curr_block.block_height}: {curr_block.target}, {curr_block.difficulty}")
                #print (f"Prev_block: {curr_block.prev_block} {curr_block.prev_block.hash}, hash: {curr_block.hash}")





