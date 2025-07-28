# Adobe Round 1b: Persona-Driven Document Intelligence - Solution

## Libraries Used

- **PyMuPDF (fitz)**: PDF processing
- **sentence-transformers**: Text embeddings
- **rank_bm25**: Using BM25 semantic search
- **scikit-learn**: For calculating cosine similarity

## Key Features and Mterics:
- Hybrid BM25 + Sentence Embeddings approach
- Domain-specific parameter tuning
- Multi-field scoring with heading emphasis
- Robust fallback mechanisms
- Modular Design by utilizing heading extractions from 1A Challenge
- No usage of Language Models
- Eliminated Internet/API calls usage
- Based on given Test Collections:
  - **Collection 1** (7 PDFs): ~25 seconds
  - **Collection 2** (15 PDFs): ~45 seconds  
  - **Collection 3** (9 PDFs): ~35 seconds
- Domain detection accuracy: ~95%
- Query expansion coverage: ~80%
- Result diversity: >90% unique documents
  
## 📁 File Structure

```
StartersNSides-1B/
├── approach_explanation.md      # Methodology documentation
├── Dockerfile                   # Container configuration
├── .dockerignore               # Docker build optimization
├── requirements.txt            # Python dependencies
├── src/                        # Source code
│   ├── run_pipeline.py         # Main pipeline (CLI support)
│   ├── extract/                # Document processing
│   ├── retrieval/              # Hybrid retrieval engine
│   ├── output/                 # Output formatting
│   └── utils/                  # Utility functions
└── Challenge_1b/               # Test data collections
```
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

## Execution

### Local Execution
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

### Docker Execution
### 1. Build the Docker Image

```bash
# Navigate to the project root directory
cd /path/to/StartersNSides-1B

# Build the Docker image
docker build -t hybrid-retrieval-system .
```

### 2. Run with Input Data

```bash
# Run the system with your input data
docker run --rm \
  -v $(pwd)/your_data_folder:/app/input \
  -v $(pwd)/output:/app/output \
  hybrid-retrieval-system
```

### 3. Example with Collection Data

```bash
# Run with Collection 1 (South of France travel guides)
docker run --rm \
  -v $(pwd)/Challenge_1b/Collection_1:/app/input \
  -v $(pwd)/output:/app/output \
  hybrid-retrieval-system

# Run with Collection 2 (Adobe Acrobat guides)
docker run --rm \
  -v $(pwd)/Challenge_1b/Collection_2:/app/input \
  -v $(pwd)/output:/app/output \
  hybrid-retrieval-system

# Run with Collection 3 (Culinary recipes)
docker run --rm \
  -v $(pwd)/Challenge_1b/Collection_3:/app/input \
  -v $(pwd)/output:/app/output \
  hybrid-retrieval-system
```

### 4. Custom Input/Output Paths

```bash
# Use custom input and output paths
docker run --rm \
  -v $(pwd)/myjob:/app/input \
  -v $(pwd)/myoutput:/app/output \
  hybrid-retrieval-system \
  python src/run_pipeline.py --input /app/input/custom_input.json --output /app/output/custom_output.json
```
## Input/Output Format

### Input
```json
{
  "challenge_info": {
    "challenge_id": "round_1b_XXX",
    "test_case_name": "specific_test_case"
  },
  "documents": [{"filename": "doc.pdf", "title": "Title"}],
  "persona": {"role": "User Persona"},
  "job_to_be_done": {"task": "Use case description"}
}
```
### Output
```json
{
  "metadata": {
    "input_documents": ["list"],
    "persona": "User Persona",
    "job_to_be_done": "Task description"
  },
  "extracted_sections": [
    {
      "document": "source.pdf",
      "section_title": "Title",
      "importance_rank": 1,
      "page_number": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "source.pdf",
      "refined_text": "Content",
      "page_number": 1
    }
  ]
}
```

## System Architecture
```mermaid
---
config:
  layout: dagre
  theme: base
  themeVariables:
    primaryColor: '#ffffff'
    primaryBorderColor: '#000000'
---
flowchart TD
 subgraph Input["Input"]
        B["Challenge Info"]
        A["Input JSON"]
        C["Documents List"]
        D["Persona"]
        E["Job To Be Done"]
  end
 subgraph Processing["Processing"]
        G["Document Processor"]
        F["PDF Collection"]
        H["Content Extractor"]
        I["Section Analyzer"]
        J["Importance Ranker"]
        K["Persona-based Filter"]
  end
 subgraph Output["Output"]
        L["Output JSON"]
        M["Metadata"]
        N["Extracted Sections"]
        O["Subsection Analysis"]
  end
 subgraph Collections["Collections"]
        P["Collection 1"]
        Q["Collection 2"]
        R["... Collection N"]
  end
 subgraph Chart[" "]
        Input
        Processing
        Output
        Collections
  end
    A L_A_B_0@-- Contains --> B & C & D & E
    F L_F_G_0@==> G
    G L_G_H_0@==> H
    H L_H_I_0@==> I
    I L_I_J_0@==> J
    D L_D_K_0@==> K
    E L_E_K_0@==> K
    K L_K_J_0@==> J
    J L_J_L_0@==> L
    L L_L_M_0@==> M & N & O
    P L_P_F_0@==> F
    Q L_Q_F_0@==> F
    R L_R_F_0@==> F
    style Input fill:#e6f3ff,color:#000000,stroke:#000000
    style Processing fill:#f9f9f9,color:#000000,stroke:#000000
    style Output fill:#e6ffe6,color:#000000,stroke:#000000
    style Collections fill:#ffe6e6,color:#000000,stroke:#000000
    style Chart fill:#FFFFFF
    linkStyle 0 stroke:#000000,fill:none
    linkStyle 1 stroke:#000000,fill:none
    linkStyle 2 stroke:#000000,fill:none
    linkStyle 3 stroke:#000000,fill:none
    linkStyle 4 stroke:#000000,fill:none
    linkStyle 5 stroke:#000000,fill:none
    linkStyle 6 stroke:#000000,fill:none
    linkStyle 7 stroke:#000000,fill:none
    linkStyle 8 stroke:#000000,fill:none
    linkStyle 9 stroke:#000000,fill:none
    linkStyle 10 stroke:#000000,fill:none
    linkStyle 11 stroke:#000000,fill:none
    linkStyle 12 stroke:#000000,fill:none
    linkStyle 13 stroke:#000000,fill:none
    linkStyle 14 stroke:#000000,fill:none
    linkStyle 15 stroke:#000000,fill:none
    linkStyle 16 stroke:#000000,fill:none
    linkStyle 17 stroke:#000000,fill:none
    L_A_B_0@{ animation: fast } 
    L_A_C_0@{ animation: fast } 
    L_A_D_0@{ animation: fast } 
    L_A_E_0@{ animation: fast } 
    L_F_G_0@{ animation: fast } 
    L_G_H_0@{ animation: fast } 
    L_H_I_0@{ animation: fast } 
    L_I_J_0@{ animation: fast } 
    L_D_K_0@{ animation: fast } 
    L_E_K_0@{ animation: fast } 
    L_K_J_0@{ animation: fast } 
    L_J_L_0@{ animation: fast } 
    L_L_M_0@{ animation: fast } 
    L_L_N_0@{ animation: fast } 
    L_L_O_0@{ animation: fast } 
    L_P_F_0@{ animation: slow } 
    L_Q_F_0@{ animation: fast } 
    L_R_F_0@{ animation: fast }

```
