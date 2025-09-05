import json, os, sys, hashlib, time
CACHE = ".agent/research_cache.json"
os.makedirs(".agent", exist_ok=True)
data = {}
if os.path.isfile(CACHE):
    try: data = json.load(open(CACHE,"r",encoding="utf-8"))
    except Exception: data = {}
cmd = sys.argv[1] if len(sys.argv)>1 else "get"
key_input = sys.argv[2] if len(sys.argv)>2 else ""
key = hashlib.sha256(key_input.encode()).hexdigest() if key_input else ""
if cmd == "get":
    rec = data.get(key, {})
    if rec and time.time() - rec.get("ts", 0) < 60*60*24*7:  # 7 days
        print(json.dumps(rec))
    else:
        print("{}")
elif cmd == "put":
    payload = json.loads(sys.argv[3])
    data[key] = {"ts": time.time(), **payload}
    json.dump(data, open(CACHE,"w",encoding="utf-8"), indent=2)
    print("ok")
else:
    print("usage: research_cache.py get <question>| put <question> '<json>'", file=sys.stderr)
    sys.exit(1)
