# Analysis Workflow

Detailed procedures for Steps 3-8 of the main `SKILL.md`. Read the sections you need.

## Contents

1. Preparing the text
2. Close reading
3. Observation versus inference
4. Open coding
5. Theme identification
6. Evidence extraction
7. Interpretation
8. Research question development
9. Moving toward a DH workflow
10. Quality checklist

---

## 1. Preparing the text

- Fix a **citation scheme** before reading: page, line, stanza, paragraph (para.), or scene/act. If the user supplied none, number sentences or paragraphs (for example `para. 2, s.1`) and say so.
- Note the **edition**: translation, abridgement, serialised or book version. These change what counts as evidence.
- Note **paratext** if supplied: title, epigraph, preface, glossary, footnotes. Paratext often frames interpretation.
- Decide the **unit of analysis**: a passage, a chapter, a whole work, or a corpus. Do not move beyond it without saying so.

## 2. Close reading

Work through the text in its own order. Revisit it at least twice: once for what happens, once for how it is told. Use the prompts below as a menu, not a checklist - skip those that the text gives you nothing on.

| Dimension | Prompts |
|---|---|
| Diction | Which words are repeated, unusual, archaic, borrowed or untranslated? Which semantic fields recur (law, water, kinship, money)? |
| Syntax | Are sentences short or accumulative? Where do lists, inversions or fragments occur? Who is the grammatical subject of action? |
| Voice and focalisation | Who speaks? Who sees? Is the narrator inside or outside the community described? Does the voice shift? |
| Form and structure | What is the sequence of events or images? Where are the turns, breaks, endings? How does form (verse, stanza, chapter) shape meaning? |
| Imagery and figuration | Metaphors, similes, symbols, personification. What is compared with what, and what does the comparison permit or hide? |
| Time and space | Tense, duration, flashback, seasons; named and unnamed places; who controls naming? |
| Characters and relations | Who has agency? Who is silent, absent or spoken for? Kinship, class, caste, gender, race, citizenship as marked by the text. |
| Sound and rhythm | For verse and performance texts: metre, alliteration, refrain, orality. |
| Intertexts and references | Allusions, genre conventions, inherited forms, other languages. |
| Silences and gaps | What is withheld, euphemised or ellipsed? What would one expect the text to say that it does not? |

**Output of this stage:** a list of numbered observations (O1, O2...), each tied to a location.

## 3. Observation versus inference

This separation is the single biggest guard against over-reading.

| | Observation | Inference |
|---|---|---|
| What it is | A verifiable feature of the text | A claim about meaning or effect |
| Test | Could two readers agree on it without discussion? | Could a reasonable reader disagree? |
| Example | "The creek is *renamed*, while the pans are *numbered*." (O2, O3) | "The text links colonial administration with the conversion of shared resources into taxable units." |
| Marker phrases | "The passage repeats...", "The narrator uses..." | "This suggests...", "This may indicate...", "One reading is..." |

Write the observation first, then the inference, and attach the confidence level (strongly supported / plausible / speculative).

## 4. Open coding

1. Read observations in order and give each a **short descriptive code** (2-4 words).
2. Prefer **in-vivo** codes (the text's own words) or **descriptive** codes ("naming as ownership") before **conceptual** codes ("epistemic violence").
3. Merge duplicates, split codes that cover different things, and keep a **codebook** with a one-line definition per code.
4. Record how many observations each code covers; codes with a single instance may be noted but should not carry a theme alone.
5. Keep a "memo" line for puzzles you cannot yet explain.

**Mini example (from the illustrative passage in `examples/sample_input.md`):**

| Observation | Code |
|---|---|
| The creek's name changes from *Amma-thodu* to *Cutter's Channel* (O2) | renaming as appropriation |
| Pans "belonged to no one and to everyone" become numbered one to forty (O3) | commons turned into units |
| Savitri understands the numbers though she cannot read English (O5) | non-literate calculation |
| Debts recorded as knots in thread (O6) | alternative record-keeping |

## 5. Theme identification

A **theme** is a pattern of meaning supported by multiple codes, expressed as a *claim*, not a topic label.

- Weak: "Colonialism."
- Stronger: "The passage presents surveying and naming as acts that convert shared ecological space into administrable property."

**Tests for a theme:**

1. **Recurrence** - supported by at least two independent observations from different parts of the text.
2. **Specificity** - says something about *this* text, not any text.
3. **Agency of the text** - describes what the text does (shows, withholds, contrasts), not only what it is about.
4. **Counter-evidence** - you have looked for contradictions and recorded them.
5. **Distinctness** - not a restatement of another theme.

Aim for 2-4 themes for a short passage and 4-7 for a chapter. Rank by strength of evidence, not by how interesting they are.

## 6. Evidence extraction

For each theme, build an **evidence table**:

| ID | Quotation (short) | Location | Observation / interpretation | Strength |
|---|---|---|---|---|
| E1 | "numbered one through forty" | para. 1 | Counting imposes a new grid on an unquantified commons | Strong |

Rules:

- Quotations must be **exact**, short (normally under 40 words) and **located**.
- Use ellipses `[...]` for omissions and square brackets for insertions; never silently alter wording.
- If the text is in translation, mark it, and if the original language is available, add the original term in a separate column or note.
- If a paraphrase is used instead of a quotation, mark it **(paraphrase)**.
- Give each piece of evidence an ID so the interpretation can cite it as `[E1]`.
- Prefer **three small pieces of evidence** over one long quotation.

## 7. Interpretation

Move from evidence to argument in three layers.

1. **Local reading** - what the passage does on its own terms.
2. **Contextual reading** - what historical, social, ecological or literary context makes this meaningful (state clearly what comes from the user's materials and what from general knowledge that needs verifying).
3. **Theoretical reading** - what a chosen lens (see `theoretical_lenses.md`) highlights or hides.

Template for a paragraph of interpretation:

> *Claim.* (one sentence) -> *Evidence* [E#, E#] -> *Reasoning* (why the evidence supports the claim) -> *Complication* (counter-evidence, ambiguity, alternative lens) -> *Confidence* (strong / plausible / speculative).

Avoid: summarising instead of interpreting; claiming authorial intention without evidence; treating a character's view as the text's view; "the author wants to show..." as a default opener.

## 8. Research question development

Generate questions at four scales:

| Scale | Example pattern |
|---|---|
| Text-level | How does [formal device] in [text/passage] construct [concept]? |
| Corpus/author-level | How do [texts/authors] across [period/region] represent [concept], and what changes over time? |
| Context-level | In what ways does [text] respond to or contest [historical/social discourse]? |
| Method-level | What can [DH method] reveal or conceal about [concept] in [corpus] compared to close reading? |

**Test every question against these criteria:**

1. **Answerable** - evidence exists or can be gathered with available sources and time.
2. **Evidence-bound** - answerable from the text(s), not only from opinion.
3. **Non-obvious** - not answerable by a yes/no or by a summary.
4. **Scoped** - fits the length and resources of the project (a seminar paper, a dissertation, a lab project).
5. **Positioned** - connects to a debate, concept or gap, even if the literature is still to be searched.
6. **Ethically feasible** - does not require data or access that raises unaddressed ethical issues.

Provide 3-5 questions, mark which is the **best fit** for the user's stated focus, and say why. Offer one **riskier** question that is more ambitious. Do not claim that a gap exists in the literature unless the user has done a search; write "possible gap, to be checked".

## 9. Moving toward a DH workflow

Match method to question. Use the table to propose, not to prescribe.

| Question type | Possible DH step | What it can do | What it cannot do |
|---|---|---|---|
| How is X represented across many texts? | Corpus building + manual annotation (spreadsheet or TEI-lite) | Systematic comparison of coded passages | Replace interpretation of tone and irony |
| Which words cluster around X? | Concordance / collocation (for example AntConc, Voyant, Python NLTK) | Reveals patterns of co-occurrence | Capture meaning not tied to specific words |
| Has X's vocabulary changed over time? | Time-sliced word frequency | Shows shifts in usage | Explain why the shift occurred |
| Which topics recur? | Topic modelling | Exploratory overview of large corpora | Provide reliable themes for a single short text |
| Where are places and people named? | Named-entity recognition + mapping | Spatial and network views | Distinguish contested or unnamed places |
| How is a text edited or transmitted? | Digital edition (TEI) | Documents variants and annotation | Settle interpretation |

Rules of thumb:

- Start small: annotate 20-30 passages by hand first to validate the codebook before scaling.
- Record **inter-rater checks** if more than one coder is involved (even a simple second-coder sample of 10-20%).
- Document tools, versions, parameters and preprocessing choices (lemmatisation, stop-words, OCR corrections).
- State what is lost when moving from text to data: tone, irony, silence, form.

## 10. Quality checklist

Before delivering, confirm:

- [ ] Every claim traces to a located piece of evidence or is labelled speculative.
- [ ] Observations and inferences are separated.
- [ ] At least one counter-evidence item or alternative reading is included.
- [ ] Quotations are short, exact and located; copyright limits respected.
- [ ] The theoretical lens is justified and its limits stated.
- [ ] Research questions meet the six criteria.
- [ ] Reflexivity and limitations are stated.
- [ ] Nothing is invented: no fabricated references, page numbers or facts.
