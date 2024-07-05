import glob
import os

script_path = os.path.dirname(os.path.abspath(__file__))

def find_file_regex():
    files = glob.glob(os.path.join(os.getcwd(),'demo_dir', 'demo_[file|document]_0[1-4].txt'))
    print(f'files={files}')

def glob_demo():
    find_file_regex()
