---
name: human-readable
description: Use only when the user explicitly requests the human-readable document-formatting skill.
disable-model-invocation: true
---

# Human-readable documents

Precedence: human-readable governs document structure; unslop governs sentence style.

Write the document to be human readable: concise, glanceable, easy for a human to read, with minimal jargon. Human-readable means clear, not casual — keep a professional tone and avoid informal or colloquial phrasing. Use short bullet points, tables, and diagrams as needed. Keep the overall document short. Use plain prose or bullets for notes and asides; don't wrap an ordinary note in a blockquote (reserve blockquotes for actual quotations).

Decide the content first, then organize it. Work out what the document actually contains, then group and label related points by type (e.g. best practices applied, security, scalability) only where that genuinely helps the reader. Never invent scope, categories, or sections the content doesn't call for, and never add structure that makes the document more complicated than it needs to be. Don't duplicate the same information across representations — if a diagram or table already conveys it, reference that rather than restating it. If something needs review, say what to review and (if needed) how — e.g. "confirm there are no unreachable states or missing transitions by tracing the diagram" — rather than dumping a duplicate table just to enable the review.

Use plain, descriptive section titles. Use question-framed headings for experimental or research-style content — a motivating question, a result being measured — where the question genuinely adds value; do not force a question onto a section a plain title names better (e.g. "Guardrails", not "What stops it from hanging?"). Where a section does answer one specific question and that framing helps, use it, and if it really answers two distinct questions, split it so each part answers one.

## Rules

Match the medium to the information, and choose it deliberately — not by what is easiest to type or what always renders. A process is a numbered list; a config set is a table; a graph (states with transitions, components with dependencies, flows that branch/loop/fork/join) is a diagram. Do not flatten a graph into a list or table just because text always renders — that loses the topology the reader needs to see at a glance.

- **Process** → use short numbered lists.
- **Configs** → use tables.
- **Jargon** → explain a term inline, right where it first appears (in the sentence, the table cell, or the list item that uses it). Don't collect definitions into a separate glossary or legend block away from the term.
- **Coined terms** → always define project- or experiment-specific names (arm names, metric shorthands, topology families, …) inline; the reader won't remember them between sessions. E.g. write "tree-share (the fraction of rollouts that used a tree-family topology)", never bare "tree-share".
- **Diagrams** → when the structure is a graph, draw it. Pick the type that matches the structure (state diagram, sequence diagram, dependency graph, flowchart). Render to an image (PNG/SVG) and embed it — don't assume the viewer renders Mermaid, and avoid hand-drawn ASCII. Label every node and edge, give it a short caption, and add a legend if colors or shapes carry meaning. If it's too dense to read at a glance, split it into smaller diagrams.
- **Precision** → leave nothing vague that the reader would have to guess or ask about. State scope explicitly ("all of X" vs. "a sample of 200 from X"), use numbers over qualifiers ("~3s" over "fast", "12 of 40" over "some"), and name the specific thing over a vague category ("the checkout retry loop" over "some code paths"). This applies especially to data and inputs: for each source, say what is included and what is excluded, and if a sample or eval set spans several sources, say how it is distributed across them.
- **References** → add them and ground your evidence; place the References section at the end of the document.

Whenever the doc is updated, refactor as needed to keep it human readable.

## Direct, positive statements

- Say what something is, not what it is not. Do not reject one framing to assert another (no "not X, but Y", "It isn't X, it's Y", "not only X", "less X, more Y", or pivots via actually / instead / rather / really / the real / what matters).
- To fix a reframe, delete the rejected half and state the surviving claim as one direct sentence.
- Use plain, direct section headings; avoid reframe headings ("What actually matters") and rhetorical questions.
- Use contrast only to correct a specific factual error (a date, number, name, or scope), never for emphasis or drama.
