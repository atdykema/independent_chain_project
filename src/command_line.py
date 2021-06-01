import src.wallet as w
import src.tx as tx
import src.main as m
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


def describe_wallet():
    wallet_to_describe = input("input wallet to describe... ")
    wallet = w.find_wallet(wallet_to_describe)
    if wallet == 1:
        print("invalid wallet\n")
        return 0
    print(wallet.label)
    print(wallet.private_key)
    print(wallet.mnemonic_phrase)


def get_wallets():
    for wallet in m.wallets:
        print(wallet.label)


def touch_tx():
    sending_wallet = input("Send from wallet... \n")
    sending_wallet_obj = w.find_wallet(sending_wallet)
    if sending_wallet_obj == 1:
        print("invalid sending wallet\n")
        return 0
    receiving_wallet = input("Receiving wallet... \n")
    receiving_wallet = w.find_wallet(receiving_wallet)
    if receiving_wallet == 1:
        print("invalid receiving wallet\n")
        return 0
    unit_exchanged = input("Amount to send... \n")
    if unit_exchanged < sending_wallet_obj.total_unspent:
        print("invalid exchange amount\n")
        return 0


def start_command_line():
    while True:
        c = input()
        # create wallet
        if c in ("touch wallet", "touch w"):
            touch_wallet()
        elif c == "describe wallet":
            describe_wallet()
        elif c in ("get wallets", "get w"):
            get_wallets()
        elif c == "touch tx":
            touch_tx()
        elif c in ("exit", "quit", "q"):
            break
