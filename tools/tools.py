

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