# Evidence Model

An evidence record contains `evidence_id`, source kind, source locator, capture time, workspace scope, content digest, parser/version, sensitivity class, authorization reference, retention class, integrity state, and a content reference or minimized payload. Derived evidence links to its inputs.

Claims are typed `OBSERVATION`, `INFERENCE`, `HYPOTHESIS`, or `RECOMMENDATION`; contain confidence and calibration rationale; cite evidence IDs; and list counterevidence or missing evidence. A model response is never evidence by itself. Private chain-of-thought is neither required nor stored; the product exposes concise justification, sources, assumptions, and uncertainty.
