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

#
# Tuples
#

def tuple_demo():
    tuple1 = 1, 2
    print(f'tuple1 = {tuple1}')
    # tuple1 = (1, 2)

    # initializer can also be in form (...) where items are listed within curly brackets
    # tuple can contain an arbitrary number of items which can be of different types
    tuple2 = (3, 'a', 'abba', 4)
    print(f'tuple2 = {tuple2}')
    # tuple2 = (3, 'a', 'abba', 4)

    # iterating over tuple
    for x in tuple2:
        print(x)

    # get number of elements in tuple
    print(f'len(tuple2) = {len(tuple2)}')

    #
    # UNPACKING is a feature in Python which allows us to assign/pack all values/arguments
    # of a sequence into a single variable.
    #
    # unpacking a tuple:
    # SyntaxError: can't use starred expression here
    # upack1 = *tuple2

    item1, item2, item3, item4 = tuple2
    print(f'item1 = {item1}, item2 = {item2}, item3 = {item3}, item4 = {item4}')
    # item1 = 3, item2 = a, item3 = abba, item4 = 4

    # If the number of variables is less than the number of values, you can add an * to
    # the variable name and the values will be assigned to the variable as a list
    item1, *item2, item3 = tuple2
    print(f'item1 = {item1}, item2 = {item2}, item3 = {item3}')
    # item1 = 3, item2 = ['a', 'abba'], item3 = 4


#
# Dictionaries
#
# Python v3.7+: Dictionary order is guaranteed to be insertion order.
# Dict values are accessible by keys, which could be of any immutable type.
# https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/

def dict_demo():
    # creating an empty dictionary
    dict1 = dict()
    print(f'type(dict1) = {type(dict1)}')
    print(f'dict1 = {dict1}')

    # adding a new key-value pair
    dict1['name'] = 'Boki'
    print(f'dict1 = {dict1}')

    # updating the value of the existing key
    dict1['name'] = 'Bojan'

    # retrieving the value of a key (via get function)
    print(f'dict1.get(\'name\') = {dict1.get("name")}')
    # retrieving the value of a key (via indexing operator)
    print(f'dict1[\'name\'] = {dict1["name"]}')

    # checking if key exists:
    keyName = 'non-existing-key'
    if dict1.get(keyName) == None:
        print(f'key {keyName} does not exist')

    # NOTE (!)
    # The following expresson can't be used to check key existance:
    #   if dict1['non-existing-key'] == None:
    #
    # This is because indexing operator throws exception
    # if key does not exist: KeyError: 'non-existing-key'

    # initilization
    dict2 = dict({'name': 'Jon', 'surname':'Smith'})
    print(f'dict2 = {dict2}')

    # initialization (shorter version)
    dict3 = dict(name='Jon', surname='Smith', age=35)
    print(f'dict3 = {dict3}')

    #
    # keys can be of different type
    #

    dict4 = dict({'name': 'Rebecca', 1:'employee'})
    print(f'dict4 = {dict4}')

    # SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
    # dict4 = dict(name='Rebecca', 1='employee')

    # iterating over a dictionary
    for key in dict3:
        print(key)

    #
    # unpacking a dictionary
    #
    # If we unpack a dictionary using a single asterisk operator,
    # we only get the unpacked form of the dictionary’s keys.
    # To unpack the key as well as the values together, we use the double-asterisk operator.
    #
    # TypeError: type() takes 1 or 3 arguments
    # print(f'type(*dict3) = {type(*dict3)}')
    # SyntaxError: can't use starred expression here
    # unpck = *dict3
    item1, *item2 = dict3
    print(f'item1 = {item1}, item2 = {item2}')
    # item1 = name, item2 = ['surname', 'age']


def foo(a):
    print({type(a)})
    print(f'a = {a}')

#
# Types of Function arguments in Python:
#
# - Positional Arguments – The arguments that can be called by their position in the function definition.
#       When the function is, called the first positional argument must be provided first, the second
#       positional argument must be provided second, and so on.
#
# - Named (Keyword) Arguments – The arguments that can be called using their name. It is generally followed by an
#       equal sign and an expression to provide it a default value.
#

# https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
#
# Converts input into a tuple and treats it as such.
# If tuple of dictionary are not unpacked they are treated as the first item in a tuple.
def foo2(*args):
    print('\nfoo2()')
    print({type(args)})
    print(f'args = {args}')
    print(f'len(args) = {len(args)}')

    for x in args:
        print(x)
    print('~foo2()\n')

# Allows an arbitrary number of keyword arguments into our function.
# We can use ** to unpack map-like objects and pass them unpacked to this function.
# Argument after ** must be a mapping.
def foo3(**kwargs):
    print('\nfoo3()')
    print({type(kwargs)})
    print(f'kwargs = {kwargs}')
    print(f'len(kwargs) = {len(kwargs)}')

    for key in kwargs:
        print(f'key = {key}, value = {kwargs[key]}')
    print('~foo3()\n')


def passing_tuples_to_functions_demo():
    tuple1 = 1, '2', "three"
    foo(tuple1)

    # pass original (packed) tuple
    foo2(tuple1)
    # foo2()
    # {<class 'tuple'>}
    # args = ((1, '2', 'three'),) <-- tuple is passed as the first item in a tuple
    # len(args) = 1
    # (1, '2', 'three')
    # ~foo2()

    # pass unpacked tuple
    foo2(*tuple1)
    # foo2()
    # {<class 'tuple'>}
    # args = (1, '2', 'three') <-- every tuple item is now passed as a separate argument
    # len(args) = 3
    # 1
    # 2
    # three
    # ~foo2()

    # TypeError: foo2() argument after ** must be a mapping, not tuple
    # foo2(**tuple1)

    # TypeError: foo3() takes 0 positional arguments but 1 was given
    # foo3(tuple1)


def passing_dictionaries_to_functions_demo():
    dict1 = dict(name='Jon', surname='Smith', age=35)

    foo(dict1)
    # Terminal output:
    #   {<class 'dict'>}
    #   a = {'name': 'Jon', 'surname': 'Smith', 'age': 35}

    # TypeError: foo() takes 1 positional argument but 3 were given
    # foo(*dict1)

    # TypeError: foo() got an unexpected keyword argument 'name'
    # foo(**dict1)

    foo2(dict1)
    # foo2()
    # {<class 'tuple'>}
    # args = ({'name': 'Jon', 'surname': 'Smith', 'age': 35},)
    # len(args) = 1
    # {'name': 'Jon', 'surname': 'Smith', 'age': 35}
    # ~foo2()

    # Every iterable can be unpacked: *x unpacks variable x
    # Because iterating over a dictionary returns only its keys * unpacks only dictionary keys.
    # https://stackoverflow.com/questions/23268615/why-can-a-dictionary-be-unpacked-as-a-tuple
    foo2(*dict1)
    # foo2()
    # {<class 'tuple'>}
    # args = ('name', 'surname', 'age')
    # len(args) = 3
    # name
    # surname
    # age
    # ~foo2()

    # TypeError: foo2() got an unexpected keyword argument 'name'
    # foo2(**dict1)

    # TypeError: foo3() takes 0 positional arguments but 1 was given
    # foo3(dict1)

    # *dict1 unpacks only keys (not key-value pairs - named arguments, what is expected by foo3)
    # TypeError: foo3() takes 0 positional arguments but 3 were given
    # foo3(*dict1)

    foo3(**dict1)
    # foo3()
    # {<class 'dict'>}
    # kwargs = {'name': 'Jon', 'surname': 'Smith', 'age': 35}
    # len(kwargs) = 3
    # key = name, value = Jon
    # key = surname, value = Smith
    # key = age, value = 35
    # ~foo3()

    foo3(a=1, b=2, c=3)
    # foo3()
    # {<class 'dict'>}
    # kwargs = {'a': 1, 'b': 2, 'c': 3}
    # len(kwargs) = 3
    # key = a, value = 1
    # key = b, value = 2
    # key = c, value = 3
    # ~foo3()


def types_demo():
    # bytes_demo()
    # dict_demo()
    # passing_tuples_to_functions_demo()
    passing_dictionaries_to_functions_demo()
    # enum_demo()
    # lists_demo()
    # strings_demo()
    # bytes_to_bytearray_conversion_demo()
    # tuple_demo()