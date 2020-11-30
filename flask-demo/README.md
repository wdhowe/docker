# Docker - flask_demo

A simple flask application in docker.

Demonstrates a systems list with restful APIs.

----

## Image Building

Build the Image from the Dockerfile

```bash
docker build -t flasktest:0.3 .
```

Run the Container

```bash
docker run -d -p 5000:5000 flasktest:0.3
```

## Flask API Queries

Get Existing Entry

```bash
curl http://127.0.0.1:5000/systems/server01
```

Modify Existing Entry

```bash
curl --request PUT --url http://127.0.0.1:5000/systems/server02 --form 'os=Ubuntu 16.04'
```

Create New Entry

```bash
curl --request POST --url http://127.0.0.1:5000/systems/server03 --form 'os=Ubuntu 18.04'
```
