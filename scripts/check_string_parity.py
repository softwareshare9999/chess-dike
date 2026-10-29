#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify string-resource parity and that every @string/ reference resolves."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / 'app/src/main/res'

NAME = re.compile(r'<string\s+name="([^"]+)"')
REF = re.compile(r'@string/([A-Za-z0-9_]+)')


def names(path: Path):
    if not path.exists():
        return None
    return set(NAME.findall(path.read_text(encoding='utf-8')))


def main():
    default = names(RES / 'values/strings.xml') or set()
    zh = names(RES / 'values-zh-rCN/strings.xml') or set()
    legacy_zh = names(RES / 'values-zh/strings.xml') or set()

    ok = True

    missing_zh = default - zh
    extra_zh = zh - default
    if missing_zh:
        ok = False
        print(f'[FAIL] missing in values-zh-rCN: {sorted(missing_zh)}')
    if extra_zh:
        ok = False
        print(f'[FAIL] extra in values-zh-rCN: {sorted(extra_zh)}')
    if not missing_zh and not extra_zh:
        print(f'[ok] values/ and values-zh-rCN/ have identical keys ({len(default)} strings)')

    if legacy_zh:
        print(f'[info] values-zh/ also present with {len(legacy_zh)} strings '
              f'(duplicate of zh-rCN; Android prefers zh-rCN)')

    # every @string/ reference in layouts/xml must exist in the default set
    refs = set()
    unresolved = []
    for p in RES.rglob('*.xml'):
        if p.name == 'strings.xml':
            continue
        for m in REF.finditer(p.read_text(encoding='utf-8')):
            refs.add(m.group(1))
    for name in sorted(refs - default):
        ok = False
        unresolved.append(name)
    if unresolved:
        print(f'[FAIL] unresolved @string refs: {unresolved}')
    else:
        print(f'[ok] all {len(refs)} @string/ references in res/ resolve')

    # R.string.<name> references in Kotlin/Java
    code_refs = set()
    for p in (ROOT / 'app/src/main/java').rglob('*'):
        if p.suffix in ('.kt', '.java'):
            for m in re.finditer(r'R\.string\.([A-Za-z0-9_]+)', p.read_text(encoding='utf-8', errors='replace')):
                code_refs.add(m.group(1))
    bad_code = sorted(code_refs - default)
    if bad_code:
        ok = False
        print(f'[FAIL] unresolved R.string refs in code: {bad_code}')
    else:
        print(f'[ok] all {len(code_refs)} R.string references in code resolve')

    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
