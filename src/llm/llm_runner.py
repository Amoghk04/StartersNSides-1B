from llama_cpp import Llama
import json

# Load Qwen2.5-0.5B (quantized GGUF model)
llm = Llama(
    model_path="./models/qwen2.5-0.5b-instruct-q4_k_m.gguf",
    n_ctx=2048,
    n_threads=4,
    verbose=False
)

def run_llm(prompt):
    response = llm(prompt, max_tokens=1024, stop=["</s>"])
    output_text = response["choices"][0]["text"].strip()

    try:
        return json.loads(output_text)
    except json.JSONDecodeError:
        print("⚠️ Failed to decode LLM output as JSON. Output was:\n", output_text)
        return {
            "extracted_sections": [],
            "subsection_analysis": []
        }