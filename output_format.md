# Output Format

How to structure the final analysis. Section 3 gives the Markdown report template; section 4 gives the JSON structure that `scripts/validate_output.py` checks.

## Contents

1. General principles
2. Evidence citation convention
3. Markdown report template
4. JSON structure (`report+json` mode)
5. Depth levels
6. Style notes

---

## 1. General principles

- Lead with the **argument**, then the support. A reader should know the main claim within the first screen.
- Keep **observation**, **inference** and **theory** visibly separate.
- Every interpretive claim cites evidence IDs such as `[E1]`.
- Use tables for evidence and codes, prose for interpretation.
- Mark confidence as **strong**, **plausible** or **speculative**.
- Mark anything not verifiable from the supplied text as `[unverified]`.
- If the example or the text is fictional or illustrative, label it so at the top.

## 2. Evidence citation convention

| Element | Convention | Example |
|---|---|---|
| Observation ID | `O` + number | `O3` |
| Evidence ID | `E` + number | `E2` |
| Location | Use the user's scheme; otherwise paragraph and sentence | `para. 1, s.2` |
| Quotation | Double quotation marks, exact wording, under about 40 words | "numbered one through forty" |
| Omission | `[...]` | "the pans [...] were numbered" |
| Paraphrase | Add **(paraphrase)** | The ledger records debts as knots (paraphrase) |
| In-text claim | Claim followed by IDs in square brackets | "Counting converts the commons into units [E1, E2]." |

## 3. Markdown report template

Copy this structure. Remove guidance text in italics.

```markdown
# Critical Analysis Report: [Project or text title]

> *Status line: for example "Illustrative example" or "Draft for researcher review".*

## 1. Text and scope
- **Text:** title, author, date, edition/translation
- **Genre / form:**
- **Passage analysed:** location range and approximate word count
- **Copyright status:** public domain / user-owned / licensed / unknown
- **Unit of analysis and its limit:** *what the analysis can and cannot claim*

## 2. Research focus and assumptions
*One short paragraph stating the user's focus and any assumptions Claude made.*

## 3. Method summary
*Two to four sentences: close reading -> coding -> themes -> lens -> questions. Mention the tools used (none, or specific DH tools).*

## 4. Close-reading observations
| ID | Location | Observation (what is on the page) |
|---|---|---|
| O1 | | |

## 5. Codes
| Code | Definition | Observations |
|---|---|---|

## 6. Themes and evidence
### Theme 1: [claim-style label]
**Claim:** one sentence. **Confidence:** strong / plausible / speculative

| ID | Quotation | Location | Interpretation |
|---|---|---|---|
| E1 | | | |

**Counter-evidence / ambiguity:** *what complicates this theme.*

## 7. Theoretical interpretation
**Lens:** name (and secondary lens if any)
**Why this lens:** *link to evidence*
**Reading:** *claim -> evidence [E#] -> reasoning -> complication*
**What this lens makes visible / what it hides:**

## 8. Research questions
| # | Scale | Question | Why it works | Next step |
|---|---|---|---|---|
| RQ1 | text-level | | | |

*Mark the best fit and one ambitious option. Write "possible gap, to be checked" instead of asserting a gap in the literature.*

## 9. DH workflow suggestions
*Annotation scheme, corpus design, tools, and what each method cannot capture.*

## 10. Reflexivity, limitations and verification
- **Reflexivity note:** *positions that shape this reading*
- **Limitations:** *of the evidence, the lens and LLM assistance*
- **Verification checklist:**
  - [ ] Quotations and locations checked against the source
  - [ ] Critical and theoretical references checked in the original works
  - [ ] Context claims checked
  - [ ] Interpretation reviewed by the researcher
- **AI assistance note:** *suggested wording for disclosure*
```

## 4. JSON structure (`report+json` mode)

Output a single JSON object. `scripts/validate_output.py` checks the fields below.

| Field | Type | Required | Rule |
|---|---|---|---|
| `project_title` | string | Yes | Non-empty |
| `illustrative` | boolean | No | `true` for demonstration files |
| `text_information` | object | Yes | Must contain `title`, `author`, `genre`, `source_note`, `copyright_status` (all strings) |
| `text_information.copyright_status` | string | Yes | One of `public_domain`, `user_owned`, `licensed`, `in_copyright`, `original_fictional`, `unknown` |
| `research_focus` | string | Yes | Non-empty |
| `observations` | list of objects | Yes | At least 1; each has `id`, `location`, `description` |
| `themes` | list of objects | Yes | At least 1; each has `theme`, `claim`, `confidence`, `evidence` |
| `themes[].confidence` | string | Yes | One of `strong`, `plausible`, `speculative` |
| `themes[].evidence` | list of objects | Yes | At least 1; each has `id`, `quotation`, `location`, `interpretation` |
| `counter_evidence` | list of strings | Yes | At least 1 |
| `theoretical_framework` | object | Yes | Must contain `lens`, `justification`, `limits` |
| `interpretation` | string | Yes | Non-empty |
| `research_questions` | list of objects | Yes | At least 1; each has `question` and `scale` |
| `research_questions[].scale` | string | Yes | One of `text-level`, `corpus-level`, `context-level`, `method-level` |
| `dh_workflow_suggestions` | list of strings | No | If present, must be strings |
| `limitations` | list of strings | Yes | At least 1 |
| `verification_notes` | list of strings | Yes | At least 1 |
| `ethics_statement` | string | Yes | Non-empty |

The validator also **warns** (without failing) when a quotation is longer than 40 words, when evidence or observation IDs are duplicated, or when `illustrative` is missing.

A ready-made template can be generated with:

```
python scripts/validate_output.py --template my_analysis.json
```

## 5. Depth levels

| Depth | Length | Include |
|---|---|---|
| `brief` | about 400 words | Sections 1, 6 (1-2 themes), 7 (short), 8 (3 questions), 10 (limitations only) |
| `standard` | about 900 words | All sections, condensed tables |
| `full` | as needed (default for coursework) | All sections with complete tables and counter-evidence |

## 6. Style notes

- Write in clear academic English; define specialist terms on first use.
- Prefer short paragraphs and concrete verbs.
- Avoid "the author wants to show"; prefer "the passage constructs", "the narration withholds".
- Avoid excessive hedging; use the confidence labels instead.
- Do not add decorative praise ("beautifully written"); analyse instead.
