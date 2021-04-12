##-- Environment Variables --#

# Docker image information
IMAGE_NAME := clojure-dev
IMAGE_PATH := wdhowe
IMAGE      := $(IMAGE_PATH)/$(IMAGE_NAME)

# Docker image tag for a local build
BUILD_TAG := $(IMAGE):build

# Docker volume name setup
DOCKER_VOL := git-repos
CONTAINER_MOUNT := /repos

# Get current branch and transform '/' to '-'
BRANCH := $(or $(CI_COMMIT_REF_NAME), `git rev-parse --abbrev-ref HEAD`)
BRANCH := $(shell echo $(BRANCH) | tr / -)

# Retrieve first 7 characters of current commit hash
SHORT_HASH := `git rev-parse --short HEAD`

# Docker image tag that will be pushed to the registry
TAG := $(IMAGE):$(BRANCH)-$(SHORT_HASH)

##-- Makefile Targets --##

# build - build a jar, local docker image, and tag the image
build: docker-build docker-tag

# volume - create the local volume for development.
volume:
	docker volume create $(DOCKER_VOL)

# shell - open a shell on the local build with a volume mount.
shell:
	docker run -it --mount source=$(DOCKER_VOL),target=$(CONTAINER_MOUNT) --name $(IMAGE_NAME)-testing $(BUILD_TAG) /bin/bash

# deploy - push image into registry
deploy: docker-login docker-push

# run - run the container from the published version with a volume mount.
run:
	docker run -it --mount source=$(DOCKER_VOL),target=$(CONTAINER_MOUNT) --name $(IMAGE_NAME) $(TAG) /bin/bash

##-- Docker Build/Deploy Helpers --##

# docker-build - build an image with a local build tag
docker-build:
	docker build --tag $(BUILD_TAG) --rm --compress $(PWD)

# docker-tag - prep local built image with tag for pushing to registry
docker-tag:
	docker tag $(BUILD_TAG) $(TAG)

# docker-login - login to registry using vars if available,
#                otherwise interactive login.
docker-login:
	@$(if $(and $(CI_REGISTRY_USER), $(CI_REGISTRY_PASSWORD)), \
		docker login -u $(CI_REGISTRY_USER) -p $(CI_REGISTRY_PASSWORD), \
		docker login)

# docker-push - push image to registry
docker-push:
	docker push $(TAG)

##-- Debug --##

# debug - display all environment variables
debug:
	@echo "IMAGE:     $(IMAGE)"
	@echo "BUILD_TAG: $(BUILD_TAG)"
	@echo "TAG:       $(TAG)"
	@echo "DOCKER_VOL" $(DOCKER_VOL)
	@echo "CONTAINER_MOUNT" $(CONTAINER_MOUNT)
