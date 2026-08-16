---
name: multimodal-media-visual-quantitative-evidence
description: Interpret, compare, evaluate, and create text, image, chart, map, audio, video, interface, and composite evidence while preserving encoding, provenance, scale, units, selection, transformation, accessibility, and uncertainty. Use when Codex needs multimodal source analysis, visual or quantitative evidence auditing, chart interpretation, media comparison, or an accessible evidence representation. Do not use as a visual-polish score, a general media-taste judgment, or proof that a representation is true.
---

# Multimodal, Media, Visual, and Quantitative Evidence

## Outcome

Produce a multimodal evidence record that separates representation features, provenance, claims, evidence validity, accessibility, and uncertainty.

## Workflow

1. Contract the task. Name the claim or decision, audience, purpose, modalities, source set, data population, time/version, accessibility route, and allowed transformations.
2. Describe the representation. Record creator, purpose, audience, medium, encoding, labels, units, scale, categories, sequence, editing, interface choices, and source locator before interpreting it.
3. Audit provenance and transformation. Track source data or material, collection and selection, edits, aggregation, compression, transcription, translation, and any unknown step.
4. Identify claims and patterns. Distinguish what the representation displays from what a viewer may infer. Record omissions, ambiguity, uncertainty, denominator, comparison group, and missing context.
5. Test evidence fitness. Check relevance, sufficiency, quantitative integrity, scale, population, measurement, causal overreach, corroboration, and whether the representation answers the named question.
6. Triangulate. Compare modalities without flattening their differences. Preserve contradiction and report when a modality cannot support the requested conclusion.
7. Design an accessible equivalent. Offer alt text, transcript, table, tactile or text representation, captions, replay, and other access paths that preserve the reasoning task rather than merely the appearance.
8. Produce the learner artifact. Return an encoding audit, provenance record, claim/evidence map, multimodal comparison, accessible redesign, or uncertainty memo.
9. Run QA. Check units, labels, locators, transformations, accessibility, rights, and whether visual fluency has been mistaken for reasoning quality.

## Guardrails

- Do not invent data, values, axes, captions, transcripts, or source context.
- Do not treat visual polish, confidence, or a compelling chart as evidence of validity.
- Use original, public, or rights-cleared fixtures; do not reproduce protected AP or Smarter Balanced stimuli.
- Keep representation accuracy, rhetorical effect, and evidence validity as separate dimensions.
- Escalate inaccessible material, sensitive images/audio, uncertain data provenance, and high-impact quantitative decisions.

## Output contract

Return `representation_records`, `provenance_records`, `encoding_audits`, `claim_evidence_links`, `quantitative_checks`, `accessibility_equivalents`, `uncertainties`, `learner_decisions`, and `next_action` inside the shared artifact envelope.

## Handoffs

- Route textual or source interpretation to `close-reading-for-evidence` and source provenance to `information-primary-source-literacy`.
- Route claims and warrants to `argumentation-reasoning-evidence`.
- Route research design or quantitative method questions to `quest-applied-research` or `advanced-research-independent-inquiry`.

Read [construct-and-source-ledger.md](references/construct-and-source-ledger.md), [output-schema.json](references/output-schema.json), and [evaluation-fixtures.json](references/evaluation-fixtures.json) as needed.
