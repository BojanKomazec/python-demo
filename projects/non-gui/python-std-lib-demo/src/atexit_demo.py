#
# https://docs.python.org/3/library/atexit.html
#
import atexit

def onExit():
    print(f'Hello from onExit()')

def onExit2(name):
    print(f'Hello {name} from onExit2()')

def atexit_demo():
    print('Registering atexit callback...')
    atexit.register(onExit)
    atexit.register(onExit2, 'Bojan')
    #
    # At normal program termination (for instance, if sys.exit() is called or the main module’s execution completes),
    # all functions registered are called in last in, first out order.
    # So the output is:
    #
    # Registering atexit callback...
    # Hello Bojan from onExit2()
    # Hello from onExit()