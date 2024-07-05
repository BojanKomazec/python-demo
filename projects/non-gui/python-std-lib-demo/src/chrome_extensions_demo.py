import binascii
import hashlib
import os
import string
import struct

# https://pypi.org/project/crx-unpack/
# From https://chromium.googlesource.com/chromium/src/+/master/components/crx_file/crx3.proto:
#
# // A CRX₃ file is a binary file of the following format:
# // [4 octets]: "Cr24", a magic number.
# // [4 octets]: The version of the *.crx file format used (currently 3).
# // [4 octets]: N, little-endian, the length of the header section.
# // [N octets]: The header (the binary encoding of a CrxFileHeader).
# // [M octets]: The ZIP archive.
# // Clients should reject CRX₃ files that contain an N that is too large for the
# // client to safely handle in memory.
#
# octet = 8 bits (1 byte)
# To get the header we first need to get its length.
# To get the header length, we first need to read first 12 bytes and read last 4 in little-endian.

def extract_id(crx_file_path: str):

    # os.O_BINARY is defined only for Windows
    # os.open(crx_file_path, os.O_RDONLY) and it returns a file descriptor
    # https://stackoverflow.com/questions/53564755/python-error-attributeerror-enter
    # I will use here built-in open() function
    with open(crx_file_path, "rb") as file_crx:
        # read magic number
        buff = file_crx.read(4)
        print(buff)

        # read crx format version
        buff = file_crx.read(4)
        print(buff)

        # read header length
        header_size = int.from_bytes(file_crx.read(4), byteorder='little')
        # or alternatively:
        # buff = file_crx.read(4)
        # print(buff)
        # header_size = buff[0] * 256**0 + buff[1] * 256**1 + buff[2] * 256**2 + buff[3] * 256**3
        print(f'header_size = {header_size}')

        header_encoded = file_crx.read(header_size)
        print(header_encoded)

        # todo:
        # - extract public key
        # - extract id from public key
    pass

# Code source: https://stackoverflow.com/a/21711992/404421
# Does not work with CRXv3
# def get_pub_key_from_crx(crx_file):
#     with open(crx_file, 'rb') as f:
#         data = f.read()
#     header = struct.unpack('<4sIII', data[:16])
#     pubkey = struct.unpack('<%ds' % header[2], data[16:16+header[2]])[0]
#     return pubkey

# Code source: https://stackoverflow.com/a/21711992/404421
# Does not work with CRXv3
# def get_extension_id(crx_file):
#     pubkey = get_pub_key_from_crx(crx_file)
#     digest = hashlib.sha256(pubkey).hexdigest()
#     trans = bytes.maketrans(b'0123456789abcdef', string.ascii_lowercase[:16].encode('utf-8'))
#     return str.translate(digest[:32], trans)

# Code source: https://stackoverflow.com/a/52263105/404421
def decode(proto, data):
    index = 0
    length = len(data)
    msg = dict()
    while index < length:
        item = 128
        key = 0
        left = 0
        while item & 128:
            item = data[index]
            index += 1
            value = (item & 127) << left
            key += value
            left += 7
        field = key >> 3
        wire = key & 7
        if wire == 0:
            item = 128
            num = 0
            left = 0
            while item & 128:
                item = data[index]
                index += 1
                value = (item & 127) << left
                num += value
                left += 7
            continue
        elif wire == 1:
            index += 8
            continue
        elif wire == 2:
            item = 128
            _length = 0
            left = 0
            while item & 128:
                item = data[index]
                index += 1
                value = (item & 127) << left
                _length += value
                left += 7
            last = index
            index += _length
            item = data[last:index]
            if field not in proto:
                continue
            msg[proto[field]] = item
            continue
        elif wire == 5:
            index += 4
            continue
        raise ValueError(
            'invalid wire type: {wire}'.format(wire=wire)
        )
    return msg

# Code source: https://stackoverflow.com/a/52263105/404421
# Modified so it works with Python 3.
# Works with CRXv3.
def get_extension_id(crx_file):
    with open(crx_file, 'rb') as f:
        f.read(8) # 'Cr24\3\0\0\0'
        data = f.read(struct.unpack('<I', f.read(4))[0])
    crx3 = decode(
        {10000: "signed_header_data"},
        [d for d in data])
    signed_header = decode(
        {1: "crx_id"},
        crx3['signed_header_data'])
    return str.translate(
        binascii.hexlify(bytearray(signed_header['crx_id'])).decode("utf-8") ,
        bytes.maketrans(b'0123456789abcdef', string.ascii_lowercase[:16].encode('utf-8')))

def extract_extenson_id_demo(crx_file_path: str):
    if not os.path.isabs(crx_file_path):
        crx_file_path = os.path.abspath(crx_file_path)
    print(f'Extension ID = {get_extension_id(crx_file_path)}')

    # extract_id(crx_file_path)