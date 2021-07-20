from hashlib import sha256
from src.block import Block


def find_difficulty(prev_difficulty, prev_block_timestamp, prev_prev_block_timestamp):

    TARGET_MINE_TIME = 3

    percent_difference = (1 / ( (prev_block_timestamp - prev_prev_block_timestamp)/ TARGET_MINE_TIME))

    #print(f'Percent change: {percent_difference}')
    #print(f'Seconds taken: {prev_block_timestamp - prev_prev_block_timestamp}')

    if percent_difference > 1.25:
        return prev_difficulty * 1.25
    elif percent_difference < .75:
        return prev_difficulty * .75    
    else:
        return prev_difficulty * percent_difference


def find_target(difficulty):
    target = .00001 / difficulty
    if target > .00001:
        return .00001
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


def get_hash_merkle_root(transactions):
    tx = transactions.copy()
    if len(tx) == 0:
        return 0
    
    tx_hashes = []

    for trans in tx:
        tx_hashes.append(sha256((trans.sending_address + trans.receiving_address + str(trans.unit_exchanged)).encode('utf-8')).hexdigest())

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


def find_block(identifier, genesis_block):
    block = genesis_block
    while block.block_hash != identifier:
        block = block.next_block
        if block is None:
            print("block not found")
            return 1
    return block


def find_block_at_height(height, genesis_block):
    block = genesis_block
    while block.block_height != height:
        block = block.next_block
    return block


def find_most_recent_block(genesis_block):
    block = genesis_block
    while block.next_block is not None:
        block = block.next_block
    return block


def find_wallet(identifier, wallets):
    for wallet in wallets:
        if wallet.label == identifier:
            return wallet
    return 1


def find_address(identifier, wallet):
    for address in wallet.addresses:
        if address.private_key == identifier:
            return address
    return 1


def list_to_string(list):
    s = ""
    for digit in list:
        s += digit
    return s


def binary_to_decimal(n):
    return int(n, 2)


def list_chars_to_other_list(from_list, to_list):
    for digit in from_list:
        to_list.append(digit)


def hex_to_binary(hex_input):
    binary = ""
    for n in hex_input:
        if n == '0':
            binary += '0000'
        if n == '1':
            binary += '0001'
        if n == '2':
            binary += '0010'
        if n == '3':
            binary += '0011'
        if n == '4':
            binary += '0100'
        if n == '5':
            binary += '0101'
        if n == '6':
            binary += '0110'
        if n == '7':
            binary += '0111'
        if n == '8':
            binary += '1000'
        if n == '9':
            binary += '1001'
        if n == 'a':
            binary += '1010'
        if n == 'b':
            binary += '1011'
        if n == 'c':
            binary += '1100'
        if n == 'd':
            binary += '1101'
        if n == 'e':
            binary += '1110'
        if n == 'f':
            binary += '1111'
    return binary


def binary_to_hex(bin_input):
    hexadecimal = ""
    for n in bin_input:
        if n == '0000':
            hexadecimal += '0'
        if n == '0001':
            hexadecimal += '1'
        if n == '0010':
            hexadecimal += '2'
        if n == '0011':
            hexadecimal += '3'
        if n == '0100':
            hexadecimal += '4'
        if n == '0101':
            hexadecimal += '5'
        if n == '0110':
            hexadecimal += '6'
        if n == '0111':
            hexadecimal += '7'
        if n == '1000':
            hexadecimal += '8'
        if n == '1001':
            hexadecimal += '9'
        if n == '1010':
            hexadecimal += 'a'
        if n == '1011':
            hexadecimal += 'b'
        if n == '1100':
            hexadecimal += 'c'
        if n == '1101':
            hexadecimal += 'd'
        if n == '1110':
            hexadecimal += 'e'
        if n == '1111':
            hexadecimal += 'f'
    return hexadecimal


