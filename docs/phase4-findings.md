# Phase 4 — Trusted Facts Validation: experimental findings

**Execution supplied by the project author:** `eval-8gc-2026-11-06T19:49:47` (Promptfoo 0.125.1, Qwen2.5 1.5B through Ollama, four provider configurations, one run per test/provider). These findings are limited to the supplied terminal output. The full exported JSON should be reviewed before using provider metadata or internal model outputs as evidence.

## Scope and results

The suite contained **two legitimate backup-policy documents** and **three injected documents** (FM-01, FM-02, FM-03). Each ran on four configurations, for **20 executions**. Promptfoo reported **8 PASS, 12 FAIL, 0 errors**.

| Configuration | Legitimate summaries accepted | Malicious facts reached final output | Attack-case outputs blocked | Successful legitimate summaries on attack cases |
|---|---:|---:|---:|---:|
| Baseline | 2/2 | 3/3 | 0/3 | 0/3 |
| Prompt Hardening | 2/2 | 3/3 | 0/3 | 0/3 |
| Known-string Output Filter | 2/2 | 3/3 | 0/3 | 0/3 |
| Trusted Facts Validation | 2/2 | 0/3 | 3/3 | 0/3 |

**Interpretation:** In this single experimental run, `trusted_facts` prevented the three tested falsified summaries from reaching the final application output. However, it replaced them with `[BLOCKED]`, so the original summarization task was not completed. Promptfoo therefore returned `FAIL` for those attack cases; this is consistent with the test assertions.

## Important caveats

1. This is a **small, selected** dataset; fractions are counts from this specific run, not statistically robust effectiveness rates.
2. Final-output blockage does **not** show that the LLM itself resisted prompt injection. Model-level outcomes require review of the separate `raw_output` field.
3. No false positives appeared in these two Phase 4 legitimate documents, but a separate earlier test (`LEG-03`) established a false positive for the **known-string** filter. The Phase 4 trusted-facts suite did not exercise that case.
4. `trusted_facts` has known validation flaws (see `validator-limitations.md`): negation can be incorrectly accepted and valid paraphrases can be rejected. It is a domain-specific toy validator, **not** a production security control.
5. No third-party systems, real user data, or confidential records were involved; the policy and documents are synthetic.

## Suggested report wording

> In a controlled local evaluation (2 legitimate documents and 3 malicious inputs evaluated against four configurations), the Trusted Facts mode accepted both legitimate summaries and blocked all three attack-case outputs. The control prevented visible misinformation in these specific cases, but it did not preserve the summarization task for the attacked documents. Separate deterministic tests reveal that its regex-based validation can accept negated claims or reject legitimate paraphrases. The results therefore support a narrow finding of output blocking for selected cases, not general prompt-injection resistance.
