from src.wallet import find_wallet
from src.wallet import Wallet
from src.address import Address, find_address
from src.tx import Tx, add_tx_to_block
from src.block import find_most_recent_block
import multiprocessing as mp


def touch_wallet(wallets):
    # TODO for testing: label_input = input("Label (leave blank for default): ")
    label_input = ''
    if label_input == '':
        label = "d" + str(len(wallets))
    else:
        label = label_input
    for wallet in wallets:
        if label in wallet.label:
            print("identical wallet label error\n")
            return 0
    wallets.append(Wallet(label))


def touch_address(wallets):
    # TODO for testing: identifier = input("wallet to add to...\n")
    identifier = "d0"
    wallet = find_wallet(identifier, wallets)
    if wallet == 1:
        print("invalid wallet\n")
        return 0
    address = Address()
    wallet.addresses.append(address)
    print(wallet.label)
    print(find_address(address.private_key, wallet).private_key)


def touch_tx(wallets, genesis_block):
    send_from_wallet = input("Send from wallet... \n")
    wallet = find_wallet(send_from_wallet, wallets)
    if wallet == 1:
        print("invalid wallet\n")
        return 1
    if len(wallet.addresses) == 0:
        print("no addresses in wallet, aborting...")
        return 1
    print("Enter number for corresponding address:")
    numbered_addresses = {}
    for address in wallet.addresses:
        numbered_addresses[wallet.addresses.index(address)] = address.private_key
        print("\t" + f"{wallet.addresses.index(address)}" + ". " + f"{address.private_key}")
    value = input()
    sending_address = numbered_addresses[int(value)]

    send_to_wallet = input("Send to wallet... \n")
    wallet = find_wallet(send_to_wallet, wallets)
    if wallet == 1:
        print("invalid wallet\n")
        return 1
    if len(wallet.addresses) == 0:
        print("no addresses in wallet, aborting...")
        return 1
    print("Enter number for corresponding address:")
    numbered_addresses = {}
    for address in wallet.addresses:
        numbered_addresses[wallet.addresses.index(address)] = address.private_key
        print("\t" + f"{wallet.addresses.index(address)}" + ". " + f"{address.private_key}")
    value = input()
    receiving_address = numbered_addresses[int(value)]

    unit_exchanged = input("Amount to send... \n")

    # TODO: create TX object
    tx = Tx(sending_address, receiving_address, unit_exchanged)

    # TODO: add tx to block
    add_tx_to_block(tx, find_most_recent_block(genesis_block))


def describe_wallet(identifier, wallets):
    wallet = find_wallet(identifier, wallets)
    if wallet == 1:
        print("invalid wallet\n")
        return 0
    print(wallet.label)
    print(wallet.timestamp)
    for address in wallet.addresses:
        print(address.private_key)


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


def start_command_line(wallets, genesis_block, coinbase):
    while True:
        c = input().split()

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

        elif c[0] == "touch":
            if len(c) == 1:
                print("invalid command")
                pass
            elif c[1] in ("wallet", "w"):
                touch_wallet(wallets)
            elif c[1] in ("tx", "t"):
                touch_tx(wallets)
            elif c[1] in ("address", "a"):
                touch_address(wallets)
            else:
                print("invalid command")

        elif c[0] == "describe":
            if len(c) == 1:
                print("invalid command")
                pass
            elif c[1] in ("wallet", "w"):
                if len(c) == 3:
                    describe_wallet(c[2], wallets)
                else:
                    print("missing wallet identifier\n")

        elif c[0] == "get":
            if len(c) == 1:
                print("invalid command")
                pass
            elif c[1] in ("wallets", "w"):
                get_wallets(wallets)
            elif c[1] in ("addresses", "a"):
                get_addresses(wallets)

        elif c[0] in ("exit", "quit", "q"):
            break

        else:
            print("unknown command")
