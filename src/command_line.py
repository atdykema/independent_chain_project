from src.wallet import find_wallet
from src.wallet import Wallet
from src.address import Address, find_address
import multiprocessing as mp


def touch_wallet(wallets):
    label_input = input("Label (leave blank for default): ")
    if label_input == '':
        label = "default" + str(len(wallets))
    else:
        label = label_input
    for wallet in wallets:
        if label in wallet.label:
            print("identical wallet label error\n")
            return 0
    wallets.append(Wallet(label))


def touch_address():
    identifier = input("wallet to add to...\n")
    wallet = find_wallet(identifier)
    if wallet == 1:
        print("invalid wallet\n")
        return 0
    address = Address()
    wallet.addresses.append(address)
    print(wallet.label)
    print(wallet.addresses)
    print(find_address(address.private_key, wallet).private_key)


def touch_tx():
    sending_address = input("Send from address... \n")
    sending_address_obj = find_address(sending_address)
    if sending_address_obj == 1:
        print("invalid sending address\n")
        return 0

    receiving_address = input("Receiving address... \n")
    receiving_address_obj = find_address(receiving_address)
    if receiving_address_obj == 1:
        print("invalid receiving wallet\n")
        return 0

    unit_exchanged = input("Amount to send... \n")
    if unit_exchanged < sending_address_obj.total_unspent:
        print("invalid exchange amount\n")
        return 0


def describe_wallet(identifier):
    wallet = find_wallet(identifier)
    if wallet == 1:
        print("invalid wallet\n")
        return 0
    print(wallet.label)
    print(wallet.timestamp)
    for address in wallet.addresses:
        print(address)


def get_wallets(wallets):
    for wallet in wallets:
        print(wallet.label)


def start_command_line():
    while True:
        c = input().split()

        if len(c) == 1:
            print("invalid command")
            continue

        if c[0] == "touch":
            if c[1] in ("wallet", "w"):
                touch_wallet()
            elif c[1] in ("tx", "t"):
                touch_tx()
            elif c[1] in ("address", "a"):
                touch_address()

        elif c[0] == "describe":
            if c[1] in ("wallet", "w"):
                if len(c) == 3:
                    describe_wallet(c[2])
                else:
                    print("missing wallet identifier\n")

        elif c[0] == "get":
            if c[1] in ("wallet", "w"):
                get_wallets()

        elif c[0] in ("exit", "quit", "q"):
            break
