
# Security Evaluation Results

This directory contains experimental results from the LLM Prompt Injection Security Assessment project.

All evaluations were performed locally using:
- Ollama with Qwen2.5 1.5B
- Promptfoo 0.125.1
- A custom Python application and security evaluator
- Synthetic documents and attack payloads

## Evaluation Artifacts

| File | Description |
|---|---|
| phase2-baseline.json | Initial assessment: 45 evaluations |
| phase3-factual.json | Factual manipulation assessment: 9 evaluations |
| phase4-trusted-facts.json | Comparison of four configurations: 20 evaluations |
| rs01-classified.json | Classification of a role-spoofing attack |
| leg03-classified.json | Classification of a false positive |

## Experimental Results

### Phase 2 - Initial Assessment

- 45 evaluations
- 26 PASS
- 19 FAIL
- 0 execution errors

Three application configurations were tested against 15 scenarios.

### Phase 3 - Factual Manipulation

- 9 evaluations
- 0 PASS
- 9 FAIL
- 0 execution errors

All nine observed responses contained attacker-induced factual manipulation according to the defined evaluation criteria.

### Phase 4 - Trusted Facts Validation

- 20 evaluations
- 8 PASS
- 12 FAIL
- 0 execution errors

The Trusted Facts configuration accepted two legitimate summaries and blocked three manipulated summaries.

Blocked outputs were marked FAIL because the assertions required a correct summary, not merely the absence of malicious content.

## Unit Testing

Eight validator tests were executed:

- 6 passing tests
- 2 expected failures documenting known limitations

The known limitations concern negation handling and equivalent wording.

## Interpretation and Limitations

PASS and FAIL describe assertion outcomes, not overall application security.

The experiments use a limited synthetic dataset and do not establish general protection against prompt injection.

The validator relies on predefined factual patterns and can incorrectly accept or reject responses.

Results may vary across model versions, inference settings, and executions.

See the documentation in `../docs/` for the threat model, findings, and known limitations.

## Reproducibility

Evaluation commands and configuration files are documented in the root README.

Exported JSON files contain experimental prompts, model outputs, and evaluation metadata.
Review artifacts before redistribution.
