def _fn_uses_yield_to_return_scalar():
    yield 123

def _fn_uses_yield_to_return_multiple_values():
    yield 12
    yield 34
    yield 56

# Function can return a single item via yield but caller has to use iterator to read that value:
def _yield_scalar_demo():
    print(_fn_uses_yield_to_return_scalar())
    # output:
    # <generator object _fn_uses_yield_to_return_scalar at 0x7fe79c36d938>

    for value in _fn_uses_yield_to_return_scalar():
        print(value)
    # output:
    # 123

    for value in _fn_uses_yield_to_return_multiple_values():
        print(value)
    # output:
    # 12
    # 34
    # 56

def functions_demo():
    _yield_scalar_demo()
