import time

from random import random

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from prometheus_client import Counter, Histogram, make_asgi_app

app = FastAPI()

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

c_total_requests = Counter("requests", "Total number of requests")
c_failed_requests = Counter("failed_requests", "Number of failed requests", ["status_code"])
c_failed_requests.labels("418")
c_failed_requests.labels("420")
h_latency = Histogram("request_latency_seconds", "Request latency in seconds")


@app.get("/")
async def root():
    number = random()
    time.sleep(number / 10 + 0.05)
    if number < 0.001:
        raise HTTPException(status_code=420, detail="Blaze it")
    if number < 0.1:
        raise HTTPException(status_code=418, detail="I'm a teapot")

    return {"message": "OK!"}


@app.middleware("http")
async def log_metrics(request: Request, call_next):
    with h_latency.time():
        c_total_requests.inc()
        response = await call_next(request)

    return response


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    c_failed_requests.labels(status_code=str(exc.status_code)).inc()
    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)
