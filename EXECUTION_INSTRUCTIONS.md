# Execution Instructions

## Overview

This document provides comprehensive instructions for running the Hybrid BM25 + Embeddings Document Retrieval System using Docker or local development environment.

## Prerequisites

### For Docker (Recommended)
- Docker installed on your system
- At least 4GB RAM available for Docker
- 2GB free disk space

### For Local Development
- Python 3.10 or higher
- pip package manager
- At least 4GB RAM
- 2GB free disk space

## Quick Start with Docker

### 1. Build the Docker Image

```bash
# Navigate to the project root directory
cd /path/to/StartersNSides-1B

# Build the Docker image
docker build -t startersnsides:latest .
```

### 2. Run with Input Data

```bash
# Run the system with your input data
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  startersnsides:latest
```

### 3. Example with Collection Data

```bash
# Run with Collection 1 (South of France travel guides)
docker run --rm \
  -v $(pwd)/Challenge_1b/Collection_1:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  startersnsides:latest

# Run with Collection 2 (Adobe Acrobat guides)
docker run --rm \
  -v $(pwd)/Challenge_1b/Collection_2:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  startersnsides:latest

# Run with Collection 3 (Culinary recipes)
docker run --rm \
  -v $(pwd)/Challenge_1b/Collection_3:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  startersnsides:latest
```

### 4. Custom Input/Output Paths

```bash
# Use custom input and output paths
docker run --rm \
  -v $(pwd)/myjob:/app/input \
  -v $(pwd)/myoutput:/app/output \
  --network none \
  startersnsides:latest \
  python src/run_pipeline.py --input /app/input/custom_input.json --output /app/output/custom_output.json
```

## Local Development Setup

### 1. Install Dependencies

```bash
# Navigate to the project root directory
cd /path/to/StartersNSides-1B

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Run the Pipeline

```bash
# Navigate to src directory
cd src

# Run with default paths (/app/input/challenge1b_input.json and /app/output/output.json)
python run_pipeline.py

# Use custom input and output paths
python run_pipeline.py --input /path/to/input/challenge1b_input.json --output /path/to/output/output.json
```

### 3. Example with Collection Data

```bash
# Run with Collection 1
python run_pipeline.py --input ../Challenge_1b/Collection_1/challenge1b_input.json --output ../output/output.json

# Run with Collection 2
python run_pipeline.py --input ../Challenge_1b/Collection_2/challenge1b_input.json --output ../output/output.json

# Run with Collection 3
python run_pipeline.py --input ../Challenge_1b/Collection_3/challenge1b_input.json --output ../output/output.json
```

## Input Format

### Directory Structure
```
input/
├── challenge1b_input.json
└── PDFs/
    ├── document1.pdf
    ├── document2.pdf
    └── ...
```

### JSON Input Format
The `challenge1b_input.json` file should contain:

```json
{
  "persona": {
    "role": "HR professional"
  },
  "job_to_be_done": {
    "task": "Create and manage fillable forms for onboarding and compliance."
  },
  "documents": [
    {
      "filename": "document1.pdf"
    },
    {
      "filename": "document2.pdf"
    }
  ]
}
```

## Output Format

The system generates `output.json` with the following structure:

```json
{
  "metadata": {
    "input_documents": ["document1.pdf", "document2.pdf"],
    "persona": "HR professional",
    "job_to_be_done": "Create and manage fillable forms...",
    "processing_timestamp": "2025-07-27T14:31:45.089"
  },
  "extracted_sections": [
    {
      "document": "document1.pdf",
      "section_title": "Form Creation",
      "importance_rank": 1,
      "page_number": 5
    }
  ],
  "subsection_analysis": [
    {
      "document": "document1.pdf",
      "refined_text": "Detailed content...",
      "page_number": 5
    }
  ]
}
```

## Performance Monitoring

The system provides detailed performance metrics:

- **Processing Time**: Total execution time
- **Domain Detection**: Automatically detected domain (travel, research, business, culinary)
- **Hybrid Weights**: BM25 vs Embedding weights used
- **Scoring Breakdown**: Individual scores for each result

## Troubleshooting

### Common Issues

1. **ImportError: cannot import name 'cached_download' from 'huggingface_hub'**
   ```bash
   # This is a dependency version conflict. Use the alternative Dockerfile:
   docker build -f Dockerfile.alternative -t hybrid-retrieval-system .
   
   # Or rebuild with no cache:
   docker build --no-cache -t hybrid-retrieval-system .
   ```

2. **Memory Issues**
   ```bash
   # Increase Docker memory limit
   docker run --memory=6g hybrid-retrieval-system
   ```

3. **Model Download Issues**
   ```bash
   # Clear pip cache
   pip cache purge
   
   # Rebuild Docker image
   docker build --no-cache -t hybrid-retrieval-system .
   ```

4. **PDF Processing Errors**
   - Ensure PDFs are not corrupted
   - Check file permissions
   - Verify PDFs are text-based (not scanned images)

### Debug Mode

```bash
# Run with verbose logging
docker run -e DEBUG=1 hybrid-retrieval-system

# Local debug mode
python run_pipeline.py --debug
```

## Advanced Usage

### Custom Embedding Models

```bash
# Use different sentence transformer model
docker run -e EMBEDDING_MODEL=all-mpnet-base-v2 hybrid-retrieval-system
```

### BM25 Parameter Tuning

```bash
# Custom BM25 parameters
docker run -e BM25_K1=1.5 -e BM25_B=0.7 hybrid-retrieval-system
```

### Batch Processing

```bash
# Process multiple collections
for collection in 1 2 3; do
  docker run -v $(pwd)/Challenge_1b:/app/Challenge_1b \
    -e COLLECTION=$collection \
    hybrid-retrieval-system
done
```

## System Requirements

- **Minimum**: 4GB RAM, 2GB disk space
- **Recommended**: 8GB RAM, 5GB disk space
- **Network**: Required for initial model download (one-time)

## Performance Benchmarks

- **Collection 1** (15 PDFs): ~30 seconds
- **Collection 2** (15 PDFs): ~45 seconds  
- **Collection 3** (9 PDFs): ~25 seconds

*Times may vary based on system specifications and network speed for model download.* 