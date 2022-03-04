import threading

def threading_demo():
    # start_thread_function()
    start_thread_function_1_arg()
    # start_thread_function_2_args()

def start_thread_function():
    thread = threading.Thread(target=thread_function, args=())
    thread.start()

def thread_function():
    print('thread_function()')
    print('~thread_function()')

def start_thread_function_1_arg():
    name = 'Bojan'

    # This fails with error:
    # TypeError: thread_function_1_arg() takes 1 positional argument but 5 were given
    # thread = threading.Thread(target=thread_function_1_arg, args=(name))
    # threading.Thread args argument expects an iterable (e.g. a tuple, a list,...) so
    # in this case every character from string 'Bojan' was passed as a separate
    # thread function argument.

    thread = threading.Thread(target=thread_function_1_arg, args=(name,))
    thread.start()

def thread_function_1_arg(name):
    print('thread_function_1_arg()')
    print(f'name = {name}')
    print('~thread_function_1_arg()')

def start_thread_function_2_args():
    thread_number = 1
    name = 'Bob'
    thread = threading.Thread(target=thread_function, args=(thread_number,name))
    thread.start()

def thread_function_2_args(thread_number, name):
    print('thread_function_1_arg()')
    print(f'thread_number = {thread_number}')
    print(f'name = {name}')
    print('~thread_function_1_arg()')