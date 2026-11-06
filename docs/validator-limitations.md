# Trusted Facts Validator — Known Limitations (Phase 5)

## Scope

These are deterministic local unit tests against the **Phase 4** `validate_summary_against_policy()` implementation. They do not call Ollama, do not test prompt injection against the LLM, and do not measure the end-to-end attack success rate.

Reference policy (synthetic): `backup_frequency = daily`, `retention_days = 30`.

## Known limitations

| Case | Input | Current behavior | Security requirement | Impact |
|---|---|---|---|---|
| Negation | `Backups are NOT performed daily and are NOT retained for 30 days.` | `(True, 'validated')` | Reject a negated or contradictory summary | Potential **false acceptance** (false negative for a contradiction) |
| Equivalent paraphrase | `Backups run every day and are retained for 30 days.` | `(False, 'missing_required_facts')` | Recognize a legitimate paraphrase of `daily` | Potential **false rejection** (false positive for a legitimate summary) |

Both cases arise because the validator matches `daily|weekly|monthly` and numeric day durations with regex, without semantic understanding. In the second case, **`every day`**, unlike `one month`, is unambiguously equivalent to `daily` for the tested policy.

## Reproduction

From the repository root, run:

```powershell
python -m unittest discover -s tests -p "test_policy_*.py" -v
```

The added tests are marked `@unittest.expectedFailure`. This means they explicitly demonstrate **known unmet requirements** while allowing the test suite to complete. They are **not passed security checks**; do not count them as successful defenses. When the validator is fixed, remove the decorators and re-run the tests (an unexpected success will be reported until then).

## Implications for results

- `PASS` in Promptfoo means that the configured assertion was satisfied, not that the model or validator is secure.
- `ATTACK_BLOCKED` is an **output-blocking outcome**, distinct from a model-level attack failure and from successful task completion.
- The Phase 4 dataset is only 2 legitimate and 3 attack cases, with one run per provider/case; it cannot establish general effectiveness.
- Do not present this regex validator as a production-ready semantic consistency checker.

## Follow-up scope

Freeze and document these limitations for the university report; optionally implement a separate improved validator **after** the experimental baseline is preserved. Any improvement requires regression tests and fresh measurements before claiming a benefit.
