
name = "Bjan"
surname = "Kmzec"

def print_name_surname(name, surname):
    print(f'name = {name}, surname = {surname}')

def change_global_variables():
    # print(f'name = {name}')
    # error: Using variable 'name' before assignment
    # This happens as in this scope we haven't defined variable 'name' and we're not using 'global name'

    # this introduces a local variable which overshadows the global one with the same name
    # so we actually don't change the value of the global variable
    name = 'Bojan'
    print(f'name = {name}')
    # name = Bojan

    # use keyword 'global' to refer to the global variable
    global surname
    surname = 'Komazec'
    print(f'surname = {surname}')
    # surname = Komazec

def global_variable_demo():
    change_global_variables()

    global name, surname
    print_name_surname(name, surname)
    # name = Bjan, surname = Komazec

def variables_demo():
    global_variable_demo()