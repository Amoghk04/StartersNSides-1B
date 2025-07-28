# Hybrid BM25 + Embeddings Document Retrieval System

## Overview

This document retrieval system implements a sophisticated hybrid approach combining BM25 (Bag of Words) and sentence embeddings to provide highly relevant document sections based on user queries. The system is designed to handle diverse domains including travel planning, research analysis, business documentation, and culinary content.

> [!WARNING]
> Make sure Internet is present during the Docker Build stage, as the embedding model has to be downloaded for hybrd retrieval system.
## Methodology

### 1. Document Processing Pipeline

The system begins with comprehensive PDF document processing:

- **Heading Extraction**: Uses PyMuPDF to analyze font characteristics, positioning, and text patterns to identify document headings. The algorithm considers font size ratios, bold formatting, and structural patterns (numbered sections, chapter titles) to distinguish headings from body text.

- **Content Chunking**: Splits documents into semantically coherent chunks based on extracted headings. Each chunk maintains context with its associated heading, page number, and source document information.

### 2. Hybrid Retrieval Architecture

The core innovation lies in the hybrid retrieval approach that leverages both sparse and dense representations:

**BM25 Component (Sparse Retrieval)**:
- Implements Okapi BM25 ranking function with domain-specific parameter tuning
- Enhanced tokenization with stop word removal and filtering
- Query expansion using domain-specific synonym mappings
- Multi-field scoring that weights headings more heavily than body content

**Sentence Embeddings Component (Dense Retrieval)**:
- Uses SentenceTransformer (paraphrase-MiniLM-L3-v2) for semantic understanding
- Computes cosine similarity between query and document embeddings
- Captures semantic relationships and conceptual similarities

**Hybrid Scoring**:
- Combines normalized BM25 and embedding scores using domain-specific weights
- Travel: BM25 (60%) + Embeddings (40%) - BM25 excels at location names
- Research: BM25 (40%) + Embeddings (60%) - Embeddings better for concepts
- Business: Balanced 50/50 split
- Culinary: BM25 (70%) + Embeddings (30%) - BM25 good for ingredients

### 3. Domain-Aware Optimization

The system automatically detects the query domain and applies specialized optimizations:

- **Dynamic BM25 Parameters**: Adjusts k1 (term frequency saturation) and b (length normalization) based on domain characteristics
- **Query Enhancement**: Expands queries with domain-specific synonyms (e.g., "hotel" → "accommodation, lodging, stay")
- **Result Diversity**: Implements diversity filtering to avoid redundant results from the same document or with similar headings

### 4. Performance Optimizations

Several optimizations ensure efficient processing:

- **Batch Processing**: Sentence embeddings computed in batches for memory efficiency
- **Fallback Mechanism**: Gracefully degrades to BM25-only if embedding model fails to load
- **Caching**: Embeddings computed once during index building and reused for queries
- **Early Termination**: Stops processing when sufficient diverse results are found

### 5. Output Formatting

The system generates structured output matching the challenge requirements:

- **Extracted Sections**: Top-ranked chunks with importance ranking and metadata
- **Subsection Analysis**: Detailed content with refined text and page references
- **Metadata**: Processing timestamp, input documents, and query information

## Technical Advantages

This hybrid approach provides several key benefits:

1. **Complementary Strengths**: BM25 excels at exact keyword matching while embeddings capture semantic relationships
2. **Domain Adaptability**: Automatic parameter tuning based on detected domain
3. **Robustness**: Fallback mechanisms ensure system reliability
4. **Scalability**: Efficient processing suitable for large document collections
5. **Interpretability**: Detailed scoring breakdowns for analysis and debugging

## Key Innovations

1. **Hybrid Scoring**: Combines BM25 and embeddings with domain-specific weights
2. **Domain Awareness**: Automatic detection and optimization per domain
3. **Query Enhancement**: Intelligent synonym expansion
4. **Result Diversity**: Prevents redundant results
5. **Robust Fallback**: Graceful degradation if embeddings fail
6. **Performance Optimization**: Batch processing and caching

## Future Enhancements

- Additional embedding models
- Real-time query processing
- Web interface for interactive use
- API endpoints for integration
- Advanced caching strategies


The system achieves high relevance through intelligent combination of traditional information retrieval techniques with modern neural embeddings, providing both precision and recall across diverse document types and user intents. 
