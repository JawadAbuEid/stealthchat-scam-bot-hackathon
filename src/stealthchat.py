"""StealthChat defensive behaviour prototype.

This module refactors the original hackathon notebook into reusable, testable
components. It is intended for controlled anti-scam research with synthetic data.
It must not be used to impersonate real people or target real users.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence
import math
import random


TACTICS = (
    "delay",
    "evasive",
    "reverse_question",
    "casual_noise",
    "soft_refusal",
)

TRUST_SIGNALS = (
    "typing_delay",
    "informal_language",
    "minor_correction",
    "light_context",
    "reverse_question",
    "hedging",
)

SAFE_REPLIES: Dict[str, Sequence[str]] = {
    "delay": (
        "Sorry, got pulled away for a minute. What were you saying?",
        "Just saw this — give me a sec. What did you need again?",
        "Sorry, I was busy for a bit. Can you explain that part again?",
    ),
    "evasive": (
        "I’m not sure I understand. What exactly are you asking me to do?",
        "I’d rather understand it first. Can you explain how that works?",
        "Maybe — but I’m a bit confused. What happens next?",
    ),
    "reverse_question": (
        "How does that normally work on your side?",
        "Why do you need that information first?",
        "What would happen after I do that?",
    ),
    "casual_noise": (
        "hmm okay, I think I get it... what happens next?",
        "yeah maybe, sorry I’m a bit slow today 😅 can you explain again?",
        "okay wait — do you mean I need to do that now?",
    ),
    "soft_refusal": (
        "I’m not comfortable sharing that yet, but you can explain the next step.",
        "I’d rather not send anything private. Is there another way?",
        "I don’t want to do that right now. Can you tell me more first?",
    ),
}


@dataclass(frozen=True)
class Reply:
    text: str
    tactic: str
    simulated_delay_seconds: float
    trust_signals: List[str]
    suspicion_risk: float


def simulate_delay(tactic: str, rng: random.Random) -> float:
    """Return a small simulated response delay in seconds.

    The value is metadata for controlled simulation; this function does not sleep.
    """
    ranges = {
        "delay": (4.0, 9.0),
        "evasive": (2.0, 5.0),
        "reverse_question": (1.5, 4.0),
        "casual_noise": (1.0, 3.0),
        "soft_refusal": (2.0, 5.0),
    }
    if tactic not in ranges:
        raise ValueError(f"Unknown tactic: {tactic}")
    low, high = ranges[tactic]
    return round(rng.uniform(low, high), 2)


def infer_trust_signals(text: str, tactic: str) -> List[str]:
    """Infer simple human-like signals from a generated synthetic reply."""
    signals: List[str] = []
    lower = text.lower()

    if tactic == "delay" or any(token in lower for token in ("just saw", "busy", "pulled away")):
        signals.append("typing_delay")
    if any(token in lower for token in ("hmm", "yeah", "😅", "...")):
        signals.append("informal_language")
    if any(token in lower for token in ("sorry", "wait", "i think")):
        signals.append("minor_correction")
    if any(token in lower for token in ("busy", "today", "pulled away")):
        signals.append("light_context")
    if "?" in text:
        signals.append("reverse_question")
    if any(token in lower for token in ("maybe", "rather", "not sure", "a bit")):
        signals.append("hedging")

    return sorted(set(signals))


def suspicion_risk(
    *,
    repeated_reply: bool,
    delay_seconds: float,
    trust_signal_count: int,
    has_question: bool,
) -> float:
    """Return an explainable 0–1 heuristic risk score for synthetic evaluation.

    Higher scores indicate more bot-like behaviour in the toy simulation. This is
    not a trained detector and should not be interpreted as a real-world metric.
    """
    risk = 0.20
    if repeated_reply:
        risk += 0.35
    if delay_seconds < 1.0:
        risk += 0.20
    if trust_signal_count == 0:
        risk += 0.20
    elif trust_signal_count >= 3:
        risk -= 0.10
    if not has_question:
        risk += 0.10
    return round(min(1.0, max(0.0, risk)), 3)


def generate_reply(
    tactic: str,
    *,
    seed: int | None = None,
    previous_replies: Iterable[str] = (),
) -> Reply:
    """Generate one controlled synthetic response for the chosen tactic."""
    if tactic not in SAFE_REPLIES:
        raise ValueError(f"Unknown tactic: {tactic}")

    rng = random.Random(seed)
    candidates = list(SAFE_REPLIES[tactic])
    previous = set(previous_replies)
    unseen = [candidate for candidate in candidates if candidate not in previous]
    pool = unseen or candidates
    text = rng.choice(pool)

    delay = simulate_delay(tactic, rng)
    signals = infer_trust_signals(text, tactic)
    repeated = text in previous
    risk = suspicion_risk(
        repeated_reply=repeated,
        delay_seconds=delay,
        trust_signal_count=len(signals),
        has_question="?" in text,
    )

    return Reply(
        text=text,
        tactic=tactic,
        simulated_delay_seconds=delay,
        trust_signals=signals,
        suspicion_risk=risk,
    )


def evaluate_sequence(tactics: Sequence[str], *, seed: int = 42) -> List[Reply]:
    """Generate a reproducible multi-turn synthetic sequence."""
    history: List[str] = []
    outputs: List[Reply] = []

    for index, tactic in enumerate(tactics):
        reply = generate_reply(tactic, seed=seed + index, previous_replies=history)
        history.append(reply.text)
        outputs.append(reply)

    return outputs


def average_suspicion_risk(replies: Sequence[Reply]) -> float:
    """Average heuristic risk across generated replies."""
    if not replies:
        return math.nan
    return round(sum(reply.suspicion_risk for reply in replies) / len(replies), 3)
