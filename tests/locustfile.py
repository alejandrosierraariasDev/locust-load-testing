from locust import HttpUser, task
from locust import events
from prometheus_client import start_http_server, Counter

# Empieza el servidor Prometheus para exponer métricas en puerto 8001
start_http_server(8001)

# Define un contador Prometheus
REQUEST_COUNTER = Counter('locust_requests_total', 'Total requests made by Locust')

class ApiUser(HttpUser):
    host = "https://httpbin.org"

    @task
    def hello_world(self):
        self.client.get("/get")
        self.client.get("/status/200")


print("DEBUG EVENTS:", dir(events))
@events.request.add_listener
def on_request(request_type, name, response_time, response_length, response, context, exception, **kwargs):
    if exception is None:
        REQUEST_COUNTER.inc()
