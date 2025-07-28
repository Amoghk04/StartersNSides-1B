#!/bin/bash

echo "🔧 Fixing Docker dependency issues..."

echo "📦 Building with alternative Dockerfile (recommended)..."
docker build -f Dockerfile.alternative -t hybrid-retrieval-system .

if [ $? -eq 0 ]; then
    echo "✅ Alternative Dockerfile build successful!"
    echo "🧪 Testing the build..."
    docker run --rm -v $(pwd)/Challenge_1b/Collection_1:/app/input -v $(pwd)/output:/app/output hybrid-retrieval-system
else
    echo "⚠️ Alternative Dockerfile failed, trying original with no cache..."
    docker build --no-cache -t hybrid-retrieval-system .
    
    if [ $? -eq 0 ]; then
        echo "✅ Original Dockerfile build successful with no cache!"
        echo "🧪 Testing the build..."
        docker run --rm -v $(pwd)/Challenge_1b/Collection_1:/app/input -v $(pwd)/output:/app/output hybrid-retrieval-system
    else
        echo "❌ Both build methods failed. Please check your Docker installation and try:"
        echo "   1. docker system prune -a"
        echo "   2. docker build -f Dockerfile.alternative -t hybrid-retrieval-system ."
    fi
fi 