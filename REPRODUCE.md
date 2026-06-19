# Reproduzir — Cap 3 Seeds

```bash
cd tasks/task12_fase4_cap3
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_pipeline.py
python scripts/harness_check.py
```

## Entrega professor

- Notebook único: `notebooks/seeds_classification_RM571820.ipynb`
- Submissão: portal assign 614329 — **Higor**

## Sem internet

```bash
python scripts/run_pipeline.py --offline
```

Usa dataset sintético compatível (mesma estrutura 7 features + 3 classes).
