import time
import random
import tools.tools
import os
import hashlib


class Wallet:
    def __init__(self):
        mnemonic_words = []
        total_word_digits = []
        current_word_digits = []
        f = open("BIP39_wordlist.txt", "r")
        word_list = f.readlines()
        f.close()
        for n in range(0, 256):
            current_word_digits.append(str(random.randint(0, 1)))
            if len(current_word_digits) % 11 == 0:
                #convert list to string
                binary_string = tools.tools.list_to_string(current_word_digits)
                #string to decimal from binary
                decimal = tools.tools.binary_to_decimal(binary_string)
                #get word from word list
                mnemonic_words.append(word_list[decimal][0:-1])
                #add digits to total list
                tools.tools.list_chars_to_other_list(current_word_digits, total_word_digits)
                #clear list
                current_word_digits.clear()
        three_digits_checksum = tools.tools.list_to_string(current_word_digits)
        #get sha256 of 256 word digits
        str_total_word_digits = tools.tools.list_to_string(total_word_digits)
        sha256_string = hashlib.sha256(bytes(str_total_word_digits, encoding='utf-8'))
        sha256_hex = sha256_string.hexdigest()
        checksum = tools.tools.hex_to_binary(sha256_hex[0:2]) + three_digits_checksum
        decimal_checksum = tools.tools.binary_to_decimal(checksum)
        mnemonic_words.append(word_list[decimal_checksum][0:-1])
        print(sha256_hex)
        print(checksum)
        print(three_digits_checksum)
        print(mnemonic_words)
