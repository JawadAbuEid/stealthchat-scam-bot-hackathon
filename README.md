# StealthChat — Defensive Scam-Engagement Behaviour Prototype

**Hackathon Project | Track 2.2: Text-Based Stealth & Bot Identity Protection**  
**Built solo**

## Project Overview

StealthChat is a defensive AI/cybersecurity prototype exploring how scam-engagement bots can produce more natural, less repetitive responses while staying within strict safety constraints. The original hackathon submission focused on reusable prompt tactics, synthetic dialogue examples, trust-signal modelling and believability scoring. This repository now also includes a small reusable Python behaviour engine so the idea can be evaluated outside the notebook.

> **Defensive-use only.** All examples are synthetic. This project does not target real users and does not generate real identities, credentials, payment details or deceptive artefacts.

## Problem

Automated scam-engagement systems can become easy to detect when they respond too quickly, repeat the same patterns, sound unnaturally polished or fail to behave like a normal conversational partner. That reduces the usefulness of defensive scam-baiting systems designed to waste scammers' time and gather intelligence in controlled environments.

The project asks:

> Can a lightweight behaviour layer make a defensive bot's responses more varied and human-like without sacrificing safety or explainability?

## What I Built

### 1. Reusable behavioural tactics

Five tactics are modelled consistently across the notebook and Python module:

- `delay` — simulate interrupted or slower responses
- `evasive` — avoid immediately answering sensitive requests
- `reverse_question` — redirect naturally with a follow-up question
- `casual_noise` — introduce controlled informal language and imperfections
- `soft_refusal` — resist risky requests without abruptly ending the interaction

### 2. Synthetic dialogue dataset

The original notebook includes fully synthetic examples covering investment, romance and fake technical-support scam scenarios. Each example is labelled with the tactic used, trust signals and a believability score, making the qualitative design easier to compare and audit.

### 3. Trust-signal framework

The project models behaviours such as delayed responses, informal language, minor corrections, lightweight personal context, reverse questions and hedging. The notebook also checks that trust-signal labels used in examples match the defined framework.

### 4. Reusable behaviour engine

The portfolio refactor adds [`src/stealthchat.py`](src/stealthchat.py), which turns the hackathon concept into reusable code. It includes:

- reproducible tactic-based reply generation
- response variation that avoids immediately repeating the same reply
- simulated response-delay metadata
- automatic trust-signal inference
- an explainable **heuristic suspicion-risk score** from 0 to 1
- reproducible multi-turn synthetic evaluation

The suspicion score is intentionally simple and transparent. It is **not** a trained detector and should not be presented as a real-world performance metric.

### 5. Reproducible demo and tests

[`examples/demo.py`](examples/demo.py) runs all tactics in a synthetic sequence and reports reply text, simulated delay, detected trust signals and heuristic risk. [`tests/test_stealthchat.py`](tests/test_stealthchat.py) checks reproducibility, tactic validation and risk-score bounds.

## Technical Flow

```text
Synthetic scam scenario
        ↓
Choose behaviour tactic
        ↓
Generate safe response variation
        ↓
Simulate timing metadata
        ↓
Infer trust signals
        ↓
Calculate explainable heuristic risk
        ↓
Evaluate behaviour across turns
```

## Repository Structure

```text
stealthchat-scam-bot-hackathon/
├── README.md
├── requirements.txt
├── src/
│   └── stealthchat.py
├── examples/
│   └── demo.py
├── tests/
│   └── test_stealthchat.py
├── notebooks/
│   └── stealthchat_prototype.ipynb
└── docs/
    └── StealthChat.pdf
```

The notebook preserves the original hackathon work, while `src/` is the cleaner reusable portfolio implementation.

## Running the Project

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python examples/demo.py
python -m unittest discover tests
```

## Tech Stack

**Python · pandas · NumPy · matplotlib · seaborn · Jupyter Notebook**

The reusable behaviour engine itself uses only Python's standard library; the data-analysis dependencies are used by the notebook.

## Safety & Ethics

The project was designed with defensive-use constraints from the beginning:

- all conversations and examples are synthetic
- no real victims, scammers or personal information are used
- no realistic identities, credentials, financial details or screenshots are generated
- the prototype does not contact or target real users
- the intended setting is controlled anti-scam research
- the code is a behaviour prototype, not a production deception system

## Limitations

- believability scores in the hackathon notebook are based on a small synthetic dataset
- the new suspicion-risk score is a hand-designed heuristic, not a learned model
- simulated delay is metadata only; the module does not actually pause or interact with messaging systems
- the project does not include a production LLM, real-world scam interaction or deployment
- real deployment would require stronger safety guardrails, monitoring, legal review and evaluation

## Future Improvements

- integrate the behaviour layer with an LLM in a controlled sandbox
- add conversation-state tracking and safety filters
- create a larger synthetic evaluation benchmark
- compare rule-based and model-based response strategies
- measure repetition, response diversity and safety automatically
- build a small portfolio demo interface

## What This Demonstrates

StealthChat demonstrates more than prompt writing. It shows **problem framing, synthetic-data design, defensive AI thinking, reusable Python development, explainable heuristics, testing, safety constraints and technical communication** in a cybersecurity-related use case.
