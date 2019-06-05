FROM python:3-alpine

ENV appDir /usr/local/src/python-demo
WORKDIR ${appDir}

# Required for installing psycopg2 (see https://github.com/psycopg/psycopg2/issues/684)
RUN apk update && apk add --no-cache postgresql-dev python3-dev gcc musl-dev

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
# COPY requirements.txt ./
# RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
COPY src/ ./src

CMD [ "python", "./python_demo.py" ]
