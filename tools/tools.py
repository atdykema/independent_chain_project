

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


def binary_to_hex(bin_input):
    hexadecimal = ""
    for n in bin_input:
        if n == '0000':
            hexadecimal += '0'
        if n == '0001':
            hexadecimal += '1'
        if n == '0010':
            hexadecimal += '2'
        if n == '0011':
            hexadecimal += '3'
        if n == '0100':
            hexadecimal += '4'
        if n == '0101':
            hexadecimal += '5'
        if n == '0110':
            hexadecimal += '6'
        if n == '0111':
            hexadecimal += '7'
        if n == '1000':
            hexadecimal += '8'
        if n == '1001':
            hexadecimal += '9'
        if n == '1010':
            hexadecimal += 'a'
        if n == '1011':
            hexadecimal += 'b'
        if n == '1100':
            hexadecimal += 'c'
        if n == '1101':
            hexadecimal += 'd'
        if n == '1110':
            hexadecimal += 'e'
        if n == '1111':
            hexadecimal += 'f'
    return hexadecimal


