#!/usr/bin/env python3
"""Pipeline Cap 3 Seeds — download → EDA → classificação."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from paths import TASK_ROOT


def _run(rel: str, label: str) -> None:
    path = TASK_ROOT / rel
    if not path.is_file():
        print(f"ERRO: ausente {rel}", file=sys.stderr)
        sys.exit(1)
    print(f"\n[pipeline] {label}")
    subprocess.run([sys.executable, str(path)], cwd=TASK_ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--skip-eda", action="store_true")
    args = parser.parse_args()

    print("=" * 60)
    print("Seeds Cap 3 — run_pipeline.py")
    print("=" * 60)

    cmd = [sys.executable, str(TASK_ROOT / "scripts/download_seeds.py")]
    if args.offline:
        cmd.append("--offline")
    subprocess.run(cmd, cwd=TASK_ROOT, check=True)

    if not args.skip_eda:
        _run("scripts/run_eda.py", "Etapa 2 — Igor: EDA + figuras")

    _run("ml/classify.py", "Etapa 3 — Higor: classificadores + tuning")

    print("\n[pipeline] Concluído.")
    print("  Humberto: consolidar notebook + docs/insights.md")
    print("  Higor: submeter no portal assign 614329")
    print("  Gates: python scripts/harness_check.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
