# Docker - clojure-dev

A docker container for Clojure development.

----

## Image Building

### Build/Run

A Makefile has been provided for ease of use. See the contents for more details.

Check settings

```bash
make debug
```

Build the Image from the Dockerfile

```bash
make build
```

Run with a volume mount for persistent git projects.

```bash
# create the volume (first time only).
make volume

# run the local build dev container and use the volume.
make shell

# run the branch tagged version meant for publishing and use the volume.
make run
```

- The docker volume is now mounted in the running container at /repos.
- The volume and any data written to it will persist even if the container is stopped and removed.
- Simply run a new container with the 'make shell' command above to use the volume again.
