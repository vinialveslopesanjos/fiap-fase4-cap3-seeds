# Notebooks — Cap 3 Seeds

## Fluxo individual

O notebook final consolida EDA, modelagem, avaliação e interpretação dos resultados em um único arquivo:

`notebooks/seeds_classification_RM572814.ipynb`

## Seções sugeridas

1. Introdução + download/carregamento do dataset (`data/seeds.csv`)
2. EDA: estatísticas, histogramas, boxplots e scatter plots
3. Preparação dos dados e divisão treino/teste
4. Modelos de classificação, com pelo menos 3 algoritmos
5. Grid Search e comparação antes/depois
6. Matriz de confusão e métricas finais
7. Interpretação dos resultados e conclusão

## Atalho Colab

```python
# Célula 1 — após upload do seeds.csv
import pandas as pd

df = pd.read_csv("seeds.csv")
df.head()
```

## Gate do notebook

```bash
test -f notebooks/seeds_classification_RM572814.ipynb && echo OK
python scripts/harness_check.py
```
