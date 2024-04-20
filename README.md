# techwide
TechWide is an experimental project for exploring and integrating various technologies.

<!-- https://github.com/marwin1991/profile-technology-icons -->
| <img width="24" src="https://user-images.githubusercontent.com/25181517/182884894-d3fa6ee0-f2b4-4960-9961-64740f533f2a.png" alt="redis" title="redis"/>
| <img width="24" src="https://github.com/marwin1991/profile-technology-icons/assets/136815194/82df4543-236b-4e45-9604-5434e3faab17" alt="SQLite" title="SQLite"/>
| <img width="24" src="https://user-images.githubusercontent.com/25181517/117207330-263ba280-adf4-11eb-9b97-0ac5b40bc3be.png" alt="Docker" title="Docker"/>
| <img width="24" src="https://user-images.githubusercontent.com/25181517/182534075-4962068b-4407-46c2-ac67-ddcb86af30cc.png" alt="Grafana" title="Grafana"/>
| <img width="24" src="https://user-images.githubusercontent.com/25181517/182534182-c510199a-7a4d-4084-96e3-e3db2251bbce.png" alt="Prometheus" title="Prometheus"/>
|

## General
Some modules run via [docker-compose](./docker-compose.yaml) or local docker compose file in modules.

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

## Monitoring

To run monitoring module run command from root:
```
docker-compose -f monitoring/docker-compose.yaml up -d
```

### Prometheus

By default prometheus will be starts on port 9090 and port will be forward to host, 
so use link http://localhost:9090

### Grafana

By default grafana will be starts on port 3000 and port will be forward to host,
so use link http://localhost:9090

## Nosql

### Redis

Add simple docker conatainer with Redis for caching


## PubSub

Simple pub-sub module via Redis channel

To run:

```
docker-compose -f pubsub/docker-compose.yaml up
```
