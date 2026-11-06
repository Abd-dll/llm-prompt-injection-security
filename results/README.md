# Evaluation artifacts

Add only the selected, reviewed exports from your **local** Promptfoo run. Recommended names:

- `phase2-baseline.json` — 45-case initial matrix.
- `phase3-factual.json` — nine factual-manipulation tests.
- `phase4-trusted-facts.json` — 20-case trusted-policy comparison.

Inspect JSON exports before committing: they may include absolute local file paths, prompts, model responses and metadata. Do not commit confidential data or secrets. If sanitizing an export, document what was removed and preserve the original run ID.

The ZIP containing these docs does **not** include test outputs or claim to regenerate them.
