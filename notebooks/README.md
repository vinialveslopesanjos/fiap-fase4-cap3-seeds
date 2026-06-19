# Notebooks — Cap 3 Seeds

## Fluxo do grupo

1. **Igor** — EDA via `python scripts/run_eda.py` (gera `figures/`) ou células iniciais aqui
2. **Higor** — ML via `python ml/classify.py` (métricas em `models/`)
3. **Humberto** — consolida tudo em **um** arquivo; **Higor** submete no portal

   `notebooks/seeds_classification_RM571820.ipynb`

## Template sugerido (seções)

1. Introdução + download dataset (`data/seeds.csv`)
2. EDA (stats, histogramas, boxplots, scatter) — pode embutir `figures/`
3. Modelos (≥3) + matriz de confusão
4. Grid Search + comparação antes/depois
5. Interpretação — copiar de `docs/insights.md`

## Atalho Colab

```python
# Célula 1 — após upload do seeds.csv
import pandas as pd
df = pd.read_csv("seeds.csv")
df.head()
```

## Gate Humberto

```bash
test -f notebooks/seeds_classification_RM571820.ipynb && echo OK
python scripts/harness_check.py --role humberto
```
