import string

def bytes_demo():
    # Python 3: indexing a bytes object returns an integer
    n = b'DCAB'[2]
    print(n) # 65
    print(type(n)) # <class 'int'>

def bytes_to_bytearray_conversion_demo():
    b = b'test'
    ba = bytearray(b)
    print(ba) # bytearray(b'test')
    print({type(ba)}) # {<class 'bytearray'>}

# Python strings are Unicode
def string_conversions_demo():
    str1 = 'test'
    str2 = 'Бојан'

    # convert string to object of bytes type
    encoding = 'utf-8' # or UTF-8
    b1 = str1.encode(encoding)
    print(b1) # b'test'
    print({type(b1)}) # {<class 'bytes'>}

    b2 = str2.encode(encoding)
    print(b2) # b'\xd0\x91\xd0\xbe\xd1\x98\xd0\xb0\xd0\xbd'

    # decode first 4 bytes with utf-8 decoding
    str3 = b2[:4].decode(encoding)
    print(str3) # Бо

    # another way to decode bytes into a string:
    str4 = str(b2[4:], encoding)
    print(str4) # јан

# https://docs.python.org/3/library/stdtypes.html#str.maketrans
# https://docs.python.org/3/library/stdtypes.html#str.translate
def string_translations_demo():
    table = str.maketrans('abc', 'xyz')
    s1 = 'a1b2c3'
    s2 = s1.translate(table)
    print(s2) #x1y2z3

def strings_demo():
    # print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
    # string_conversions_demo()
    string_translations_demo()

def types_demo():
    # bytes_demo()
    strings_demo()
    # bytes_to_bytearray_conversion_demo()