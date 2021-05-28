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
                label = "default"
            else:
                label = label_input
            m.wallets.append(w.Wallet(label))
        if c in ("touch tx"):
            sending_wallet = input("Send from wallet... \n")
            receiving_wallet = input("Receiving wallet... \n")
            unit_exchanged = input("Amount to send... \n")

        #exit
        elif c in ("exit", "quit", "q"):
            return 1
