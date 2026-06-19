#!/usr/bin/env python3
"""Gates harness Cap 3 Seeds."""

from __future__ import annotations

import json
import sys
from pathlib import Path

TASK_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TASK_ROOT / "scripts"))
from paths import (  # noqa: E402
    BEST_MODEL,
    COMPARISON_CSV,
    FIGURES_DIR,
    INSIGHTS_MD,
    METRICS_JSON,
    NOTEBOOK_FINAL,
    SEEDS_CSV,
)


def gate(name: str, ok: bool, detail: str = "") -> bool:
    print(f"  [{'OK' if ok else 'FALHA'}] {name}" + (f" — {detail}" if detail else ""))
    return ok


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--role", choices=["higor", "igor", "humberto", "all"], default="all")
    args = parser.parse_args()
    ok = True
    print("Harness Cap 3 — gates\n")

    if args.role in ("all", "igor"):
        print("Igor (EDA):")
        ok &= gate("G1 seeds.csv", SEEDS_CSV.is_file())
        fig_count = len(list(FIGURES_DIR.glob("*.png"))) if FIGURES_DIR.is_dir() else 0
        ok &= gate("G2 figures/", fig_count >= 3, f"{fig_count} PNGs (meta ≥3)")
        eda_doc = TASK_ROOT / "docs" / "eda_cells.md"
        ok &= gate("G3 eda_cells.md", eda_doc.is_file(), "células para Humberto")

    if args.role in ("all", "higor"):
        print("\nHigor (ML + portal):")
        ok &= gate("G3 best model", BEST_MODEL.is_file())
        ok &= gate("G4 comparison CSV", COMPARISON_CSV.is_file())
        if METRICS_JSON.is_file():
            data = json.loads(METRICS_JSON.read_text(encoding="utf-8"))
            ok &= gate("G5 métricas", "best_model" in data, data.get("best_model", ""))
        else:
            ok &= gate("G5 métricas", False)
        ok &= gate("G8 checklist portal", (TASK_ROOT / "entrega" / "CHECKLIST_PORTAL.md").is_file())

    if args.role in ("all", "humberto"):
        print("\nHumberto (notebook):")
        ok &= gate("G6 insights.md", INSIGHTS_MD.is_file())
        ok &= gate("G7 notebook final", NOTEBOOK_FINAL.is_file(), "consolidar .ipynb")
        ok &= gate("G9 crisp_dm_resumo", (TASK_ROOT / "docs" / "crisp_dm_resumo.md").is_file())

    print()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
