

def list_to_string(list):
    s = ""
    for digit in list:
        s += digit
    return s


def binary_to_decimal(n):
    return int(n, 2)


def list_chars_to_other_list(from_list, to_list):
    for digit in from_list:
        to_list.append(digit)


def hex_to_binary(hex_input):
    binary = ""
    for n in hex_input:
        if n == '0':
            binary += '0000'
        if n == '1':
            binary += '0001'
        if n == '2':
            binary += '0010'
        if n == '3':
            binary += '0011'
        if n == '4':
            binary += '0100'
        if n == '5':
            binary += '0101'
        if n == '6':
            binary += '0110'
        if n == '7':
            binary += '0111'
        if n == '8':
            binary += '1000'
        if n == '9':
            binary += '1001'
        if n == 'a':
            binary += '1010'
        if n == 'b':
            binary += '1011'
        if n == 'c':
            binary += '1100'
        if n == 'd':
            binary += '1101'
        if n == 'e':
            binary += '1110'
        if n == 'f':
            binary += '1111'
    return binary
