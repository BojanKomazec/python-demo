## Prerequisites:

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
