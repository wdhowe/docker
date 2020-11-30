## Dockerfile to build an image for
## checking syntax and security of shell/python scripts

# Start with an Alpine (Edge) Docker Hub Image
FROM alpine:edge

# Install Python3 development packages (required to build pip packages)
# shellcheck - bash linting
# bats - Bash Automated Testing System
RUN apk update && apk add --no-cache make python3 python3-dev gcc musl-dev shellcheck bats

# Ensure pip is installed and the latest
RUN python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel

# Install python packages
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt