from locust import HttpUser, task, events
from prometheus_client import CollectorRegistry, Counter, push_to_gateway

registry = CollectorRegistry()
REQUEST_COUNTER = Counter('locust_requests_total', 'Total requests made by Locust', registry=registry)

class ApiUser(HttpUser):
    host = "https://httpbin.org"
    @task
    def hello_world(self):
        self.client.get("/get")
        self.client.get("/status/200")

def on_request_success(request_type, name, response_time, response_length, **kwargs):
    REQUEST_COUNTER.inc()

