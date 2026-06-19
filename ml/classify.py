#!/usr/bin/env python3
"""Classificação Seeds — CRISP-DM tarefas 2–3 (Higor)."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

import sys

TASK_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TASK_ROOT / "scripts"))
from paths import (  # noqa: E402
    BEST_MODEL,
    COMPARISON_CSV,
    FEATURE_COLUMNS,
    METRICS_JSON,
    MODELS_DIR,
    SEEDS_CSV,
    TARGET_COLUMN,
    VARIETY_LABELS,
)


def _eval_model(name: str, model, X_test, y_test) -> dict:
    preds = model.predict(X_test)
    return {
        "model": name,
        "accuracy": round(float(accuracy_score(y_test, preds)), 4),
        "precision": round(float(precision_score(y_test, preds, average="weighted")), 4),
        "recall": round(float(recall_score(y_test, preds, average="weighted")), 4),
        "f1": round(float(f1_score(y_test, preds, average="weighted")), 4),
    }


def train_and_compare(csv_path: Path = SEEDS_CSV) -> dict:
    if not csv_path.is_file():
        raise FileNotFoundError(f"Dataset ausente: {csv_path}. Rode download_seeds.py")

    df = pd.read_csv(csv_path)
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    candidates = {
        "knn": KNeighborsClassifier(),
        "svm": SVC(kernel="rbf"),
        "random_forest": RandomForestClassifier(random_state=42),
        "naive_bayes": GaussianNB(),
        "logistic_regression": LogisticRegression(max_iter=2000, random_state=42),
    }

    rows = []
    fitted = {}
    for name, estimator in candidates.items():
        pipe = Pipeline([("scaler", StandardScaler()), ("clf", estimator)])
        pipe.fit(X_train, y_train)
        fitted[name] = pipe
        rows.append(_eval_model(name, pipe, X_test, y_test))

    comparison = pd.DataFrame(rows).sort_values("f1", ascending=False)
    best_name = comparison.iloc[0]["model"]
    best_pipe = fitted[best_name]

    tuned_metrics = None
    grid = None
    if best_name == "knn":
        grid = GridSearchCV(best_pipe, {"clf__n_neighbors": [3, 5, 7, 11]}, cv=3)
    elif best_name == "svm":
        grid = GridSearchCV(best_pipe, {"clf__C": [0.5, 1, 2, 4]}, cv=3)
    elif best_name == "random_forest":
        grid = GridSearchCV(best_pipe, {"clf__n_estimators": [80, 120, 200]}, cv=3)

    if grid is not None:
        grid.fit(X_train, y_train)
        best_pipe = grid.best_estimator_
        tuned_metrics = _eval_model(f"{best_name}_tuned", best_pipe, X_test, y_test)

    preds = best_pipe.predict(X_test)
    report = classification_report(
        y_test, preds, target_names=[VARIETY_LABELS[i] for i in sorted(VARIETY_LABELS)]
    )
    cm = confusion_matrix(y_test, preds).tolist()

    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(best_pipe, BEST_MODEL)
    comparison.to_csv(COMPARISON_CSV, index=False)

    payload = {
        "trained_at": datetime.now(timezone.utc).isoformat(),
        "best_model": best_name,
        "comparison": rows,
        "tuned": tuned_metrics,
        "classification_report": report,
        "confusion_matrix": cm,
    }
    METRICS_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, default=SEEDS_CSV)
    args = parser.parse_args()
    train_and_compare(args.csv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
