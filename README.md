# Seeds Cap 3 — IR ALÉM ML (Fase 4)

**Turma 1TIAOA · Grupo 32** · Prazo **19/06/2026 23h59**  
**Portal:** [assign 614329](https://on.fiap.com.br/mod/assign/view.php?id=614329)

| Integrante | RM | Branch | Parte |
|------------|-----|--------|-------|
| Vinicius Anjos | 572814 | `f4-cap3-vinicius-integracao` | Revisão final + gravação/explicação |
| Higor Henrique Garcia | 571820 | `f4-cap3-higor-ml` | ML + **portal** |
| Igor | 572822 | `f4-cap3-igor-eda` | EDA + figuras |
| Humberto | 570536 | `f4-cap3-humberto-notebook` | Notebook + `insights.md` |

**Harness:** [`specs/task12_fase4_cap3/HARNESS_GRUPO.md`](../../specs/task12_fase4_cap3/HARNESS_GRUPO.md)

---

## Setup

```bash
cd tasks/task12_fase4_cap3
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Pipeline completo

```bash
python scripts/run_pipeline.py        # download → EDA → ML
python scripts/harness_check.py       # gates por papel
```

Offline (sem rede): `python scripts/run_pipeline.py --offline`

---

## Por integrante

### Igor — `f4-cap3-igor-eda`

```bash
python scripts/download_seeds.py
python scripts/run_eda.py
python scripts/harness_check.py --role igor
```

Saída: `figures/*.png` + stats no terminal

### Higor — `f4-cap3-higor-ml`

```bash
python ml/classify.py
python scripts/harness_check.py --role higor
```

Saída: `models/best_classifier.joblib`, `model_comparison.csv`, `classification_metrics.json`

### Humberto — `f4-cap3-humberto-notebook`

1. Consolidar `notebooks/seeds_classification_RM571820.ipynb`
2. Preencher `docs/insights.md`
3. `python scripts/harness_check.py --role humberto`
4. Avisar **Higor** quando notebook estiver pronto para portal

### Higor — portal

- Submeter assign 614329 com notebook + artefatos

---

## Estrutura

```
task12_fase4_cap3/
├── scripts/       download, EDA, pipeline, harness
├── ml/            classify.py
├── data/          seeds.csv (gerado)
├── figures/       Igor
├── models/        Higor
├── notebooks/     Humberto — entrega .ipynb
├── docs/insights.md
└── entrega/
```

Dataset oficial: https://archive.ics.uci.edu/dataset/236/seeds
