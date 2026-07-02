"""Generate Pydantic models from the merged OpenAPI spec.

Regenerates ``src/sympheny_toolbox/models.py`` from ``docs/sympheny_openapi.json``
using datamodel-code-generator (dev dependency). Rerun after any spec change:

    uv run python scripts/generate_models.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SPEC = REPO_ROOT / "docs" / "sympheny_openapi.json"
OUTPUT = REPO_ROOT / "src" / "sympheny_toolbox" / "models.py"


def main() -> None:
    cmd = [
        "datamodel-codegen",
        "--input",
        str(SPEC),
        "--input-file-type",
        "openapi",
        "--output",
        str(OUTPUT),
        "--output-model-type",
        "pydantic_v2.BaseModel",
        "--target-python-version",
        "3.11",
        "--snake-case-field",
        "--field-constraints",
        "--set-default-enum-member",
        "--allow-population-by-field-name",
        "--use-standard-collections",
        "--use-union-operator",
        "--use-schema-description",
        "--collapse-root-models",
        "--use-double-quotes",
        "--disable-timestamp",
        "--custom-file-header",
        (
            '"""Pydantic models generated from docs/sympheny_openapi.json — do NOT edit by hand.\n\n'
            'Regenerate with: uv run python scripts/generate_models.py\n"""'
        ),
    ]
    result = subprocess.run(cmd, cwd=REPO_ROOT, check=False)  # noqa: S603
    if result.returncode != 0:
        sys.exit(result.returncode)
    # Avoid the pydantic[email] extra (email-validator) for a single login field.
    text = OUTPUT.read_text()
    text = text.replace("EmailStr,\n", "").replace(": EmailStr", ": str")
    OUTPUT.write_text(text)
    subprocess.run(["uv", "run", "ruff", "format", str(OUTPUT)], cwd=REPO_ROOT, check=True)  # noqa: S603, S607
    subprocess.run(["uv", "run", "ruff", "check", "--fix", str(OUTPUT)], cwd=REPO_ROOT, check=False)  # noqa: S603, S607
    print(f"Wrote {OUTPUT.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
