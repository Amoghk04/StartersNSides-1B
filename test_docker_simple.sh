#!/bin/bash

echo "🐳 Testing Docker with specified input/output format..."

# Create test directories
mkdir -p input/PDFs output

# Copy test data
cp Challenge_1b/Collection_1/challenge1b_input.json input/
cp Challenge_1b/Collection_1/PDFs/*.pdf input/PDFs/

# Build Docker image
echo "📦 Building Docker image..."
docker build -t startersnsides:latest .

if [ $? -eq 0 ]; then
    echo "✅ Docker build successful!"
    
    # Test the container
    echo "🧪 Testing container..."
    docker run --rm \
        -v $(pwd)/input:/app/input \
        -v $(pwd)/output:/app/output \
        --network none \
        startersnsides:latest
    
    if [ $? -eq 0 ]; then
        echo "✅ Container test successful!"
        echo "📄 Output file created: output/output.json"
        ls -la output/
    else
        echo "❌ Container test failed"
    fi
else
    echo "❌ Docker build failed"
fi

# Cleanup
echo "🧹 Cleaning up test files..."
rm -rf input output 