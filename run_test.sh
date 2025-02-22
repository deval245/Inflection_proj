#!/bin/bash

# Ensure the reports directory exists at the root level
mkdir -p ../reports

echo "🔥 Running Integration Tests..."
pytest Test/integration --html=../reports/test_integration_report.html --self-contained-html

echo "🔥 Running End-to-End Tests..."
pytest Test/end_to_end --html=../reports/test_end_to_end_report.html --self-contained-html

echo "✅ All tests executed. Reports available in '../reports/'"
