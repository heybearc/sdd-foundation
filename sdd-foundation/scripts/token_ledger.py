import json, os
LEDGER = ".agent/ledger.json"
os.makedirs(".agent", exist_ok=True)
entry = {
    "feature_branch": os.popen("git branch --show-current").read().strip(),
    "prompt_tokens": int(os.environ.get("PROMPT_TOKENS", "0")),
    "completion_tokens": int(os.environ.get("COMPLETION_TOKENS", "0")),
}
data = []
if os.path.isfile(LEDGER):
    try:
        data = json.load(open(LEDGER, "r", encoding="utf-8"))
    except Exception:
        data = []
data.append(entry)
json.dump(data, open(LEDGER, "w", encoding="utf-8"), indent=2)
print("Logged token usage to", LEDGER)
