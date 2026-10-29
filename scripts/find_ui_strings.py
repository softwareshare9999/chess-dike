#!/usr/bin/env python3
"""Find CJK-bearing string literals (user-facing text) in Kotlin/Java sources.

Distinguishes real string literals from comments so the i18n port targets
only text that actually reaches the screen.
"""
import re
import sys
from pathlib import Path

CJK = re.compile(r'[\u4e00-\u9fff]')
# Kotlin/Java string literal, double-quoted, no newlines, honoring escapes.
LIT = re.compile(r'"((?:[^"\\\n]|\\.)*)"')


def strip_comments(text: str) -> str:
    """Replace comments with spaces, preserving line structure and offsets."""
    out = []
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c == '/' and i + 1 < n and text[i + 1] == '/':
            while i < n and text[i] != '\n':
                out.append(' ')
                i += 1
        elif c == '/' and i + 1 < n and text[i + 1] == '*':
            out.append('  ')
            i += 2
            while i < n and not (text[i] == '*' and i + 1 < n and text[i + 1] == '/'):
                out.append('\n' if text[i] == '\n' else ' ')
                i += 1
            if i < n:
                out.append('  ')
                i += 2
        elif c == '"':
            out.append(c)
            i += 1
            while i < n:
                if text[i] == '\\' and i + 1 < n:
                    out.append(text[i:i + 2])
                    i += 2
                    continue
                out.append(text[i])
                if text[i] == '"':
                    i += 1
                    break
                i += 1
        else:
            out.append(c)
            i += 1
    return ''.join(out)


def scan(path: Path):
    text = path.read_text(encoding='utf-8', errors='replace')
    clean = strip_comments(text)
    # Track line numbers against the comment-stripped text (same offsets).
    results = []
    for m in LIT.finditer(clean):
        body = m.group(1)
        if CJK.search(body):
            line = clean.count('\n', 0, m.start()) + 1
            results.append((line, body))
    return results


def main():
    roots = sys.argv[1:] or ['app/src/main/java']
    total = 0
    for root in roots:
        for path in sorted(Path(root).rglob('*')):
            if path.suffix not in ('.kt', '.java'):
                continue
            hits = scan(path)
            if not hits:
                continue
            print(f'\n=== {path}  ({len(hits)} literals) ===')
            for line, body in hits:
                total += 1
                preview = body if len(body) <= 110 else body[:107] + '...'
                print(f'  {line:>5}: "{preview}"')
    print(f'\nTOTAL user-facing CJK literals: {total}')


if __name__ == '__main__':
    main()
