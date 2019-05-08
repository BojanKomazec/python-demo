FROM python:3-alpine

WORKDIR /usr/src/python-demo

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./python_demo.py" ]
