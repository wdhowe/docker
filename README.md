# Docker

Applications deployed in docker.

----

## Directories

* flask_demo -> A simple flask application using restful APIs.
* packer-build -> Alpine image with Packer and Ansible
* py3shtester -> Alpine image with python and shell lint/testing software.
* py3tester -> Python3 image with packages for testing python code.
* terraform-aws-tester -> Amazon Linux image with Terraform and AWS provider installed.

----

## Image Running/Building Examples

The docker images can all be run/built similar to the following.

### Variables

Setup the variables per image.

GitHub Example

```bash
registry="docker.io/"
image_path="myuser/"
image_name="myimage"
tag_name="latest"
image="${registry}${image_path}${image_name}:${tag_name}"
```

GitLab Example

```bash
registry="mygitlab.example.com:4567/"
image_path="mygroup/myproject/"
image_name="myimage"
tag_name="latest"
image="${registry}${image_path}${image_name}:${tag_name}"
```

### Run the image

To run an image manually from the command line:

```bash
docker run -it --rm --name testing ${image} /bin/sh
```

To run an image and mount your current working directry into the image for use (at /mnt)

```bash
docker run -it --rm --name testing -v ${PWD}:/mnt ${image} /bin/sh
```

----

### How to Build a Docker Image Manually

* Build image using a Dockerfile (in the current directory)

```bash
docker build -t ${image_name}:${tag_name} .
```

* Run a test container from the built image to verify

```bash
docker run -it --rm --name testing ${image_name}:${tag_name} /bin/sh
```

* Tag the local image in preparation for a remote registry push

```bash
docker tag ${image_name}:${tag_name} ${image}
```

* Login to the remote registry (prompted for registry username/password)

```bash
docker login https://${registry}
```

* Push to the remote registry

```bash
docker push ${image}
```

* Optional: Additional tag latest and push

```bash
docker tag ${image_name}:${tag_name} ${registry}${image_path}${image_name}:latest
docker push ${registry}${image_path}${image_name}:latest
```

----
