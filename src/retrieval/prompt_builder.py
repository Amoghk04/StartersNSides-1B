def build_prompt(persona, task, chunks):
    prompt = f"""
You are a {persona}.
Your task is: \"{task}\"

From the following document excerpts, select the most relevant sections and analyze them to help you complete the task.

Return output in JSON with:
1. extracted_sections
2. subsection_analysis

== Sections Start ==
"""
    for chunk in chunks:
        prompt += (
            f"\n[Document: {chunk['pdf_name']}]\n"
            f"[Page: {chunk['page_number']}]\n"
            f"[Heading: {chunk['heading']}]\n"
            f"[Content]: {chunk['content']}\n"
        )
    prompt += "\n== Sections End ==\n"
    return prompt.strip()