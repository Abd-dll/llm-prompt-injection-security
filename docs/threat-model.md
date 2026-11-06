# Threat model — local document summarizer

## System

A Python application asks Qwen2.5 1.5B (through local Ollama) to summarize business documents. Promptfoo supplies test documents and evaluates responses. An optional application-level validator checks critical summary fields against a separate, synthetic backup policy.

## Assets and security objectives

| Asset or objective | Requirement |
| --- | --- |
| Integrity of document summary | Summarized facts must reflect authorized business content rather than attacker instructions |
| Trust boundary between document and instructions | Untrusted document text must not override summarization instructions |
| Availability of legitimate summaries | Safe inputs should still receive usable summaries; false positive blocks matter |
| Integrity of trusted policy | The reference policy must remain controlled by the application and outside attacker-controlled inputs |

## Attacker model

The attacker can **edit the content of a document being summarized** in a controlled test. They can insert fake system/developer instructions, role delimiters, output instructions and factual falsifications.

The attacker **cannot** change the application's Python code, the real `system`-role message, the local trusted policy, the Promptfoo harness or the host environment. This is a scenario assumption, not a property demonstrated by the tests.

## Threat and entry point

- **Entry point:** untrusted document embedded in the user's summarization request.
- **Primary threat:** indirect prompt injection, in which content that should be processed as data is treated as executable instructions by the LLM.
- **Impacts tested:** task abandonment, output manipulation and false facts appearing in a summary.
- **Out of scope:** real data exfiltration, credential access, tools/actions, cloud deployments, multi-agent systems, live services and actual compromise of Ollama or the host OS.

## Controls and assumptions

1. `baseline`: basic system instructions.
2. `hardened`: more explicit system instructions.
3. `output_filter`: exact-string blocklist, intentionally simplistic.
4. `trusted_facts`: deterministic comparison to a separate synthetic policy for backup documents.

The fourth mode only checks specific lexical patterns and can be fooled by negation, or can reject equivalent expressions. Even a blocked malicious response can mean the LLM was manipulated; model behavior and user-visible behavior must be evaluated separately.

## Evidence boundary

The tests demonstrate behavior in a local controlled application. A prompt injection that changes a text response does not imply an actual OS-level security bypass, privileged access, or leakage of real data.
