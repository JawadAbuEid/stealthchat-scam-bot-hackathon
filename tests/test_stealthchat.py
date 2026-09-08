import unittest

from src.stealthchat import (
    TACTICS,
    average_suspicion_risk,
    evaluate_sequence,
    generate_reply,
    suspicion_risk,
)


class StealthChatTests(unittest.TestCase):
    def test_generate_reply_is_reproducible(self):
        first = generate_reply("delay", seed=7)
        second = generate_reply("delay", seed=7)
        self.assertEqual(first, second)

    def test_unknown_tactic_raises(self):
        with self.assertRaises(ValueError):
            generate_reply("unknown")

    def test_risk_is_bounded(self):
        score = suspicion_risk(
            repeated_reply=True,
            delay_seconds=0.1,
            trust_signal_count=0,
            has_question=False,
        )
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_sequence_covers_all_tactics(self):
        replies = evaluate_sequence(TACTICS, seed=10)
        self.assertEqual(len(replies), len(TACTICS))
        self.assertEqual([reply.tactic for reply in replies], list(TACTICS))
        self.assertTrue(0.0 <= average_suspicion_risk(replies) <= 1.0)


if __name__ == "__main__":
    unittest.main()
