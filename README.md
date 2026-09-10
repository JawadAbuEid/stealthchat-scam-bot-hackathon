# StealthChat — Defensive Scam-Engagement Behaviour Prototype

**Solo Hackathon Project | Python · Defensive AI · Responsible AI**

## Project Overview

### Context
Defensive scam-engagement bots can become predictable when they reply too quickly, repeat the same patterns or sound unnaturally consistent. In controlled anti-scam research, that can reduce the usefulness of a system intended to sustain synthetic scam-engagement scenarios safely.

I built StealthChat to explore a simple question:

> Can a lightweight behaviour layer make defensive bot responses more varied and natural while keeping the system safe, explainable and reproducible?

### Actions
I built this project solo and developed a reusable Python behaviour engine around five tactics: **delay, evasive response, reverse question, casual noise and soft refusal**.

The project includes:
- fully synthetic scam scenarios
- seeded reply variation for reproducible behaviour
- simulated response-delay metadata
- automatic trust-signal inference
- an explainable heuristic suspicion-risk score
- reproducible multi-turn evaluation
- a runnable demo and unit tests

### Results
The hackathon concept was turned into a reusable Python module rather than remaining only as notebook experimentation. The final portfolio version can generate tactic-based responses, infer behavioural trust signals, calculate a transparent heuristic risk score and evaluate behaviour across synthetic conversation turns.

The risk score is intentionally a **hand-designed heuristic**, not a trained scam detector or real-world performance metric. No real victims, scammers or personal data are used.

### Growth & Next Steps
The next stage would be to integrate the behaviour layer with an LLM inside a controlled sandbox, add conversation-state tracking and stronger safety filters, build a larger synthetic evaluation benchmark and measure response diversity, repetition and safety automatically.

---

## How It Works

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

## Core Components

### Behavioural Tactics
Five tactics are modelled consistently across the notebook and Python module:

- `delay` — simulate interrupted or slower responses
- `evasive` — avoid immediately answering sensitive requests
- `reverse_question` — redirect naturally with a follow-up question
- `casual_noise` — introduce controlled informal language and imperfections
- `soft_refusal` — resist risky requests without abruptly ending the interaction

### Synthetic Dialogue Data
The original notebook includes fully synthetic examples covering investment, romance and fake technical-support scam scenarios. Examples are labelled with the tactic used, trust signals and a believability score so the qualitative design can be compared and audited.

### Trust-Signal Framework
The project models behaviours such as delayed responses, informal language, minor corrections, lightweight personal context, reverse questions and hedging. The notebook also checks that trust-signal labels used in examples match the defined framework.

### Reusable Python Engine
[`src/stealthchat.py`](src/stealthchat.py) includes:
- reproducible tactic-based reply generation
- variation that avoids immediately repeating the same reply
- simulated response-delay metadata
- automatic trust-signal inference
- an explainable heuristic suspicion-risk score from 0 to 1
- reproducible multi-turn synthetic evaluation

### Demo & Tests
[`examples/demo.py`](examples/demo.py) runs the tactics in a synthetic sequence and reports reply text, simulated delay, detected trust signals and heuristic risk.

[`tests/test_stealthchat.py`](tests/test_stealthchat.py) contains checks for reproducibility, tactic validation and risk-score bounds.

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

The notebook preserves the original hackathon work, while `src/` contains the reusable portfolio implementation.

## Tech Stack

**Python · pandas · NumPy · matplotlib · seaborn · Jupyter Notebook**

The reusable behaviour engine itself uses only Python's standard library; the data-analysis dependencies are used by the notebook.

## Run Locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python examples/demo.py
python -m unittest discover tests
```

## Safety & Ethics

This project was designed with defensive-use constraints from the beginning:
- all conversations and examples are synthetic
- no real victims, scammers or personal information are used
- no realistic identities, credentials, financial details or screenshots are generated
- the prototype does not contact or target real users
- the intended setting is controlled anti-scam research
- the code is a behaviour prototype, not a production deception system

## Limitations

- believability scores in the hackathon notebook are based on a small synthetic dataset
- the suspicion-risk score is a hand-designed heuristic, not a learned model
- simulated delay is metadata only; the module does not actually pause or interact with messaging systems
- the project does not include a production LLM, real-world scam interaction or deployment
- real deployment would require stronger safety guardrails, monitoring, legal review and evaluation

## What This Demonstrates

**Problem framing · synthetic-data design · Python development · defensive AI · explainable heuristics · testing · Responsible AI · technical communication**
