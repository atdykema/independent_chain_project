from src.wallet import Wallet
from src.address import Address
from tools.tools import find_address, find_most_recent_block, find_wallet, find_address_without_wallet_specified
from src.tx import Tx


def update_blockchain(genesis_block, to_cl_queue):
    mrb = find_most_recent_block(genesis_block)
    while to_cl_queue.empty() is False:
        mrb.next_block = to_cl_queue.get()
        mrb = mrb.next_block


def touch_wallet(wallets, label=None):
    if label is None:
        label = input("Label (leave blank for default): ")
    for wallet in wallets:
        if label in wallet.label:
            print("identical wallet label error\n")
            return 1
    wallets.append(Wallet(label))


def touch_address(wallets, identifier=None):
    if identifier is None:
        identifier = input("wallet to add to...\n")
    wallet = find_wallet(identifier, wallets)
    if wallet == 1:
        print("invalid wallet\n")
        return 0
    address = Address()
    wallet.addresses.append(address)
    print(wallet.label)
    print(find_address(address.private_key, wallet).private_key)


def touch_tx(wallets, to_mine_queue, send_from_wallet=None, from_address_value=None, send_to_wallet=None, to_address_value=None, unit_exchanged=None):
    
    if send_from_wallet is None:
        send_from_wallet = input("Send from wallet... \n")

    wallet = find_wallet(send_from_wallet, wallets)
    if wallet == 1:
        print("invalid sending wallet\n")
        return 1
    if len(wallet.addresses) == 0:
        print("no addresses in sending wallet, aborting...")
        return 1
    
    numbered_addresses = {}
    for address in wallet.addresses:
        numbered_addresses[wallet.addresses.index(address)] = address.private_key

    if from_address_value is None:
        print("Enter number for corresponding address:")
        print("\t" + f"{wallet.addresses.index(address)}" + ". " + f"{address.private_key}")
        from_address_value = input()
    else:
        if len(numbered_addresses) - 1 < int(from_address_value):
            print("no sending address found at this value")
            return 1

    sending_address = find_address_without_wallet_specified(numbered_addresses[int(to_address_value)], wallets)

    if send_to_wallet is None:
        send_to_wallet = input("Send to wallet... \n")

    wallet = find_wallet(send_to_wallet, wallets)
    if wallet == 1:
        print("invalid receiving wallet\n")
        return 1
    if len(wallet.addresses) == 0:
        print("no addresses in receiving wallet, aborting...")
        return 1
    
    numbered_addresses = {}
    for address in wallet.addresses:
        numbered_addresses[wallet.addresses.index(address)] = address.private_key

    if to_address_value is None:
        print("Enter number for corresponding address:")
        print("\t" + f"{wallet.addresses.index(address)}" + ". " + f"{address.private_key}")
        to_address_value = input()
    else:
        if len(numbered_addresses) - 1 < int(to_address_value):
            print("no receiving address found at this value")
            return 1
    
    receiving_address = find_address_without_wallet_specified(numbered_addresses[int(to_address_value)], wallets)

    if unit_exchanged is None:
        unit_exchanged = input("Amount to send... \n")

    try:
        unit_exchanged = float(unit_exchanged)
    except ValueError:
        print("unit is not an int")
        return 1

    if sending_address.total_unspent < unit_exchanged:
        print("Insufficient funds in sending wallet")
        return 1

    print(f"Sending {unit_exchanged} units from {sending_address} to {receiving_address}")
    
    to_mine_queue.put(Tx(sending_address, receiving_address, unit_exchanged))


def describe_wallet(identifier, wallets):
    wallet = find_wallet(identifier, wallets)
    if wallet == 1:
        print("invalid wallet\n")
        return 0
    print(wallet.label)
    print(wallet.timestamp)
    for address in wallet.addresses:
        print(address.private_key)
        print(address.total_unspent)


def describe_blockchain(genesis_block):
    block = genesis_block
    while block.next_block is not None:
        print(block.block_height)
        for tx in block.txs:
            print(tx.sending_address)
            print(tx.receiving_address)
            print(tx.unit_exchanged)
        block = block.next_block


def get_wallets(wallets):
    for wallet in wallets:
        print(wallet.label)


def get_addresses(wallets):
    for wallet in wallets:
        print(wallet.label)
        if len(wallet.addresses) == 0:
            print("\tNo addresses in this wallet")
            continue
        for address in wallet.addresses:
            print("\t" + address.private_key)