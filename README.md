# python-demo
Python3 demo project
python
# Running on the native dev box OS

Prerequisites:

1) OpenCV (see https://www.bojankomazec.com/2019/11/how-to-install-opencv-on-ubuntu-1804.html)
https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/

Preferred way is to install it directly in virtual environment:
```
(venv) $ pip install opencv-contrib-python
```

To provide globally installed `cv2` package to virtual environment (here named `py3.6_cv2`):
```
$ cd ~/.virtualenvs/py3.6_cv2/lib/python3.6/site-packages/
$ ln -s /usr/local/lib/python3.6/site-packages/cv2/python-3.6/cv2.cpython-36m-x86_64-linux-gnu.so cv2.so
```

2) Other dependencies:
```
(venv) $ pip install -r requirements.txt
(venv) $ sudo apt install postgresql  postgresql-dev python-psycopg2 libpq-dev
(venv) $ pip install psycopg2 --upgrade
```

Application is capable of finding coordinates of corners so only image (jpeg or png) can be passed:
```
$ python python_demo.py --image="images/example_01.jpg"
```
If we pass coordinates, they will be respected:
```
$ python python_demo.py --image="images/example_01.png" --coords="[(73, 239), (356, 117), (475, 265), (187, 443)]"
```

# Runnung the app in Docker container
```
$ docker build -t python-demo . && docker run -it --rm --name python-demo python-demo
```

# schema2db

This module/tool performs the following sequence of actions:
* reads configuration from `.env` file or, if this file is absent, from system environment variables
* reads JSON schema files and for each of them creates table(s) in PostgreSQL database

# Configuration

schema2db reads current environment and other configuration from `.env` file.
Environment can take any of the following values: `dev`, `stage`, `beta`, `prod`.
This repository contains `.env.example` which provides an example of key-value pair(s) expected to be found in `.env` file.

# Input

Input are schema files. Their names have to be in the following form: `schema_name.schema.json`.
For test purposes, download https://github.com/better/jsonschema2db/blob/master/test/test_schema.json into `input_schemas_dev` and rename it to `test.schema.json`.

# Dependencies

[theskumar/python-dotenv](https://github.com/theskumar/python-dotenv) - package which manages reading from `.env` file

[better/jsonschema2db](https://github.com/better/jsonschema2db) - package which reads JSON schema and creates DB tables

All dependencies are listed in `requirements.txt`.

# Running & Verification

To run the application and database in containers execute:
```
docker-compose up
```

In another terminal run:
```
$ docker exec -it browser-schema2db_db_1 bash
```
...and use `psql` terminal to observe tables generated in the Postgres instance running in the container.


To see all databases run:
```
psql -l user=<db_user_name>
```

To connect to specific database use:
```
psql <database_name> <db_user_name
```

To list all schemas use:
```
\dn
```

To list all tables in a specific schema use:
```
\dt <schema_name>.*
```
Example:
```
\dt block_filterlist.*
```

To show the content (or just to verify generated columns) of some specific table in a given schema, use:
```
select * from <schema_name>.<table_name>;
```
Example:
```
select * from block_filterlist.root;
```
To exit psql terminal use:
```
\q
```

`schema_name` matches the name of the post type from WP API (e.g. "block_filterlist").

