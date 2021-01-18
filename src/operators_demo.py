import math

def power_operator_demo():
    print(f'10 raised to the power of 2: 10**2 = {10**2}')

    # using built-in function
    print(f'10 raised to the power of 2: pow(10, 2) = {pow(10, 2)}')

    # using math.pow() function: converts both arguments to float and returns float
    print(f'10 raised to the power of 2: math.pow(10, 2) = {math.pow(10, 2)}')

# caret
def xor_operator_demo():
    print(f'0 xor 0: 0^0 = {0^0}')
    print(f'0 xor 1: 0^1 = {0^1}')
    print(f'1 xor 0: 1^0 = {1^0}')
    print(f'1 xor 1: 1^1 = {1^1}')

def math_operators_demo():
    power_operator_demo()
    xor_operator_demo()

def operators_demo():
    math_operators_demo()