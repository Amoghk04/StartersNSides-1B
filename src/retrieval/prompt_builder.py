def build_prompt(persona, task, chunks):
    prompt = f"""
You are a helpful assistant.

Your role is: {persona}

Your task is: "{task}"

Based on the following document chunks, generate a response in this exact JSON format:

{{
  "extracted_sections": [
    {{
      "document": "<PDF filename>",
      "section_title": "<Section title (heading)>",
      "importance_rank": <integer>,
      "page_number": <integer>
    }},
    ...
  ],
  "subsection_analysis": [
    {{
      "document": "<PDF filename>",
      "refined_text": "<Detailed analysis based on that chunk>",
      "page_number": <integer>
    }},
    ...
  ]
}}

Only return valid JSON — no explanation, no notes, no headings like 'Conclusion'.

== Document Chunks Start ==
"""
    for chunk in chunks:
        prompt += (
            f"\n[Document: {chunk['pdf_name']}]\n"
            f"[Page: {chunk['page_number']}]\n"
            f"[Heading: {chunk['heading']}]\n"
            f"[Content]: {chunk['content']}\n"
        )
    prompt += "\n== Document Chunks End ==\n"
    prompt += "\n\nReturn only the JSON object below.\n"
    return prompt.strip()
