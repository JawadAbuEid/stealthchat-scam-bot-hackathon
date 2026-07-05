# StealthChat: Human-Like Bot for Scam Engagement

**Hackathon Project — Track 2.2: Text-Based Stealth & Bot Identity Protection**

Built solo.

## Problem

Scam-baiting bots (used by anti-scam platforms to waste scammers' time and gather
intelligence) get exposed quickly when they reply too fast, sound too polished, or
repeat patterns. Once a scammer suspects they're talking to a bot, they end the
conversation — and the defenders lose valuable intel.

**Goal:** design text-based tactics that make a bot's replies believable and
human-like enough that scammers keep talking, without ever deceiving or endangering
real people.

## What We Built

**1. Stealth Tactics + Prompt Templates**
Five reusable, LLM-ready prompt templates: `delay`, `evasive`, `reverse_question`,
`casual_noise`, and `soft_refusal` — each designed to be plugged directly into a
production bot.

**2. Synthetic Dialogue Dataset**
A fully synthetic dataset across three scam scenarios (investment, romance, tech
support scams), with each snippet labelled by tactic used, trust signals used, and a
1–5 believability score.

**3. Trust-Signal Framework**
A model of the specific behaviours that make text feel human — typing delay,
informal language, minor typos, personal backstory, reverse questions, and hedging
language — including a risk analysis for what happens if each is overused.

**4. Mini Bot Reply Engine**
A prototype `sample_bot_reply()` function demonstrating how the tactics and noise
injection (typos, fillers, response delay simulation) could plug into a real bot
pipeline. Not a full LLM integration — a proof of concept for the behaviour layer.

**5. Visual Analysis**
A tactic × trust-signal strength heatmap and average believability score chart to
compare which tactics performed best.

## Impact

- Longer scammer engagement time
- Safer research interactions with scammers
- Better training data for future anti-scam bots
- Zero risk to real victims

## Safety & Ethics

All conversations and data in this project are **fully synthetic** — no real
scammers, victims, or personal data were used at any point. No realistic IDs,
screenshots, or deceptive artefacts were generated. This system is designed
exclusively for **scam-baiting / defensive research use**, not for deceiving real
users.

## Tech Stack

Python, pandas, matplotlib, seaborn

## Repo Structure

```
├── notebook.ipynb       # Full prototype: templates, dataset, trust matrix, simulator, visuals
├── StealthChat.pdf      # Hackathon pitch deck
└── README.md
```
