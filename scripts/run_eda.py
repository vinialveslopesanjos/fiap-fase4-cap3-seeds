#!/usr/bin/env python3
"""EDA Seeds — gera figuras sem notebook pesado."""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

TASK_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TASK_ROOT / "scripts"))
from paths import FEATURE_COLUMNS, FIGURES_DIR, SEEDS_CSV, TARGET_COLUMN, VARIETY_LABELS  # noqa: E402


def run_eda(csv_path: Path = SEEDS_CSV) -> None:
    if not csv_path.is_file():
        raise FileNotFoundError("Rode: python scripts/download_seeds.py")

    df = pd.read_csv(csv_path)
    df["variety_name"] = df[TARGET_COLUMN].map(VARIETY_LABELS)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    print(df.describe())
    print("Missing:", df.isna().sum().sum())

    for col in FEATURE_COLUMNS:
        plt.figure(figsize=(6, 4))
        sns.histplot(data=df, x=col, hue="variety_name", kde=True)
        plt.title(f"Distribuição — {col}")
        plt.tight_layout()
        out = FIGURES_DIR / f"hist_{col}.png"
        plt.savefig(out, dpi=120)
        plt.close()
        print(f"[ok] {out.relative_to(TASK_ROOT)}")

    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x="variety_name", y="area")
    plt.title("Boxplot área por variedade")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "boxplot_area.png", dpi=120)
    plt.close()

    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="area", y="perimeter", hue="variety_name")
    plt.title("Scatter área vs perímetro")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "scatter_area_perimeter.png", dpi=120)
    plt.close()

    print(f"[ok] EDA salva em {FIGURES_DIR.relative_to(TASK_ROOT)}/")


def main() -> int:
    run_eda()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
