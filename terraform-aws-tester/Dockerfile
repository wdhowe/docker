## Dockerfile to build an image for Terraform tests/deploys

# Start with an AmazonLinux:Latest Docker Hub Image
FROM amazonlinux:latest

RUN yum -y install unzip wget

# Install terraform
RUN wget https://releases.hashicorp.com/terraform/0.12.21/terraform_0.12.21_linux_amd64.zip && \
    unzip terraform_0.12.21_linux_amd64.zip && \
    mv terraform /usr/local/bin/ && \
    chmod +x /usr/local/bin/terraform && \
    rm -f terraform_0.12.21_linux_amd64.zip

# Install aws provider
RUN wget https://releases.hashicorp.com/terraform-provider-aws/2.51.0/terraform-provider-aws_2.51.0_linux_amd64.zip && \
    unzip terraform-provider-aws_2.51.0_linux_amd64.zip && \
    mkdir -p /opt/tf-plugins && \
    mv terraform-provider-aws_v2.51.0_x4 /opt/tf-plugins/ && \
    rm -f terraform-provider-aws_2.51.0_linux_amd64.zip

