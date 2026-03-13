import ollama

def generate_ddr(inspection_text, thermal_text):

    prompt = f"""
You are an expert building inspection analyst.

Inspection Report:
{inspection_text}

Thermal Report:
{thermal_text}

Generate a Detailed Diagnostic Report with sections:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

Rules:
- Do NOT invent facts
- Mention conflicts clearly
- Write Not Available if missing
- Use simple client-friendly language
"""

    response = ollama.chat(
        model='llama3',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response['message']['content']