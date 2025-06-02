# revision/revise_article_phi2.py

from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

model_name = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_revision(original_text, suggestions):
    prompt = f"""You are a documentation editor.

Here is the original article:
"""{original_text}"""

Here are the improvement suggestions:
"""{suggestions}"""

Revise the article to apply the suggestions. Improve clarity, tone, structure, and flow. Preserve technical accuracy and formatting.
"""
    result = generator(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7)
    return result[0]["generated_text"][len(prompt):]

with open("outputs/original_raise_support_ticket.txt", "r", encoding="utf-8") as f:
    original = f.read()

with open("outputs/analysis_raise_support_ticket.md", "r", encoding="utf-8") as f:
    suggestions = f.read()

revised = generate_revision(original, suggestions)

with open("outputs/revised_raise_support_ticket.md", "w", encoding="utf-8") as f:
    f.write(revised)

print("✅ Revised article saved to: outputs/revised_raise_support_ticket.md")
