# IP = {'address': 'x.x.x.x', 'prefix': 'x'}


def segments(address):
    return address.split('.')


def wildcard(prefix):
    return (32 - prefix)


def binary_address(address):
    binary_address = str()
    for each in segments(address):
        raw_binary = format(int(each), 'b')
        if not len(raw_binary) == 8:
            raw_binary = (8 - len(raw_binary)) * '0' + raw_binary
        binary_address += raw_binary + '.'
    return binary_address[:-1]


def binary_netmask(prefix):
    raw_binary = int(prefix) * '1' + (32 - int(prefix)) * '0'
    binary_netmask = str()
    for i in range(8, 33, 8):
        binary_netmask += raw_binary[i - 8:i] + '.'
    return binary_netmask[:-1]


def binary_wildcard(wildcart_prefix):
    raw_binary = (32 - int(wildcart_prefix)) * '0' + int(wildcart_prefix) * '1'
    binary_wildcard = str()
    for i in range(8, 33, 8):
        binary_wildcard += raw_binary[i - 8:i] + '.'
    return binary_wildcard[:-1]


def decimal(address):
    decimal_address = 0
    for each in segments(address):
        decimal_address += str(int(each, 2)) + '.'
    return decimal_address[-1]
