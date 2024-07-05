import os

class Config:
    def __init__(self):
        self._python_env = os.getenv("PYTHON_ENV")
        self._schemas_dir = os.getenv("SCHEMAS_DIR")
        self._db_host = os.getenv("DB_HOST")
        self._db_name = os.getenv("DB_NAME")
        self._db_user = os.getenv("DB_USER")
        self._db_password = os.getenv("DB_PASSWORD")

    @property
    def python_env(self):
        return self._python_env

    @property
    def schemas_dir(self):
        return self._schemas_dir

    @property
    def db_host(self):
        return self._db_host

    @property
    def db_name(self):
        return self._db_name

    @property
    def db_user(self):
        return self._db_user

    @property
    def db_password(self):
        return self._db_password
