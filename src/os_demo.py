import os

# os.getenv(key, default_value)
#
# This method returns a string that denotes the value of the environment variable key.
# In case key does not exists it returns the value of default parameter.
#
# To test this function execute this applicationi as this:
# $ TEST_ENV_VAR_SET_TO_TRUE=True TEST_ENV_VAR_SET_TO_FALSE=False python3 ./python_demo.py
def os_getenv_demo():
    test_env_var_set_to_true = os.getenv("TEST_ENV_VAR_SET_TO_TRUE", "True").lower() in ["true", "1"]
    test_env_var_set_to_false = os.getenv("TEST_ENV_VAR_SET_TO_FALSE", "True").lower() in ["true", "1"]
    test_env_var_set_to_not_set_at_all = os.getenv("TEST_ENV_VAR_NOT_SET_AT_ALL", "True").lower() in ["true", "1"]

    print(f'test_env_var_set_to_true = {test_env_var_set_to_true}') # True
    print(f'test_env_var_set_to_false = {test_env_var_set_to_false}') # False
    print(f'test_env_var_set_to_not_set_at_all = {test_env_var_set_to_not_set_at_all}') # True

def file_creation_demo():
    with open("do-not-commit.txt", "w") as file:
        file.write("This file should not be\n")
        file.write("added to the repository")

def get_working_directory_demo():
    print(f'Working directory = {os.getcwd()}')

# TODO: create demo for:
# os.path.join

def os_demo():
    # os_getenv_demo()
    # file_creation_demo()
    get_working_directory_demo()