#!/bin/bash

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
REPORT_DIR="reports/$TIMESTAMP"
mkdir -p "$REPORT_DIR"

echo "Starting Prometheus metrics server..."
python prometheus_exporter.py &
PROMETHEUS_PID=$!

echo "Starting Locust load test..."
locust -f tests/locustfile.py --headless -u 100 -r 10 --run-time 1m --html "$REPORT_DIR/report.html"

echo "Stopping Prometheus metrics server..."
kill $PROMETHEUS_PID

echo "Load test finished. Report saved in $REPORT_DIR/report.html"
