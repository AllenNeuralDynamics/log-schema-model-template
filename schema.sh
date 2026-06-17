#!/usr/bin/env bash
# Regenerates src/log-schema-template/custom/*.py from schemas/*.json using datamodel-codegen.
# Run from anywhere:  bash schema/schema.sh
# Or make executable: chmod +x schema/schema.sh && ./schema/schema.sh
set -euo pipefail

# Always operate relative to the repo root, regardless of where the script is called from.
REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"

SCHEMAS_DIR="$REPO_ROOT/schemas"
OUTPUT_DIR="$REPO_ROOT/src/log_schema_template/generated"

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

uv run datamodel-codegen \
  --input "$SCHEMAS_DIR" \
  --input-file-type jsonschema \
  --output "$OUTPUT_DIR" \
  --output-model-type pydantic_v2.BaseModel \
  --use-default \
  --use-default-kwarg \
  --strict-nullable
