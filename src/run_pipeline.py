from extract.heading_extractor import PDFHeadingExtractor
from extract.content_chunker import extract_chunks_with_headings
from embed.embedder import MiniLMEmbedder
from retrieval.retriever import build_faiss_index, search_top_k
from retrieval.prompt_builder import build_prompt
from llm.llm_runner import run_llm
from utils.file_utils import load_json, save_json, current_timestamp, ensure_dir, list_pdfs
from pathlib import Path
import json

def main():
    input_path = "../Challenge_1b/Collection_1/challenge1b_input.json"
    output_path = Path("./output/output.json")
    embeddings_path = Path("./output/embeddings.json")
    pdf_dir = Path("../Challenge_1b/Collection_1/PDFs/")

    ensure_dir("data/")
    ensure_dir("output/")

    # Step 1: Extract and Embed Chunks
    extractor = PDFHeadingExtractor()
    embedder = MiniLMEmbedder()

    all_results = []
    for pdf_file in pdf_dir.glob("*.pdf"):
        print(f"🔍 Processing {pdf_file.name}")
        headings = extractor.extract_headings(str(pdf_file))
        chunks = extract_chunks_with_headings(str(pdf_file), headings)
        embedded_chunks = embedder.embed_chunks(chunks)
        all_results.extend(embedded_chunks)

    save_json(all_results, embeddings_path)
    print(f"✅ Saved embeddings to {embeddings_path}")

    # Step 2: Retrieval + Prompting
    input_data = load_json(input_path)
    persona = input_data['persona']['role']
    task = input_data['job_to_be_done']['task']
    input_docs = [doc['filename'] for doc in input_data['documents']]

    relevant_chunks = [c for c in all_results if c['pdf_name'] in input_docs]

    index = build_faiss_index(relevant_chunks)
    top_chunks = search_top_k(index, embedder, task, relevant_chunks, k=5)

    prompt = build_prompt(persona, task, top_chunks)
    output = run_llm(prompt)

    output['metadata'] = {
        "input_documents": input_docs,
        "persona": persona,
        "job_to_be_done": task,
        "processing_timestamp": current_timestamp()
    }

    save_json(output, output_path)
    print(f"✅ Output saved to {output_path}")

if __name__ == "__main__":
    main()