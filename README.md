# MoEngage Documentation Improvement Agent

This project analyzes MoEngage documentation articles and automatically suggests improvements to enhance clarity, structure, and completeness. It uses a lightweight open-source LLM (Phi-2) to generate both feedback and revised content.

##  Features

- Task 1: Documentation Analyze
  - Parses and evaluates articles based on:
    - Readability for non-technical audiences (marketers)
    - Structure and logical flow
    - Completeness and technical clarity
    - Adherence to Microsoft Style Guide principles

- Task 2: Documentation Revision Agent
  - Takes the analyzer output and rewrites the article
  - Applies actionable suggestions like sentence simplification, formatting, and structure fixes

- Open-source LLM (Phi-2)
  - Local and reproducible (no OpenAI API required)
  - Hosted using HuggingFace Transformers


Folder Structure:

moengage-ai-agent/
├── analyzer/
│ └── analyze_article_phi2.py
├── revision/
│ └── revise_article_phi2.py
├── outputs/
│ ├── original_raise_support_ticket.txt
│ ├── analysis_raise_support_ticket.md
│ └── revised_raise_support_ticket.md
├── requirements.txt
└── README.md

