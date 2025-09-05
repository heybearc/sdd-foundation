import os, re, json, sys
from pathlib import Path

def parse_examples(text:str):
    import re
    ex_blocks = re.findall(r'## Examples[\s\S]*?(?=\n## |\Z)', text, re.M)
    examples = []
    for block in ex_blocks:
        gs = re.findall(r'-\s*Example[^\n]*:?[\s\S]*?(?=\n-\s*Example|\Z)', block)
        for g in gs:
            given = re.findall(r'Given\s*(.*)', g)
            when = re.findall(r'When\s*(.*)', g)
            then = re.findall(r'Then\s*(.*)', g)
            examples.append({"given": given, "when": when, "then": then})
    return examples

def main():
    spec_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("specs")
    out_contracts = Path("contracts")
    out_tests = Path("tests/contract")
    out_contracts.mkdir(parents=True, exist_ok=True)
    out_tests.mkdir(parents=True, exist_ok=True)
    for spec in spec_dir.rglob("feature-spec.md"):
        text = spec.read_text(encoding="utf-8")
        ex = parse_examples(text)
        base = spec.parent.name
        schema_path = out_contracts / f"{base}.schema.json"
        test_path = out_tests / f"test_{base.replace('-', '_')}.py"
        schema = {"$schema": "https://json-schema.org/draft/2020-12/schema", "title": base, "type": "object", "properties": {}, "required": []}
        schema_path.write_text(json.dumps(schema, indent=2), encoding="utf-8")
        test_path.write_text(f"""
# Auto-generated from examples in {spec}
def test_contract_{base.replace('-', '_')}_fails_without_impl():
    assert False, "Implement contract and code to satisfy examples"
""", encoding="utf-8")
        print("Generated", schema_path, "and", test_path)
if __name__ == "__main__":
    main()
