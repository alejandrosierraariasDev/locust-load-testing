FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
# Expose ports for Locust web UI and Prometheus exporter
EXPOSE 8089 8000
# Default command to run Locust in headless mode,
CMD ["locust", "-f", "tests/locustfile.py", "--headless", "-u", "10", "-r", "1", "--run-time", "1m", "--host", "http://localhost", "--web-port", "8089"]
