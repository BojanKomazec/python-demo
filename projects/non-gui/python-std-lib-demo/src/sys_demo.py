import sys

def read_command_line_args_demo():
    print(f'Number of arguments: {len(sys.argv)} arguments.')
    print(f'Argument List: {str(sys.argv)}')
    print(f'sys.argv[0] = {sys.argv[0]}')
    print(f'sys.argv[1] = {sys.argv[1]}')
    print(f'sys.argv[2] = {sys.argv[2]}')
    # An example of simple CLA parser
    if len(sys.argv) != 3:
        print("Usage: python_demo.py <source_dir> <dest_dir>")
        print("       <source_dir> - directory that contains input resources")
        print("       <dest_dir> - directory that should contain generated output resources") # can be ./
        exit()
#
# $ python python_demo.py 123 test
# Number of arguments: 3 arguments.
# Argument List: ['python_demo.py', '123', 'test']
# sys.argv[0] = python_demo.py
# sys.argv[1] = 123
# sys.argv[2] = test



def sys_demo():
    read_command_line_args_demo()