import subprocess

def call_bash_script_with_no_args():
    file_path = './test_scripts/test.sh'
    try:
        subprocess.call(file_path)
    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except PermissionError:
        print(f'No permissions to run {file_path}')
        # To fix this error, run:
        # $ sudo chmod +x ./data/test.sh
    except:
        print(f'Unknown error occured when trying to run {file_path}')
    finally:
        print('~call_bash_script_with_no_args()')

def call_bash_script_with_args():
    file_path = './test_scripts/test.sh'
    try:
        # This throws generic exception:
        # subprocess.call(file_path, 'Bojan')
        subprocess.call([file_path, 'Bojan'])
    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except PermissionError:
        print(f'No permissions to run {file_path}')
        # To fix this error, run:
        # $ sudo chmod +x ./data/test.sh
    except:
        print(f'Unknown error occured when trying to run {file_path}')
    finally:
        print('~call_bash_script_with_args()')


def subprocess_demo():
    call_bash_script_with_no_args()
    call_bash_script_with_args()