import string
from enum import Enum

#
# bytes
#

def bytes_demo():
    # Python 3: indexing a bytes object returns an integer
    n = b'DCAB'[2]
    print(n) # 65
    print(type(n)) # <class 'int'>

#
# bytearray
#

def bytes_to_bytearray_conversion_demo():
    b = b'test'
    ba = bytearray(b)
    print(ba) # bytearray(b'test')
    print({type(ba)}) # {<class 'bytearray'>}

#
# Enumerations
#

class Brand(Enum):
    BRAND_A = "BrandA"
    BRAND_B = "BrandB"
    BRAND_C = "BrandC"

def iterate_through_enum_demo():
    for e in Brand:
        print(f'name = {e.name}, value = {e.value}')
    # Expected output:
    # name = BRAND_A, value = BrandA
    # name = BRAND_B, value = BrandB
    # name = BRAND_C, value = BrandC

def enum_demo():
    iterate_through_enum_demo()
    if "BrandC" == Brand.BRAND_C.value:
        print(f'Brand.BRAND_C.name = {Brand.BRAND_C.name}') # BRAND_C
        print(f'Brand.BRAND_C.value = {Brand.BRAND_C.value}') # BrandC


#
# Strings
#

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

def list_append_vs_extend_demo():
    listA = []
    print(f'listA = {listA}')

    # IndexError: list assignment index out of range
    # listA[0] = 'Ana'
    listA.append('Ana')
    print(f'listA = {listA}')

    listB = ['Bella', 'Cynthia']
    print(f'listB = {listB}')

    listA.append(listB)
    print(f'listA (after appending listB) = {listA}')

    listC = ['Donna', 'Emanuela']
    print(f'listC = {listC}')

    listA.extend(listC)
    print(f'listA  (after extending with listC) = {listA}')

def lists_demo():
    list_append_vs_extend_demo()

def types_demo():
    # bytes_demo()
    # enum_demo()
    lists_demo()
    # strings_demo()
    # bytes_to_bytearray_conversion_demo()