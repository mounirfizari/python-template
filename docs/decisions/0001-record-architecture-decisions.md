# 1. Record architecture decisions

Date: 2026-09-10

## Status

Accepted

## Context

This project needs a lightweight and durable way to record why the project made the
technical choices it did. Decisions not stored in the codebase itself
get lost over time, and new contributors re-litigate settled questions.
Old contributors change their minds and quietly reverse things.

## Decision

This project uses Architecture Decision Records, as
[described by Michael Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions),
stored as numbered markdown files under `docs/decisions/`. Each record
captures the context, the decision, and its consequences.

Records are immutable once accepted. Superseding decisions get a new
record that explicitly links back.

## Consequences

- Cheap to write — one page, one PR.
- Cheap to read — chronologically ordered, indexed in `README.md`.
- Requires discipline: contributors have to remember to write them.
- Requires review: an ADR PR is where the decision actually happens,
  so reviewers should engage with the reasoning, not just the wording.
