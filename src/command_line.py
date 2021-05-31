import wallet as w
import tx as tx
import main as m
import multiprocessing as mp


def start_command_line():
    while True:
        c = input()
        # create wallet
        if c in ("touch wallet", "touch w"):
            label_input = input("Label (leave blank for default)")
            if label_input == '':
                label = "default" + str(len(m.wallets))
            else:
                label = label_input
            m.wallets.append(w.Wallet(label))
            print(m.wallets)
        if c in "describe wallet":
            describe_wallet = input("input wallet to describe...")
            wallet = w.find_wallet(describe_wallet)
            if wallet == 1:
                print("invalid wallet")
                return 0
            print(wallet.get_label())
            print(wallet.get_private_key())
            print(wallet.get_mnemonic_phrase())
            print(wallet.get_utxos())
        if c in ("get wallets", "g wallets"):
            for wallet in m.wallets:
                print(wallet.get_label())
        if c in "touch tx":
            sending_wallet = input("Send from wallet... \n")
            sending_wallet_obj = w.find_wallet(sending_wallet)
            if sending_wallet_obj == 1:
                print("invalid sending wallet")
                return 0
            receiving_wallet = input("Receiving wallet... \n")
            receiving_wallet = w.find_wallet(receiving_wallet)
            if receiving_wallet == 1:
                print("invalid receiving wallet")
                return 0
            unit_exchanged = input("Amount to send... \n")
            if unit_exchanged < sending_wallet_obj.total_unspent:
                print("invalid exchange amount")
                return 0
        #exit
        elif c in ("exit", "quit", "q"):
            return 1
