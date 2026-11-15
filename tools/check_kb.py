"""Compute a source fingerprint, not proof that an agent reviewed the sources."""
import argparse
import hashlib
import json
from pathlib import Path


def fingerprint(root):
    paths = set()
    for folder in ('knowledge-base', 'codex-prompts'):
        paths.update(p for p in (root / folder).rglob('*') if p.is_file())
    paths.update(p for p in root.iterdir() if p.is_file() and p.suffix.lower() in ('.md', '.docx', '.pdf', '.txt'))
    paths.add(root / 'tools' / 'check_kb.py')
    for required in ('AGENTS.md', 'knowledge-base/index.md', 'knowledge-base/maintenance.md', 'tma-ops-processes.md'):
        if not (root / required).is_file():
            raise FileNotFoundError(required)
    manifest = []
    for path in sorted(paths, key=lambda p: p.relative_to(root).as_posix()):
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError('External or symbolic source requires manual review: ' + str(path))
        manifest.append([path.relative_to(root).as_posix(), hashlib.sha256(path.read_bytes()).hexdigest()])
    return hashlib.sha256(json.dumps(manifest, separators=(',', ':')).encode()).hexdigest(), len(manifest)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--expect', help='Fingerprint of a review retained in this conversation')
    args = parser.parse_args()
    try:
        digest, count = fingerprint(Path(__file__).resolve().parents[1])
        print(json.dumps({'fingerprint': digest, 'files': count,
                          'state': 'unchanged' if args.expect == digest else 'review-required'}))
    except (OSError, ValueError) as error:
        print(json.dumps({'state': 'check-failed', 'error': str(error)}))
        raise SystemExit(1)
