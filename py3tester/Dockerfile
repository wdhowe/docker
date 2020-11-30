# Image for running python3 tests
FROM python:3

# Install virtualenv
RUN pip --no-cache-dir install virtualenv

# Virtual environment setup
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install python packages into virtualenv
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt

