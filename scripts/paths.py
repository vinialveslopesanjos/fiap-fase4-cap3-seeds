"""Caminhos do projeto Seeds Cap 3 (task12_fase4_cap3)."""

from pathlib import Path

TASK_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = TASK_ROOT / "scripts"
DATA_DIR = TASK_ROOT / "data"
DOCS_DIR = TASK_ROOT / "docs"
ML_DIR = TASK_ROOT / "ml"
MODELS_DIR = TASK_ROOT / "models"
NOTEBOOKS_DIR = TASK_ROOT / "notebooks"
FIGURES_DIR = TASK_ROOT / "figures"
ENTREGA_DIR = TASK_ROOT / "entrega"

SEEDS_CSV = DATA_DIR / "seeds.csv"
SEEDS_RAW = DATA_DIR / "seeds_dataset.txt"
ML_CLASSIFY = ML_DIR / "classify.py"
BEST_MODEL = MODELS_DIR / "best_classifier.joblib"
METRICS_JSON = MODELS_DIR / "classification_metrics.json"
COMPARISON_CSV = MODELS_DIR / "model_comparison.csv"
NOTEBOOK_FINAL = NOTEBOOKS_DIR / "seeds_classification_RM572814.ipynb"
INSIGHTS_MD = DOCS_DIR / "insights.md"

SEEDS_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00236/seeds_dataset.txt"

FEATURE_COLUMNS = [
    "area",
    "perimeter",
    "compactness",
    "length_kernel",
    "width_kernel",
    "asymmetry",
    "groove_length",
]
TARGET_COLUMN = "variety"
VARIETY_LABELS = {1: "Kama", 2: "Rosa", 3: "Canadian"}
