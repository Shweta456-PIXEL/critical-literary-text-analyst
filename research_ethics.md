# Research Ethics

Guidance on reflexivity, bias, representation, copyright, transparency and verification when using an LLM in literary and cultural research. This file supports Steps 2 and 10 of `SKILL.md`.

## Contents

1. Researcher reflexivity
2. Bias: of the model, the corpus and the researcher
3. Representation and sensitive material
4. Copyright and permissions
5. Transparency and disclosure
6. Verification protocol
7. Ethics checklist

---

## 1. Researcher reflexivity

Interpretation is shaped by who reads. Reflexivity means recording how the researcher's position may influence the reading, not confessing for its own sake.

**Prompts to ask the user (or to answer briefly in the report):**

- What languages do I read the text in? Am I reading a translation?
- What is my relation to the community, region, period or tradition represented (insider, outsider, descendant, student of)?
- Which theories am I trained in, and which am I less familiar with?
- What do I expect to find, and what would surprise me?
- Whose criticism have I read, and whose have I not?
- How might my disciplinary habits (literary studies, social science, computing) lead me to emphasise some things?

**How Claude uses this:**

- Add a 2-3 sentence reflexivity note to every full report, using only what the user has shared. If the user has shared nothing, write: "No researcher position was supplied; the researcher should add one."
- Never invent a researcher's identity or background.
- Remind the user that Claude does not have a lived position and its reading may reproduce dominant critical habits.

## 2. Bias: of the model, the corpus and the researcher

| Source of bias | How it appears | Mitigation |
|---|---|---|
| Model training data | Defaulting to canonical, English-language, Euro-American interpretive frames; thin knowledge of regional, oral, Dalit, Adivasi, queer or diasporic traditions | Ask which local critical traditions exist; recommend searching regional scholarship; avoid asserting "the" meaning |
| Confirmation bias | Choosing a lens first and finding evidence for it | Code before choosing a lens; record counter-evidence |
| Corpus bias | Digital collections over-represent certain languages, periods and publishers; OCR performs worse on some scripts | Document how the corpus was built; report what is missing |
| Selection bias | Analysing only the most striking passages | State how passages were selected; sample systematically where possible |
| Presentism | Judging historical texts by present categories without discussing the difference | Name the anachronism risk; contextualise |
| Authority bias | Treating a fluent AI output as correct | Verify against the source |

## 3. Representation and sensitive material

- **Communities.** Do not generalise from a character or passage to an entire community. Use terms the text or community uses; flag analytic terms you bring from outside.
- **Stereotypes.** When a text contains stereotypes or slurs, analyse them as part of the text's construction, quote only what is necessary, and avoid reproducing slurs gratuitously.
- **Gender, caste, race, religion, disability, sexuality.** Treat as structural categories. Do not infer identity from names or appearance without textual evidence.
- **Trauma and testimony.** For narratives of violence, displacement or abuse, prioritise dignity; avoid extracting suffering as "data"; consider content warnings in outputs intended for others.
- **Indigenous, sacred or restricted knowledge.** Some oral traditions and ritual texts are governed by community protocols. Recommend checking permission and community guidelines before analysing, quoting, annotating or publishing. Consider the CARE principles (Collective benefit, Authority to control, Responsibility, Ethics) for Indigenous data governance.
- **Living people and unpublished material.** Interviews, letters, diaries and social media posts may require consent or institutional ethics review. Recommend consulting the institution's ethics committee or supervisor.
- **Archival material.** Respect access conditions, donor restrictions and privacy of named individuals.

If a request requires analysis of sensitive material and permissions are unclear, Claude should pause, state the concern, and suggest how to obtain clearance rather than refusing outright or ignoring the issue.

## 4. Copyright and permissions

- **Public domain** varies by country and by edition; a modern translation or critical edition can be in copyright even if the original is not. Ask the user for the edition.
- **Quotation:** use short quotations, with location markers, for the purpose of criticism or review; do not reproduce whole poems or substantial parts of in-copyright works. In this skill, keep each quotation under about 40 words and total quotation modest relative to the analysis.
- **Do not reconstruct text from memory.** If the user has not supplied the passage, ask for it.
- **Datasets and corpora:** check licences before sharing text files or derived datasets (for example Project Gutenberg, HathiTrust, institutional repositories). Share **metadata, codebooks and annotations** rather than full text when licensing is unclear.
- **Student and teaching examples:** use original passages written for the purpose and label them as illustrative (as done in `examples/`).
- **Images and manuscripts:** reproduction may need permission from the holding institution.
- **Not legal advice.** If rights are important to the project, the researcher should consult the library, supervisor or a rights officer.

## 5. Transparency and disclosure

- **Disclose AI assistance** as the institution requires. Suggested wording: "An LLM-based assistant was used to support close-reading notes, theme organisation and drafting of research questions. All quotations, interpretations and references were verified and revised by the researcher."
- **Record provenance** if outputs inform published work: model name and version, date, the text of the prompt, and any edits.
- **Distinguish** (a) what comes from the text, (b) what Claude inferred, (c) what comes from general knowledge, and (d) what the researcher decided.
- **Share the codebook and evidence table** with the final work so others can audit the reading.
- **Do not present outputs as expert consensus.** Interpretations are proposals.
- **Do not misrepresent** the model's reasoning as a human reader's experience.

## 6. Verification protocol

For every report, advise the researcher to complete these checks before using any claim.

1. **Quotation check.** Compare each quotation, word by word, with the source edition. Check punctuation and spelling.
2. **Location check.** Confirm every page, line or paragraph reference.
3. **Attribution check.** For each named theorist or concept, confirm the idea and its source in the primary work; never cite a source only because Claude mentioned it.
4. **Context check.** Verify historical, biographical and publication facts from reliable sources (editions, scholarly histories, archives).
5. **Alternative-reading check.** Ask: could a different reader, especially one from the text's own context, reasonably read this passage differently?
6. **Scope check.** Does any claim exceed the unit of analysis (passage, chapter, work, corpus)?
7. **Peer check.** Share the analysis with a supervisor or peer for a second reading.
8. **Reproducibility check.** If using computational steps, save scripts, parameters and data versions.

**Claude's behaviour when uncertain:** state the uncertainty, label the claim `[unverified]`, and suggest how to check it. Never invent a citation, page number or biographical fact to fill a gap.

## 7. Ethics checklist

- [ ] The text was supplied by the user, and its copyright status is known or assumed in-copyright.
- [ ] Quotations are short, located and necessary.
- [ ] Sensitive, restricted or community-owned material has been identified, and permissions considered.
- [ ] No claims are made about living people beyond what the supplied text supports.
- [ ] Reflexivity note is included or flagged for the researcher.
- [ ] Biases of the model, corpus and researcher are acknowledged.
- [ ] AI assistance disclosure text is provided.
- [ ] Verification steps are listed.
