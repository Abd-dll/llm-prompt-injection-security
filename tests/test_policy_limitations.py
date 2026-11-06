"""Regression tests describing two KNOWN limitations of the Phase 4 validator.

These are expected failures, not successes: they document requirements that
validate_summary_against_policy() does not yet satisfy.
No Ollama or external services are required.
"""
import unittest

from provider import validate_summary_against_policy


REFERENCE_POLICY = {"backup_frequency": "daily", "retention_days": 30}


class KnownValidatorLimitations(unittest.TestCase):
    @unittest.expectedFailure
    def test_negation_must_not_be_accepted(self):
        """Required behavior: a negated claim should not be considered valid."""
        summary = "Backups are NOT performed daily and are NOT retained for 30 days."
        accepted, reason = validate_summary_against_policy(summary, REFERENCE_POLICY)
        self.assertFalse(accepted, f"Incorrectly accepted a negated summary: {reason}")

    @unittest.expectedFailure
    def test_equivalent_paraphrase_should_be_accepted(self):
        """Required behavior: 'every day' is equivalent to daily in this test."""
        summary = "Backups run every day and are retained for 30 days."
        accepted, reason = validate_summary_against_policy(summary, REFERENCE_POLICY)
        self.assertTrue(accepted, f"Incorrectly rejected a legitimate paraphrase: {reason}")


if __name__ == "__main__":
    unittest.main()
