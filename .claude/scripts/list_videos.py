import json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
for f in sorted(Path('raw/youtube').glob('*.info.json')):
    try:
        d = json.loads(f.read_text(encoding='utf-8'))
        print(f"{d.get('upload_date','')} | {d.get('uploader','')} | {d.get('title','')} | {d.get('duration_string','')}")
    except Exception as e:
        print(f"ERROR: {f.name}: {e}")
