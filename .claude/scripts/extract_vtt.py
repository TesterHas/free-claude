"""Extract clean text from VTT files and output structured summaries."""
import sys
import re
import json
from pathlib import Path

def extract_clean_text(vtt_path):
    """Parse VTT, strip timing tags, deduplicate, return clean transcript."""
    text = Path(vtt_path).read_text(encoding='utf-8', errors='replace')
    lines = text.splitlines()

    seen = set()
    clean = []
    for line in lines:
        # Skip WEBVTT header, timestamps, empty lines
        if line.startswith('WEBVTT') or '-->' in line or not line.strip():
            continue
        # Strip inline timing tags like <00:00:01.000> and <c>...</c>
        clean_line = re.sub(r'<[^>]+>', '', line).strip()
        if clean_line and clean_line not in seen:
            seen.add(clean_line)
            clean.append(clean_line)

    return ' '.join(clean)

def main():
    raw_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('raw/youtube')

    results = []
    for vtt in sorted(raw_dir.glob('*.vtt')):
        # Try to load metadata
        info_file = vtt.with_suffix('').with_suffix('.info.json')
        meta = {}
        if info_file.exists():
            try:
                with open(info_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                meta = {
                    'title': data.get('title', ''),
                    'channel': data.get('uploader', ''),
                    'date': data.get('upload_date', ''),
                    'duration': data.get('duration_string', ''),
                    'url': data.get('webpage_url', ''),
                    'description': data.get('description', '')[:300],
                    'view_count': data.get('view_count', 0),
                }
            except Exception:
                pass

        text = extract_clean_text(vtt)
        # First 800 words for preview
        words = text.split()
        preview = ' '.join(words[:800])

        results.append({
            'file': vtt.name,
            'meta': meta,
            'preview': preview,
            'word_count': len(words),
        })

    for r in results:
        print(f"\n{'='*60}")
        print(f"FILE: {r['file']}")
        if r['meta']:
            print(f"TITLE: {r['meta'].get('title', 'N/A')}")
            print(f"CHANNEL: {r['meta'].get('channel', 'N/A')}")
            print(f"DATE: {r['meta'].get('date', 'N/A')}")
            print(f"DURATION: {r['meta'].get('duration', 'N/A')}")
            print(f"VIEWS: {r['meta'].get('view_count', 'N/A')}")
            print(f"URL: {r['meta'].get('url', 'N/A')}")
        print(f"WORDS: {r['word_count']}")
        print(f"PREVIEW:\n{r['preview']}")
        print()

if __name__ == '__main__':
    main()
