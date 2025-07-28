#!/bin/bash

# Test script for Docker build and execution
set -e

echo "🐳 Testing Docker build and execution..."

# Build the Docker image
echo "📦 Building Docker image..."
docker build -t hybrid-retrieval-system .

# Test with Collection 1
echo "🧪 Testing with Collection 1..."
docker run --rm -v $(pwd)/Challenge_1b:/app/Challenge_1b hybrid-retrieval-system python src/run_pipeline.py --collection 1 --debug

# Test with Collection 2
echo "🧪 Testing with Collection 2..."
docker run --rm -v $(pwd)/Challenge_1b:/app/Challenge_1b hybrid-retrieval-system python src/run_pipeline.py --collection 2 --debug

# Test with Collection 3
echo "🧪 Testing with Collection 3..."
docker run --rm -v $(pwd)/Challenge_1b:/app/Challenge_1b hybrid-retrieval-system python src/run_pipeline.py --collection 3 --debug

echo "✅ All Docker tests completed successfully!" 