import time
import random
import tools.tools


class Wallet:
    def __init__(self):
        mnemonic_words = []
        binary_generation = []
        for n in range(0, 256):
            binary_generation.append(str(random.randint(0, 1)))
            if(len(binary_generation) % 11 == 0):
                #convert list to string
                tools.tools.list_to_string(binary_generation)
                #string to decimal from binary
                print(binary_generation)
                print(n / 11)
                # add one, get word from word list
                binary_generation.clear()
                #clear list


