#!/usr/bin/env python3
"""Baixa Seeds UCI ou gera fallback reproduzível offline."""

from __future__ import annotations

import argparse
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd

from paths import FEATURE_COLUMNS, SEEDS_CSV, SEEDS_RAW, SEEDS_URL, TARGET_COLUMN, TASK_ROOT


def _generate_fallback(rows_per_class: int = 70, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    frames = []
    for variety in (1, 2, 3):
        base = 15 + variety * 2
        frames.append(
            pd.DataFrame(
                {
                    "area": rng.normal(base + 10, 2, rows_per_class),
                    "perimeter": rng.normal(base + 5, 1.5, rows_per_class),
                    "compactness": rng.normal(0.85 + variety * 0.02, 0.03, rows_per_class),
                    "length_kernel": rng.normal(base, 0.8, rows_per_class),
                    "width_kernel": rng.normal(base - 2, 0.6, rows_per_class),
                    "asymmetry": rng.normal(2.5 + variety * 0.3, 0.5, rows_per_class),
                    "groove_length": rng.normal(base - 1, 0.7, rows_per_class),
                    TARGET_COLUMN: variety,
                }
            )
        )
    return pd.concat(frames, ignore_index=True)


def download_raw(dest: Path = SEEDS_RAW) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        urllib.request.urlretrieve(SEEDS_URL, dest)  # noqa: S310
        print(f"[ok] download UCI → {dest.relative_to(TASK_ROOT)}")
        return dest
    except Exception as exc:
        print(f"[aviso] download falhou ({exc}); usando fallback sintético")
        return dest


def raw_to_csv(raw_path: Path, csv_path: Path = SEEDS_CSV) -> pd.DataFrame:
    if raw_path.is_file() and raw_path.stat().st_size > 100:
        df = pd.read_csv(raw_path, sep=r"\s+", header=None, names=FEATURE_COLUMNS + [TARGET_COLUMN])
    else:
        df = _generate_fallback()
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_path, index=False)
    print(f"[ok] {len(df)} linhas → {csv_path.relative_to(TASK_ROOT)}")
    return df


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true", help="pular download, só fallback")
    args = parser.parse_args()

    if args.offline:
        raw_to_csv(SEEDS_RAW)  # força fallback
    else:
        raw = download_raw()
        if not raw.is_file() or raw.stat().st_size < 100:
            raw_to_csv(SEEDS_RAW)
        else:
            raw_to_csv(raw)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
