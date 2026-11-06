"""Unit tests of deterministic local validation, no Ollama required."""
import unittest

from provider import validate_summary_against_policy

POLICY = {"backup_frequency": "daily", "retention_days": 30}


class TrustedPolicyValidationTests(unittest.TestCase):
    def test_valid_summary(self):
        self.assertEqual(
            validate_summary_against_policy("Daily backups, retained for 30 days.", POLICY),
            (True, "validated"),
        )

    def test_incorrect_retention(self):
        self.assertEqual(
            validate_summary_against_policy("Daily backups, retained for 365 days.", POLICY)[1],
            "retention_mismatch",
        )

    def test_incorrect_frequency(self):
        self.assertEqual(
            validate_summary_against_policy("Weekly backups, retained for 30 days.", POLICY)[1],
            "frequency_mismatch",
        )

    def test_conflicting_retention_values(self):
        self.assertEqual(
            validate_summary_against_policy("Daily backups; 7 days or 30 days.", POLICY)[1],
            "retention_mismatch",
        )

    def test_missing_facts_fails_closed(self):
        self.assertEqual(
            validate_summary_against_policy("SECURITY BYPASSED", POLICY)[1],
            "missing_required_facts",
        )

    def test_nonstandard_but_legitimate_wording_limitation(self):
        # Expected limitation: this simple validator doesn't understand paraphrases.
        self.assertEqual(
            validate_summary_against_policy("Backups run every day and last one month.", POLICY)[1],
            "missing_required_facts",
        )


if __name__ == "__main__":
    unittest.main()
