#!/usr/bin/env python3
"""
validate_output.py - check the structure of a JSON research analysis file.

Part of the "Critical Literary Text Analyst" skill.
The expected structure is described in references/output_format.md (section 4).

Usage
-----
    python validate_output.py analysis.json            # validate a file
    python validate_output.py --template my_file.json  # write a blank template

Exit codes
----------
    0  the file is valid (warnings may still be printed)
    1  the file is invalid, missing, or not readable JSON
    2  wrong command-line usage

Only the Python standard library is used (Python 3.8+).
"""

import argparse
import json
import os
import sys

# --------------------------------------------------------------------------
# Rules (edit these if your skill's output format changes)
# --------------------------------------------------------------------------

# Top-level fields that must exist, with the type each must have.
REQUIRED_TOP_LEVEL = {
    "project_title": str,
    "text_information": dict,
    "research_focus": str,
    "observations": list,
    "themes": list,
    "counter_evidence": list,
    "theoretical_framework": dict,
    "interpretation": str,
    "research_questions": list,
    "limitations": list,
    "verification_notes": list,
    "ethics_statement": str,
}

# Optional fields that, if present, must have the given type.
OPTIONAL_TOP_LEVEL = {
    "illustrative": bool,
    "dh_workflow_suggestions": list,
}

TEXT_INFO_FIELDS = ["title", "author", "genre", "source_note", "copyright_status"]
COPYRIGHT_VALUES = [
    "public_domain", "user_owned", "licensed",
    "in_copyright", "original_fictional", "unknown",
]
OBSERVATION_FIELDS = ["id", "location", "description"]
THEME_FIELDS = ["theme", "claim", "confidence", "evidence"]
CONFIDENCE_VALUES = ["strong", "plausible", "speculative"]
EVIDENCE_FIELDS = ["id", "quotation", "location", "interpretation"]
FRAMEWORK_FIELDS = ["lens", "justification", "limits"]
QUESTION_FIELDS = ["question", "scale"]
SCALE_VALUES = ["text-level", "corpus-level", "context-level", "method-level"]

# Lists that must contain at least one item.
NON_EMPTY_LISTS = [
    "observations", "themes", "counter_evidence",
    "research_questions", "limitations", "verification_notes",
]

MAX_QUOTE_WORDS = 40  # longer quotations produce a copyright-caution warning

TEMPLATE = {
    "project_title": "Title of your analysis",
    "illustrative": False,
    "text_information": {
        "title": "Title of the text",
        "author": "Author name",
        "genre": "For example: poem, short story, novel excerpt",
        "source_note": "Edition, translation, year, where you found it",
        "copyright_status": "unknown",
    },
    "research_focus": "What you want to find out",
    "observations": [
        {"id": "O1", "location": "para. 1, s.1", "description": "What is on the page."}
    ],
    "themes": [
        {
            "theme": "Short label for the theme",
            "claim": "One-sentence claim about what the text does",
            "confidence": "plausible",
            "evidence": [
                {
                    "id": "E1",
                    "quotation": "Short exact quotation",
                    "location": "para. 1, s.1",
                    "interpretation": "Why this supports the claim",
                }
            ],
        }
    ],
    "counter_evidence": ["A passage or ambiguity that complicates your reading"],
    "theoretical_framework": {
        "lens": "Name of the lens",
        "justification": "Why this lens fits the evidence",
        "limits": "What the lens hides or strains",
    },
    "interpretation": "Your argument, citing evidence IDs such as [E1].",
    "research_questions": [
        {"question": "Your research question?", "scale": "text-level"}
    ],
    "dh_workflow_suggestions": ["Optional: annotation scheme, tools, corpus"],
    "limitations": ["A limitation of the evidence, lens or method"],
    "verification_notes": ["What you will check against the source"],
    "ethics_statement": "Copyright, permissions, AI-assistance disclosure.",
}


# --------------------------------------------------------------------------
# Small helper functions
# --------------------------------------------------------------------------

def type_name(value):
    """Return a friendly type name for error messages."""
    names = {dict: "object", list: "list", str: "text", bool: "true/false",
             int: "number", float: "number", type(None): "null"}
    return names.get(type(value), type(value).__name__)


def is_blank(value):
    """True if value is not a string or is empty/whitespace."""
    return not isinstance(value, str) or value.strip() == ""


def check_text_field(obj, field, path, errors):
    """Check that obj[field] exists and is a non-empty string."""
    if field not in obj:
        errors.append("Missing field: '%s.%s'" % (path, field))
    elif not isinstance(obj[field], str):
        errors.append("'%s.%s' must be text, but found %s"
                      % (path, field, type_name(obj[field])))
    elif obj[field].strip() == "":
        errors.append("'%s.%s' is empty" % (path, field))


def check_choice(obj, field, allowed, path, errors):
    """Check that obj[field] is one of the allowed values (if it is text)."""
    value = obj.get(field)
    if isinstance(value, str) and value.strip() != "" and value not in allowed:
        errors.append("'%s.%s' has the value '%s'; allowed values are: %s"
                      % (path, field, value, ", ".join(allowed)))


def check_object_list(items, name, fields, errors):
    """Check every item in a list is an object containing the given text fields.
    Returns the items that are valid objects so callers can go deeper."""
    valid = []
    for i, item in enumerate(items):
        path = "%s[%d]" % (name, i)
        if not isinstance(item, dict):
            errors.append("'%s' must be an object, but found %s"
                          % (path, type_name(item)))
            continue
        valid.append((path, item))
        for field in fields:
            if field == "evidence":
                continue  # lists are checked separately
            check_text_field(item, field, path, errors)
    return valid


def check_string_list(items, name, errors):
    """Check every item in a list is a non-empty string."""
    for i, item in enumerate(items):
        if is_blank(item):
            errors.append("'%s[%d]' must be non-empty text" % (name, i))


def check_duplicate_ids(ids, label, warnings):
    seen = set()
    for item_id in ids:
        if item_id in seen:
            warnings.append("Duplicate %s ID '%s'" % (label, item_id))
        seen.add(item_id)


# --------------------------------------------------------------------------
# Main validation
# --------------------------------------------------------------------------

def validate(data):
    """Validate the parsed JSON. Returns (errors, warnings), both lists of text."""
    errors, warnings = [], []

    if not isinstance(data, dict):
        errors.append("The top level of the file must be an object { ... }, "
                      "but found %s" % type_name(data))
        return errors, warnings

    # 1. Required top-level fields: missing-field and type checks
    for field, expected in REQUIRED_TOP_LEVEL.items():
        if field not in data:
            errors.append("Missing required field: '%s'" % field)
        elif not isinstance(data[field], expected):
            errors.append("'%s' must be %s, but found %s"
                          % (field, type_name(expected()), type_name(data[field])))

    for field, expected in OPTIONAL_TOP_LEVEL.items():
        if field in data and not isinstance(data[field], expected):
            errors.append("'%s' must be %s, but found %s"
                          % (field, type_name(expected()), type_name(data[field])))

    # 2. Plain text fields must not be empty
    for field in ("project_title", "research_focus", "interpretation",
                  "ethics_statement"):
        if isinstance(data.get(field), str) and data[field].strip() == "":
            errors.append("'%s' is empty" % field)

    # 3. Lists that need at least one item
    for field in NON_EMPTY_LISTS:
        if isinstance(data.get(field), list) and len(data[field]) == 0:
            errors.append("'%s' must contain at least one item" % field)

    # 4. text_information
    info = data.get("text_information")
    if isinstance(info, dict):
        for field in TEXT_INFO_FIELDS:
            check_text_field(info, field, "text_information", errors)
        check_choice(info, "copyright_status", COPYRIGHT_VALUES,
                     "text_information", errors)

    # 5. observations
    if isinstance(data.get("observations"), list):
        valid = check_object_list(data["observations"], "observations",
                                  OBSERVATION_FIELDS, errors)
        check_duplicate_ids([o.get("id") for _, o in valid
                             if isinstance(o.get("id"), str)],
                            "observation", warnings)

    # 6. themes and their evidence
    evidence_ids = []
    if isinstance(data.get("themes"), list):
        for t_path, theme in check_object_list(data["themes"], "themes",
                                               THEME_FIELDS, errors):
            check_choice(theme, "confidence", CONFIDENCE_VALUES, t_path, errors)
            evidence = theme.get("evidence")
            if "evidence" not in theme:
                continue  # already reported as a missing field
            if not isinstance(evidence, list):
                errors.append("'%s.evidence' must be a list, but found %s"
                              % (t_path, type_name(evidence)))
            elif len(evidence) == 0:
                errors.append("'%s.evidence' must contain at least one item"
                              % t_path)
            else:
                for e_path, ev in check_object_list(
                        evidence, t_path + ".evidence", EVIDENCE_FIELDS, errors):
                    if isinstance(ev.get("id"), str):
                        evidence_ids.append(ev["id"])
                    quote = ev.get("quotation")
                    if isinstance(quote, str):
                        words = len(quote.split())
                        if words > MAX_QUOTE_WORDS:
                            warnings.append(
                                "'%s.quotation' has %d words (more than %d). "
                                "Shorten it or paraphrase, for copyright caution."
                                % (e_path, words, MAX_QUOTE_WORDS))
        check_duplicate_ids(evidence_ids, "evidence", warnings)

    # 7. theoretical_framework
    framework = data.get("theoretical_framework")
    if isinstance(framework, dict):
        for field in FRAMEWORK_FIELDS:
            check_text_field(framework, field, "theoretical_framework", errors)

    # 8. research_questions
    if isinstance(data.get("research_questions"), list):
        for q_path, q in check_object_list(data["research_questions"],
                                           "research_questions",
                                           QUESTION_FIELDS, errors):
            check_choice(q, "scale", SCALE_VALUES, q_path, errors)

    # 9. Lists of plain strings
    for field in ("counter_evidence", "limitations", "verification_notes",
                  "dh_workflow_suggestions"):
        if isinstance(data.get(field), list):
            check_string_list(data[field], field, errors)

    # 10. Soft warnings (these do not make the file invalid)
    if "illustrative" not in data:
        warnings.append("Optional field 'illustrative' is missing. Add "
                        "\"illustrative\": true if this is a demonstration file.")

    return errors, warnings


def load_json(path):
    """Read and parse a JSON file. Returns (data, error_message)."""
    if not os.path.isfile(path):
        return None, "File not found: '%s'. Check the path and file name." % path
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle), None
    except UnicodeDecodeError:
        return None, ("Could not read '%s' as UTF-8 text. Re-save the file "
                      "with UTF-8 encoding." % path)
    except json.JSONDecodeError as exc:
        return None, ("Invalid JSON in '%s': %s (line %d, column %d). "
                      "Common causes: a missing comma, a trailing comma, or "
                      "single quotes instead of double quotes."
                      % (path, exc.msg, exc.lineno, exc.colno))
    except OSError as exc:
        return None, "Could not open '%s': %s" % (path, exc)


def write_template(path):
    """Write a blank, valid-structure template file."""
    if os.path.exists(path):
        print("Refusing to overwrite existing file: %s" % path)
        return 1
    try:
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(TEMPLATE, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
    except OSError as exc:
        print("Could not write template: %s" % exc)
        return 1
    print("Template written to %s. Edit it, then run:" % path)
    print("    python validate_output.py %s" % path)
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate the structure of a JSON literary analysis file.")
    parser.add_argument("file", nargs="?",
                        help="path to the JSON analysis file to check")
    parser.add_argument("--template", metavar="OUTPUT",
                        help="write a template JSON file to OUTPUT and exit")
    args = parser.parse_args(argv)

    if args.template:
        return write_template(args.template)

    if not args.file:
        parser.print_usage()
        print("Error: please give the path of a JSON file, or use --template.")
        return 2

    data, load_error = load_json(args.file)
    if load_error:
        print("ERROR: " + load_error)
        return 1

    errors, warnings = validate(data)

    if warnings:
        print("Warnings (%d):" % len(warnings))
        for message in warnings:
            print("  - " + message)
    if errors:
        print("\nErrors (%d):" % len(errors))
        for message in errors:
            print("  - " + message)
        print("\nRESULT: INVALID - fix the errors above and run again.")
        return 1

    print("\nRESULT: VALID - '%s' has all required fields." % args.file)
    return 0


if __name__ == "__main__":
    sys.exit(main())
