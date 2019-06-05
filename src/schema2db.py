import json
import os
import psycopg2

# pylint: disable=import-error
from dotenv import load_dotenv
from json import JSONDecodeError
from jsonschema2db import JSONSchemaToPostgres
from src.config import Config

def schema2db():
    load_dotenv(verbose=True)
    config = Config()

    schema_file_names = os.listdir(config.schemas_dir)
    schema_file_names.sort()

    con = psycopg2.connect(f'host={config.db_host} dbname={config.db_name} user={config.db_user} password={config.db_password}')

    for schema_file_name in schema_file_names:
        try:
            json_schema = json.load(open(os.path.join(config.schemas_dir, schema_file_name)))
        except JSONDecodeError:
            print("Failed to decode file as JSON. File:", schema_file_name)
            continue

        db_schema_name = schema_file_name.rsplit('.', 2)[0]
        print("db_schema_name =", db_schema_name)
        translator = JSONSchemaToPostgres(json_schema, postgres_schema=db_schema_name, debug=True)
        translator.create_tables(con)

    con.commit()
    con.close()
