# prometheus-grafana-example
Prometheus + Grafana monitoring a FastAPI app called by Locust

## Getting started

Begin with

```
docker compose up --build -d 
```

Wait for all services to get up and running and navigate to:

- http://localhost:8089/ for the Locust UI,
- http://localhost:9090/graph for the Prometheus UI,
- http://localhost:3000/ for Grafana.

For any metrics to appear in Prometheus, you need to start a Locust load test.