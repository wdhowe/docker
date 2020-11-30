# Docker - clojure-lein

Generalized openjdk-lein image that will build and run any lein based Clojure uberjar.

----

## Image Building

### Pre-Reqs

* Create a Clojure lein project.
* Copy the Dockerfile in this directory into your project.

### Build/Run

Build the Image from the Dockerfile

```bash
docker build -t project-name:tagname .
```

Run the Container

```bash
docker run -it --name project-name-tmp project-name:tagname /bin/bash
```
