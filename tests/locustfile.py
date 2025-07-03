from locust import HttpUser, task, events
from prometheus_client import CollectorRegistry, Counter, push_to_gateway

registry = CollectorRegistry()
REQUEST_COUNTER = Counter('locust_requests_total', 'Total requests made by Locust', registry=registry)

class ApiUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")


@events.request_success.add_listener
def on_request_success(request_type, name, response_time, response_length, **kwargs):
    REQUEST_COUNTER.inc()


