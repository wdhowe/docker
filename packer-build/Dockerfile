## Dockerfile to build an image for Packer image builds

# Start with an Alpine (Edge/3.11) Docker Hub Image
FROM alpine:edge

# Install packer
RUN wget https://releases.hashicorp.com/packer/1.5.4/packer_1.5.4_linux_amd64.zip && \
    unzip packer_1.5.4_linux_amd64.zip && \
    mv packer /usr/local/bin/ && \
    chmod +x /usr/local/bin/packer && \
    rm -f packer_1.5.4_linux_amd64.zip

# Install Ansible, a common packer provisioner
RUN apk add ansible

