# Critical Literary Text Analyst

A modular **LLM Skill** that helps Digital Humanities researchers critically analyse literary and cultural texts: close reading, thematic analysis, evidence extraction, theoretical interpretation, research question development and preliminary DH workflow planning.

Created for the **DH Lab 2** assignment "Creating a Skill for LLM".

---

## 1. Project purpose

Language models can produce fluent but unsupported readings of literature. This skill instructs the model to work the way a careful researcher does:

- separate **observation** from **inference** from **theory**;
- support every claim with **short, located quotations**;
- report **counter-evidence** and **confidence**;
- choose a theoretical lens that **fits the evidence**;
- state **limitations**, researcher **reflexivity** and **verification** steps;
- respect **copyright** and **research ethics**.

It is designed as a research aid for a postgraduate workflow, not as a replacement for the researcher's own reading and argument.

## 2. Folder structure

```
critical-literary-text-analyst/
|
|-- SKILL.md                          Main skill: metadata, workflow, rules, output format
|-- README.md                         This file
|
|-- references/                       Modules the skill reads on demand
|   |-- analysis_workflow.md          Close reading, coding, themes, evidence, RQ development, DH steps
|   |-- theoretical_lenses.md         Postcolonialism, ecocriticism, intersectionality, affect, etc.
|   |-- output_format.md              Report template and JSON structure
|   `-- research_ethics.md            Reflexivity, bias, representation, copyright, verification
|
|-- examples/                         Illustrative material (original fictional passage)
|   |-- sample_input.md               Example request and passage
|   |-- sample_output.md              Example report plus JSON version
|   `-- sample_research_questions.md  Example of question development
|
`-- scripts/
    |-- validate_output.py            Checks the structure of a JSON analysis file
    `-- requirements.txt              Dependencies (none beyond the standard library)
```

## 3. How to use the skill

The skill is a folder whose entry point is `SKILL.md`. The YAML block at the top (`name`, `description`) lets a compatible assistant decide when to load it.

**Option A - Claude (Skills feature).** Zip the folder (the folder itself must be at the top of the ZIP), then in Claude go to *Settings -> Capabilities -> Skills* and upload the ZIP. Availability depends on your plan and Claude's current interface; check Anthropic's documentation if the menu differs.

**Option B - Claude Code or other agent tools.** Place the folder where the tool looks for skills (for Claude Code, a `.claude/skills/` folder in a project or in your home directory). Check the tool's documentation for the current location.

**Option C - Any chat-based LLM (no skills feature).** Paste the contents of `SKILL.md` as the first message (or as a system prompt) and then attach or paste the reference files that you need. This is slower but works anywhere.

**Typical request**

> Use the Critical Literary Text Analyst skill. Text: [paste passage]. Title/author/edition: [...]. Copyright status: [public domain / mine / unknown]. Research focus: [...]. Depth: standard. Output: report + json.

See `examples/sample_input.md` for a complete example. The skill asks up to three clarifying questions if essential information is missing.

## 4. How to use the reference modules

Each module is loaded only when needed, so the main skill stays short.

| Module | Use it for |
|---|---|
| `references/analysis_workflow.md` | The detailed method: how to observe, code, build themes, extract evidence and test research questions. Read it when you want to do the analysis step by step yourself. |
| `references/theoretical_lenses.md` | Choosing and applying a lens. It includes guiding questions, evidence cues and cautions for each framework, plus a lens fit table. |
| `references/output_format.md` | The report template and the JSON structure, so outputs are consistent across texts. |
| `references/research_ethics.md` | Reflexivity prompts, bias checks, sensitive-material guidance, copyright rules, disclosure wording and a verification protocol. |

You can also read the modules as a student: `analysis_workflow.md` works as a method guide, and `theoretical_lenses.md` as a revision sheet (always verify against the original theoretical texts).

## 5. How to run the Python validator

`scripts/validate_output.py` checks that a JSON analysis file has the required fields, correct types, allowed values and non-empty content. It uses only Python's standard library (Python 3.8 or newer).

```bash
# 1. Open a terminal in the project folder
cd critical-literary-text-analyst

# 2. Create a template file you can edit (will not overwrite existing files)
python scripts/validate_output.py --template my_analysis.json

# 3. Validate a file
python scripts/validate_output.py my_analysis.json
```

On some systems the command is `python3` instead of `python`.

**What it checks**

- the file exists and is valid JSON (with line and column of any syntax error);
- all required fields are present (missing-field check) and have the right type;
- lists such as `observations`, `themes` and `limitations` are not empty;
- `confidence`, `scale` and `copyright_status` use allowed values;
- every theme has at least one evidence item with `id`, `quotation`, `location` and `interpretation`;
- **warnings** (not errors) for duplicate IDs, quotations over 40 words, and a missing `illustrative` flag.

**Example outputs**

```
RESULT: VALID - 'my_analysis.json' has all required fields.
```

```
Errors (2):
  - Missing required field: 'ethics_statement'
  - 'themes[0].confidence' has the value 'high'; allowed values are: strong, plausible, speculative

RESULT: INVALID - fix the errors above and run again.
```

Exit code is `0` for valid files and `1` for invalid ones, so the script can also be used in automated checks.

### Sample JSON structure

A shortened structure (the complete version is in `examples/sample_output.md` and in `references/output_format.md`, section 4):

```json
{
  "project_title": "Critical Analysis Report: Title",
  "illustrative": false,
  "text_information": {
    "title": "Title of the text",
    "author": "Author",
    "genre": "Short story",
    "source_note": "Edition and year",
    "copyright_status": "public_domain"
  },
  "research_focus": "What you want to find out",
  "observations": [
    {"id": "O1", "location": "para. 1, s.1", "description": "What is on the page"}
  ],
  "themes": [
    {
      "theme": "Short label",
      "claim": "One-sentence claim",
      "confidence": "plausible",
      "evidence": [
        {"id": "E1", "quotation": "Short exact quote", "location": "para. 1, s.1", "interpretation": "Why it matters"}
      ]
    }
  ],
  "counter_evidence": ["Something that complicates the reading"],
  "theoretical_framework": {
    "lens": "Name of lens",
    "justification": "Why it fits the evidence",
    "limits": "What it hides"
  },
  "interpretation": "Argument citing [E1].",
  "research_questions": [
    {"question": "Your question?", "scale": "text-level"}
  ],
  "dh_workflow_suggestions": ["Optional next steps"],
  "limitations": ["A limitation"],
  "verification_notes": ["What to check"],
  "ethics_statement": "Copyright, permissions, AI-assistance disclosure"
}
```

Allowed values: `confidence` = `strong | plausible | speculative`; `scale` = `text-level | corpus-level | context-level | method-level`; `copyright_status` = `public_domain | user_owned | licensed | in_copyright | original_fictional | unknown`.

## 6. Example input and output

> All examples are **illustrative**. They use an original fictional passage, "The Salt Ledger", written for this project. No published or copyrighted text is used.

**Input (`examples/sample_input.md`, shortened)**

> *The surveyor arrived in the dry month [...] By evening the creek that the women called Amma-thodu had become "Cutter's Channel" on his map, and the pans [...] were numbered one through forty.*
> Focus: land, naming and records. Depth: standard. Output: report + json.

**Output (`examples/sample_output.md`, summary)**

| Element | Result |
|---|---|
| Observations | 9 numbered observations with locations |
| Themes | (1) surveying and naming turn a commons into taxable property (strong); (2) written records set against knotted and oral records (plausible); (3) the environment acts beyond human inscription (plausible) |
| Lens | Postcolonial theory (epistemic violence) with ecocriticism; the report notes that the colonial setting is inferred, not stated |
| Research questions | 5 questions across text, context, corpus and method scales |
| Extras | Counter-evidence, DH workflow, reflexivity note, verification checklist, JSON version |

To test the validator on the sample, copy the JSON block from the end of `examples/sample_output.md` into a file named `analysis.json` and run `python scripts/validate_output.py analysis.json`.

## 7. Limitations

- **Not a substitute for reading.** The skill supports analysis of supplied passages; it cannot replace reading the full text or consulting scholarship.
- **Model bias.** LLMs over-represent canonical, English-language and Global North interpretive traditions. Regional, oral and minority texts need local critical sources.
- **Unreliable references.** Models can invent quotations, page numbers and citations. Every quotation, location and theoretical reference must be verified against the original.
- **Partial context.** A short passage cannot support claims about a whole work, author or period.
- **No lived position.** The model has no cultural or emotional stake in a text; reflexivity must come from the researcher.
- **Variable output.** Results differ between runs and model versions.
- **Theory summaries are simplified.** `theoretical_lenses.md` is a starting point, not a substitute for the primary works.
- **Validator scope.** `validate_output.py` checks structure only; it cannot judge whether an interpretation is good.
- **Academic integrity.** Follow your institution's policy on AI use and disclose assistance (suggested wording is in `references/research_ethics.md`).

## 8. Author details

| | |
|---|---|
| **Name** | Shweta Kumari |
| **Programme** | MA Digital Humanities & Social Sciences |
| **Institution** | IIT (ISM) Dhanbad |
| **Semester** | Monsoon Semester 2026 |
| **Course assignment** | DH Lab 2 - Creating a Skill for LLM |

## 9. Licence and attribution note

The example passage and all example outputs were written for this project and are illustrative. Theoretical concepts are summarised in the author's words with attribution to their originators; consult the original works for exact formulations. Add a licence file (for example MIT or CC BY 4.0) to the repository if you want others to reuse it.
