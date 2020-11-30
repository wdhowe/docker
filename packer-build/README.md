# Docker - packer-build

Alpine image with Packer and Ansible.

Dockerhub: [https://hub.docker.com/r/wdhowe/packer-build](https://hub.docker.com/r/wdhowe/packer-build)

----

## Image Building

Build the Image from the Dockerfile

```bash
docker build -t packer-build:tagname .
```

Run the Container

```bash
docker run -it --name packer-build-tmp packer-build:tagname /bin/bash
```
