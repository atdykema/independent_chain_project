import time, random, tools.tools, os, hashlib, binascii
from pbkdf2 import PBKDF2


def mnemonic_phrase_generation():
    mnemonic_words = []
    total_word_digits = []
    current_word_digits = []
    f = open("BIP39_wordlist.txt", "r")
    word_list = f.readlines()
    f.close()
    for n in range(0, 256):
        current_word_digits.append(str(random.randint(0, 1)))
        if len(current_word_digits) % 11 == 0:
            # convert list to string
            binary_string = tools.tools.list_to_string(current_word_digits)
            # string to decimal from binary
            decimal = tools.tools.binary_to_decimal(binary_string)
            # get word from word list
            mnemonic_words.append(word_list[decimal][0:-1])
            # add digits to total list
            tools.tools.list_chars_to_other_list(current_word_digits, total_word_digits)
            # clear list
            current_word_digits.clear()
    three_digits_checksum = tools.tools.list_to_string(current_word_digits)
    # get sha256 of 256 word digits
    str_total_word_digits = tools.tools.list_to_string(total_word_digits)
    sha256_string = hashlib.sha256(bytes(str_total_word_digits, encoding='utf-8'))
    # sha256 to hex
    sha256_hex = sha256_string.hexdigest()
    # get 24th word from checksum
    checksum = tools.tools.hex_to_binary(sha256_hex[0:2]) + three_digits_checksum
    decimal_checksum = tools.tools.binary_to_decimal(checksum)
    mnemonic_words.append(word_list[decimal_checksum][0:-1])
    mnemonic_phrase = f'{mnemonic_words[0]}'
    for word in mnemonic_words[1:24]:
        mnemonic_phrase += ' '
        mnemonic_phrase += word
    return mnemonic_phrase


def master_key_generation(mnemonic_phrase, additional_master_key_password):
    mnemonic_password = mnemonic_phrase
    mnemonic_salt = "mnemonic" + additional_master_key_password
    iterations = 1000
    mnemonic_key = '0x' + str(binascii.hexlify
                     (PBKDF2(mnemonic_password, mnemonic_salt, iterations, digestmodule=hashlib.sha256).read(64)))[2:-1]
    master_key = '0x' + str(binascii.hexlify
                     (PBKDF2(mnemonic_key, 'Bitcoin seed', iterations, digestmodule=hashlib.sha256).read(64)))[2:-1]
    return master_key


class Wallet:
    def __init__(self, label):
        self.label = label
        print(self.label)
        self.mnemonic_phrase = mnemonic_phrase_generation()
        print(self.mnemonic_phrase)
        #TODO:
        additional_master_key_password = ""#input("Additional master key password (optional) ")
        self.master_key = master_key_generation(self.mnemonic_phrase, additional_master_key_password)
        print(self.master_key)
        #AKA extended private key ^
        self.private_key = self.master_key[2:66]
        print(self.private_key)


    def get_label(self):
        return self.label


    def get_mnemonic_words(self):
        return self.mnemonic_phrase
