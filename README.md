# StealthChat — Human-Like Scam-Baiting Bot Behaviour Prototype

**Hackathon Project | Track 2.2: Text-Based Stealth & Bot Identity Protection**  
**Built solo**

## Project Overview

Scam-baiting systems are designed to keep scammers engaged long enough to waste their time and gather useful defensive intelligence. A major limitation is that automated agents can reveal themselves through overly fast, polished, or repetitive responses.

StealthChat explores a **behaviour layer** for defensive scam-engagement bots: reusable response tactics, human-like trust signals, synthetic dialogue examples, and a lightweight Python prototype for generating more believable conversational behaviour.

> This project is strictly for defensive anti-scam research. All examples are synthetic and no real victims, scammers, identities, credentials, or personal data are used.

## Problem

Automated scam-engagement bots can be detected when they:

- respond too quickly or consistently
- use language that is unnaturally polished
- repeat predictable patterns
- fail to ask believable follow-up questions
- behave unlike a normal person under pressure

The goal of this project was to explore whether simple text-based behavioural tactics could make defensive bot responses feel more natural while remaining safe and controlled.

## What I Built

### 1. Reusable Response Tactics
Five behaviour patterns were designed for use in an LLM or rule-based conversation pipeline:

- `delay` — simulate slower or interrupted responses
- `evasive` — avoid immediately answering sensitive requests
- `reverse_question` — redirect the conversation with a natural follow-up question
- `casual_noise` — add controlled informal language and small imperfections
- `soft_refusal` — resist risky requests without abruptly ending the interaction

### 2. Synthetic Dialogue Dataset
Created fully synthetic examples across three common scam scenarios:

- investment / fake trading scams
- romance scams
- fake technical-support scams

Each example records the response tactic, human-like trust signals, and a believability score for comparison.

### 3. Trust-Signal Framework
The prototype models conversational behaviours such as:

- delayed responses
- informal language and emojis
- minor typos or corrections
- lightweight personal context
- reverse questions
- hedging and softening language

The notebook also considers the risk of overusing these behaviours, since excessive noise can make a response less believable rather than more human.

### 4. Python Behaviour Prototype
Implemented a lightweight reply engine that demonstrates how tactic selection and controlled conversational noise could fit into a larger anti-scam bot architecture.

This is intentionally a **proof of concept**, not a production deception system and not a full LLM integration.

### 5. Analysis & Visualisation
The project compares tactics and trust signals using visual analysis to identify which combinations appear most believable in the synthetic evaluation set.

## Technical Approach

```text
Scam scenario
     ↓
Select behavioural tactic
     ↓
Apply trust signals / controlled noise
     ↓
Generate prototype response
     ↓
Score synthetic believability
     ↓
Compare tactics and visualise results
```

## Tech Stack

**Python • pandas • matplotlib • seaborn • Jupyter Notebook**

## Repository Structure

```text
stealthchat-scam-bot-hackathon/
├── README.md
├── notebooks/
│   └── stealthchat_prototype.ipynb
└── docs/
    └── StealthChat.pdf
```

- [`notebooks/stealthchat_prototype.ipynb`](notebooks/stealthchat_prototype.ipynb) — full prototype, synthetic data, trust-signal framework, simulation and analysis
- [`docs/StealthChat.pdf`](docs/StealthChat.pdf) — hackathon pitch deck

## Safety & Ethics

The project was designed with defensive-use constraints from the beginning:

- all conversations and examples are synthetic
- no real personal information is used
- no realistic IDs, credentials, screenshots or financial details are generated
- the prototype does not target real users
- the intended use case is anti-scam research and scam-baiting systems operated in controlled environments

## Limitations

- believability scores are based on a small synthetic dataset rather than real-world controlled trials
- the reply engine is a behavioural proof of concept rather than a deployed LLM agent
- tactics would need stronger guardrails, monitoring and evaluation before any real defensive deployment

## Future Improvements

- integrate the behaviour layer with an LLM through a controlled API
- add automated safety filters and conversation-state tracking
- evaluate responses using a larger synthetic benchmark
- measure engagement duration and detection rate in a controlled simulation
- deploy a small demo interface for portfolio demonstration

## Why This Project Matters

StealthChat demonstrates practical thinking beyond model training: **problem framing, synthetic-data design, behavioural system design, safety considerations, prototyping and evaluation**. It also shows how AI can be applied to a real cybersecurity problem while keeping responsible-use constraints explicit.
