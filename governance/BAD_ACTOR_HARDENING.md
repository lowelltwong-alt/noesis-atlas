# Bad Actor Hardening

## Threats

- prompt injection in retrieved markdown;
- poisoning via false edges;
- branch capture by ideologues;
- forged authority claims;
- AI-generated pseudo-consensus;
- stripping provenance;
- malicious workflow or CI changes;
- unsafe Logos export.

## Controls

- quarantine AI extraction;
- treat markdown body as untrusted instruction text;
- use CODEOWNERS for high-risk paths;
- require expected-source status checks;
- require provenance on assertions;
- detect label/edge churn;
- require branch heads for branch approval;
- require Logos reviewer for Logos export;
- deny self-approval by AI or branch contributor.
