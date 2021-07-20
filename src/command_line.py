from src.coinbase import Coinbase
from src.wallet import find_wallet
from src.wallet import Wallet
from src.address import Address, find_address
from src.tx import Tx
from src.block import find_most_recent_block, find_block_at_height



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

    sending_address = numbered_addresses[int(from_address_value)]

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
    
    receiving_address = numbered_addresses[int(to_address_value)]

    if unit_exchanged is None:
        unit_exchanged = input("Amount to send... \n")

    try:
        unit_exchanged = int(unit_exchanged)
    except ValueError:
        print("unit is not an int")
        return 1

    print(f"Sending {unit_exchanged} units from {sending_address} to {receiving_address}")
    
    to_mine_queue.put(Tx(sending_address, receiving_address, unit_exchanged))

    #TODO: check amount at address


def describe_wallet(identifier, wallets):
    wallet = find_wallet(identifier, wallets)
    if wallet == 1:
        print("invalid wallet\n")
        return 0
    print(wallet.label)
    print(wallet.timestamp)
    for address in wallet.addresses:
        print(address.private_key)


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


def start_command_line(wallets, genesis_block, coinbase, to_cl_queue, to_mine_queue):
    while True:

        c = input().split()

        update_blockchain(genesis_block, to_cl_queue)

        if len(c) == 0:
            continue


        elif c[0] in ("help", "h"):
            print("Commands:")
            print("\ttouch")
            print("\t\twallet, w")
            print("\t\ttx, t")
            print("\t\taddress, a")
            print("\tget")
            print("\t\twallets, w")
            print("\t\taddresses, a")
            print("\tdescribe")
            print("\t\twallet, w")
            print("\t\tmrb")


        elif c[0] in ("touch", "t"):
            if len(c) == 1:
                print("invalid command")
                pass
            elif c[1] in ("wallet", "w"):
                if len(c) == 3:
                    touch_wallet(wallets, c[2])
            elif c[1] in ("tx", "t"):
                if len(c) < 3:
                    touch_tx(wallets, to_mine_queue)
                elif len(c) == 3:
                    touch_tx(wallets, to_mine_queue, c[2])
                elif len(c) == 4:
                    touch_tx(wallets, to_mine_queue, c[2], c[3])
                elif len(c) == 5:
                    touch_tx(wallets, to_mine_queue, c[2], c[3], c[4])
                elif len(c) == 6:
                    touch_tx(wallets, to_mine_queue, c[2], c[3], c[4], c[5])
                elif len(c) == 7:
                    touch_tx(wallets, to_mine_queue, c[2], c[3], c[4], c[5], c[6])
                else:
                    touch_tx(wallets, to_mine_queue)
            elif c[1] in ("address", "a"):
                if len(c) == 3:
                    touch_address(wallets, c[2])
            else:
                print("unknown command")


        elif c[0] in ("describe", "d"):
            if len(c) == 1:
                print("invalid command")
                pass
            elif c[1] in ("wallet", "w"):
                if len(c) == 3:
                    describe_wallet(c[2], wallets)
                else:
                    print("missing wallet identifier\n")
            elif c[1] in ("block", "b"):
                if len(c) == 3:
                    find_block_at_height(c[2], genesis_block)
                else:
                    print("missing block height\n")
            elif c[1] in ("mrb"):
                mrb = find_most_recent_block(genesis_block)
                print("Block number: " + str(mrb.block_height))
                print("Block hash: " + str(mrb.hash))
                if len(mrb.txs) == 0:
                    print("No txs")
                for tx in mrb.txs:
                    print("---")
                    print("Tx: " + str(mrb.txs.index(tx)))
                    print("To: " + str(tx.sending_address))
                    print("From: " + str(tx.receiving_address))
                    print("Amount: " + str(tx.unit_exchanged))
                    print("---")
            elif c[1] in ("blockchain", "bc"):
                describe_blockchain(genesis_block)
            else:
                print("unknown command")


        elif c[0] in ("get", "g"):
            if len(c) == 1:
                print("invalid command")
                pass
            elif c[1] in ("wallets", "w"):
                get_wallets(wallets)
            elif c[1] in ("addresses", "a"):
                get_addresses(wallets)
            else:
                print("unknown command")


        elif c[0] in ("exit", "quit", "q"):
            break


        else:
            print("unknown command")
