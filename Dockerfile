FROM python:3-alpine as python_base

# Required for installing psycopg2 (see https://github.com/psycopg/psycopg2/issues/684)
RUN apk update \
&& apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev \
&& pip install numpy
RUN which pip
RUN pip --version

FROM python_base as opencv_base
RUN apk update \
# --no-cache = do not cache the index locally (in order to keep container small)
# It equals apk update in the beginning and rm -rf /var/cache/apk/* in the end.
# https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management#Local_Cache
&& apk add --no-cache \
    clang \
    # without it make errors with: fatal error: 'emmintrin.h' file not found
    clang-dev \
    # without it cmake errors with: CMAKE_MAKE_PROGRAM is not set
    build-base \
    # bzip2-dev \
    cmake \
    # cmake-dev \
    # Alpine version of libgtk2.0-dev
    gtk+2.0-dev \
    # without it make errors with: fatal error: 'linux/auxvec.h' file not found
    linux-headers \
    # ninja
    # Alpine version of pkg-config
    pkgconfig

# ENV CC=clang
# ENV CXX=clang++
# ENV CC /usr/local/clang
# ENV CXX /usr/local/clang++

ENV OPENCV_VERSION="4.1.1"
RUN wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip \
&& unzip ${OPENCV_VERSION}.zip \
&& rm ${OPENCV_VERSION}.zip \
&& cd opencv-${OPENCV_VERSION} \
&& mkdir build \
&& cd build \
&& cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_CUDA=OFF \
    -D INSTALL_C_EXAMPLES=OFF \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    # if set to ON then opencv_contrib is required
    -D OPENCV_ENABLE_NONFREE=OFF \
    # -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D BUILD_EXAMPLES=OFF \
    -D CMAKE_C_COMPILER=/usr/bin/clang \
    -D CMAKE_CXX_COMPILER=/usr/bin/clang++ \
    .. \
&& make install
# RUN find /usr/local/lib/python3.7/site-packages -name cv2.*.so
RUN ls -la /usr/local/lib/python3.7/site-packages/cv2/
# RUN ls -la /usr/local/python/cv2/python-3.7/ # No such file or directory
#RUN ls -la /usr/local/lib/python3.7/site-packages/cv2/python-3.7
#RUN cp -p $(find /usr/local/lib/python3.7/site-packages -name cv2.*.so) /usr/lib/python3.7/site-packages/cv2.so
#RUN python -c 'import cv2; print("Python: import cv2 - SUCCESS")'
# RUN ln -s \
#   /usr/local/python/cv2/python-3.7/cv2.cpython-37m-x86_64-linux-gnu.so \
#   /usr/local/lib/python3.7/site-packages/cv2.so

ENV appDir /usr/local/src/python-demo
WORKDIR ${appDir}

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
# RUN pip3 install --no-cache-dir -r requirements.txt

FROM opencv_base
COPY . .
COPY src/ ./src
RUN pwd
CMD [ "python", "./python_demo.py", "--image", "images/example_01.png", "--coords", "[(73, 239), (356, 117), (475, 265), (187, 443)]" ]
