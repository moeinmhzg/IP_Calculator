# example of the ip varibale:
# ip = {'address': 'x.x.x.x', 'prefix': 'x'}


def segmented(raw_addres):
    segmented_address = str()
    for i in range(8, 33, 8):
        segmented_address += raw_addres[i - 8:i] + '.'
    return segmented_address[:-1]


def raw_binary(binary):
    return binary.replace('.', '')


def segments(address):
    return address.split('.')


def wildcard(prefix):
    return (32 - prefix)


def binary(address):
    binary_address = str()
    for segment in segments(address):
        segment_binary = format(int(segment), 'b')
        if not len(segment_binary) == 8:
            segment_binary = (8 - len(segment_binary)) * '0' + segment_binary
        binary_address += segment_binary + '.'
    return binary_address[:-1]


def binary_netmask(prefix):
    raw_binary = int(prefix) * '1' + (32 - int(prefix)) * '0'
    return segmented(raw_binary)


def binary_wildcard(wildcart_prefix):
    raw_binary = (32 - int(wildcart_prefix)) * '0' + int(wildcart_prefix) * '1'
    return segmented(raw_binary)


def decimal(address):
    decimal_address = str()
    for segment in segments(address):
        decimal_address += str(int(segment, 2)) + '.'
    return decimal_address[:-1]


def network_address(ip):
    network_part = raw_binary(binary(ip['address']))[:int(ip['prefix'])]
    host_part = '0' * int(wildcard(ip['prefix']))
    return decimal(segmented(network_part + host_part))


def broadcast_address(ip):
    network_part = raw_binary(binary(ip['address']))[:int(ip['prefix'])]
    host_part = '1' * int(wildcard(ip['prefix']))
    return decimal(segmented(network_part + host_part))