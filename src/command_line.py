from wallet import *
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
            wallet = Wallet(label)
        #exit
        elif c == "exit" or "quit" or "q":
            return 1
