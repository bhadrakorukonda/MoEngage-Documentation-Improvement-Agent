# analyzer/analyze_article_phi2.py

import os
import requests
from bs4 import BeautifulSoup
from readability import Document
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

os.makedirs("outputs", exist_ok=True)

model_name = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_response(prompt, max_tokens=1024):
    result = generator(prompt, max_new_tokens=max_tokens, do_sample=True, temperature=0.7)
    return result[0]["generated_text"][len(prompt):]

def analyze_article(url):
    response = requests.get(url)
    doc = Document(response.text)
    html = doc.summary()
    title = doc.title()

    soup = BeautifulSoup(html, 'html.parser')
    content = soup.get_text(separator='\n')

    with open("outputs/original_raise_support_ticket.txt", "w", encoding="utf-8") as f:
        f.write(content)

    prompt = f"""You are an AI editor assessing the following documentation article:

Title: {title}
URL: {url}

Content:
"""{content}"""

Evaluate the article based on:
1. Readability for a marketer
2. Structure and flow
3. Completeness of information and examples
4. Adherence to simplified Microsoft Style Guide:
    - Voice and tone
    - Clarity and conciseness
    - Action-oriented language

Provide a structured markdown report with bullet-point suggestions under each heading.
"""
    response_text = generate_response(prompt)
    return response_text

if __name__ == "__main__":
    url = "https://help.moengage.com/hc/en-us/articles/4405057569170"
    report = analyze_article(url)

    with open("outputs/analysis_raise_support_ticket.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("✅ Analysis report saved to: outputs/analysis_raise_support_ticket.md")
