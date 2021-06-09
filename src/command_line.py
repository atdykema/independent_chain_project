import src.wallet as w
import src.tx as tx
import src.main as m
import src.address as a
import multiprocessing as mp


def touch_wallet():
    label_input = input("Label (leave blank for default): ")
    if label_input == '':
        label = "default" + str(len(m.wallets))
    else:
        label = label_input
    for wallet in m.wallets:
        if label in wallet.label:
            print("identical wallet label error\n")
            return 0
    m.wallets.append(w.Wallet(label))


def touch_address():
    identifier = input("wallet to add to...\n")
    wallet = w.find_wallet(identifier)
    if wallet == 1:
        print("invalid wallet\n")
        return 0
    address = a.Address()
    wallet.addresses.append(address)
    print(wallet.label)
    print(wallet.addresses)
    print(a.find_address(address.private_key, wallet).private_key)


def touch_tx():
    sending_address = input("Send from address... \n")
    sending_address_obj = a.find_address(sending_address)
    if sending_address_obj == 1:
        print("invalid sending address\n")
        return 0

    receiving_address = input("Receiving address... \n")
    receiving_address_obj = a.find_address(receiving_address)
    if receiving_address_obj == 1:
        print("invalid receiving wallet\n")
        return 0

    unit_exchanged = input("Amount to send... \n")
    if unit_exchanged < sending_address_obj.total_unspent:
        print("invalid exchange amount\n")
        return 0


def describe_wallet(identifier):
    wallet = w.find_wallet(identifier)
    if wallet == 1:
        print("invalid wallet\n")
        return 0
    print(wallet.label)
    print(wallet.timestamp)
    for address in wallet.addresses:
        print(address)


def get_wallets():
    for wallet in m.wallets:
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
