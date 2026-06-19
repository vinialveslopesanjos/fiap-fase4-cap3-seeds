# Células EDA — colar no notebook (Igor → Humberto)

> Gerado/atualizado por Igor. Humberto integra em `seeds_classification_RM571820.ipynb`.

## Seção 1 — Import e carga

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/seeds.csv")
df.head()
```

## Seção 2 — Estatísticas

```python
df.describe()
df.isna().sum()
```

## Seção 3 — Visualizações

> Usar PNGs de `figures/` ou replotar com seaborn.

## Seção 4 — Pré-processamento

```python
from sklearn.preprocessing import StandardScaler
# Igor documenta se aplicou scaling antes do ML
```

_SUBSTITUIR com células executadas após `python scripts/run_eda.py`._
