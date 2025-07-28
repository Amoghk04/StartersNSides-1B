# Use Python 3.10 slim image for smaller size and better performance
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for PyMuPDF and other packages
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libffi-dev \
    libssl-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies in specific order to avoid conflicts
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy==1.24.3 && \
    pip install --no-cache-dir scikit-learn==1.3.0 && \
    pip install --no-cache-dir torch>=1.9.0 && \
    pip install --no-cache-dir huggingface-hub>=0.19.0 && \
    pip install --no-cache-dir transformers>=4.30.0 && \
    pip install --no-cache-dir sentence-transformers>=2.5.1 && \
    pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/ ./src/

# Create necessary directories
RUN mkdir -p src/output src/data

# Set environment variables
ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1
ENV HF_HUB_DISABLE_TELEMETRY=1

# Default command to run the pipeline
CMD ["python", "src/run_pipeline.py"] 