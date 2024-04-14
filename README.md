# techwide
TechWide is an experimental project for exploring and integrating various technologies.

## General
All modules run via [docker-compose](./docker-compose.yaml).

Just run:
```bash
docker-compose up
```

### Docker

`Docker` is for simplifying running, installing all dependencies within a container, and isolating it from the base host.


## Modules

### Simple web server: HTTP API

A `Python` app with `FastAPI` (https://fastapi.tiangolo.com/) runs on the `Uvicorn` web server.


### SQL server
We currently use a simple SQL server for relational models – `SQLite`.

Run via docker-compose separatly:
```bash
docker-compose up sqlite
```


## Nosql

### Redis

Add simple docker conatainer with Redis for caching
