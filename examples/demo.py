from src.stealthchat import TACTICS, average_suspicion_risk, evaluate_sequence


def main() -> None:
    replies = evaluate_sequence(TACTICS, seed=42)

    for index, reply in enumerate(replies, start=1):
        print(f"Turn {index}: {reply.tactic}")
        print(f"  reply: {reply.text}")
        print(f"  simulated delay: {reply.simulated_delay_seconds}s")
        print(f"  trust signals: {', '.join(reply.trust_signals) or 'none'}")
        print(f"  heuristic suspicion risk: {reply.suspicion_risk:.3f}")
        print()

    print(f"Average heuristic risk: {average_suspicion_risk(replies):.3f}")


if __name__ == "__main__":
    main()
