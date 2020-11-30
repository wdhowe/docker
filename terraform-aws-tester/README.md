# Docker - terraform-aws-tester

Image with Terraform and AWS provider.

Dockerhub: [https://hub.docker.com/r/wdhowe/terraform-aws-tester](https://hub.docker.com/r/wdhowe/terraform-aws-tester)

----

## Image Building

Build the Image from the Dockerfile

```bash
docker build -t terraform-aws-tester:tagname .
```

Run the Container

```bash
docker run -it --name terraform-aws-tester-tmp terraform-aws-tester:tagname /bin/bash
```
