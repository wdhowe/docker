# Docker - py3shtester

Alpine image with packages for linting/testing shell and python code.

Dockerhub: [https://hub.docker.com/r/wdhowe/py3shtester](https://hub.docker.com/r/wdhowe/py3shtester)

----

## Image Building

Build the Image from the Dockerfile

```bash
docker build -t py3shtester:tagname .
```

Run the Container

```bash
docker run -it --name py3shtester-tmp py3shtester:tagname /bin/sh
```
