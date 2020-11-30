# Docker - py3tester

Python3 image with packages for testing python code.

Dockerhub: [https://hub.docker.com/r/wdhowe/py3tester](https://hub.docker.com/r/wdhowe/py3tester)

----

## Image Building

Build the Image from the Dockerfile

```bash
docker build -t py3tester:tagname .
```

Run the Container

```bash
docker run -it --name py3tester-tmp py3tester:tagname /bin/bash
```
