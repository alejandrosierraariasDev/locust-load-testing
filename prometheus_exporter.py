from prometheus_client import start_http_server, Counter
import time


REQUEST_COUNT = Counter('locust_request_count', 'Number of requests processed')

if __name__ == "__main__":
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")

    while True:
        time.sleep(1)
