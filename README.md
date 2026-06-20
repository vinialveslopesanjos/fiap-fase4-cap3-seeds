# Seeds Cap 3 — IR ALÉM ML (Fase 4)

**Turma 1TIAOA · Entrega individual** · Prazo **19/06/2026 23h59**  
**Aluno:** Vinicius Anjos · RM 572814  
**Portal:** [assign 614329](https://on.fiap.com.br/mod/assign/view.php?id=614329)

---

## Visão geral

Projeto individual desenvolvido para aplicar o processo CRISP-DM no dataset Seeds da UCI. O trabalho contempla download ou geração offline dos dados, análise exploratória, treinamento de modelos de classificação, comparação de métricas e consolidação em notebook final.

Dataset oficial: https://archive.ics.uci.edu/dataset/236/seeds

---

## Setup local

```bash
git clone https://github.com/vinialveslopesanjos/fiap-fase4-cap3-seeds.git
cd fiap-fase4-cap3-seeds
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

No Windows PowerShell:

```powershell
git clone https://github.com/vinialveslopesanjos/fiap-fase4-cap3-seeds.git
cd fiap-fase4-cap3-seeds
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Pipeline completo

```bash
python scripts/run_pipeline.py
python scripts/harness_check.py
```

Sem internet:

```bash
python scripts/run_pipeline.py --offline
python scripts/harness_check.py
```

O modo offline usa um dataset sintético compatível, com a mesma estrutura de 7 features e 3 classes.

---

## O que o projeto entrega

1. Base `data/seeds.csv`.
2. Figuras de EDA em `figures/`.
3. Treinamento de múltiplos classificadores.
4. Comparação de modelos em `models/model_comparison.csv`.
5. Métricas finais em `models/classification_metrics.json`.
6. Modelo salvo em `models/best_classifier.joblib`.
7. Notebook final em `notebooks/seeds_classification_RM572814.ipynb`.
8. Resumo interpretativo em `docs/insights.md`.

---

## Estrutura

```text
fiap-fase4-cap3-seeds/
├── README.md
├── REPRODUCE.md
├── requirements.txt
├── scripts/       # download, EDA, pipeline e harness
├── ml/            # classificação e tuning
├── data/          # seeds.csv
├── figures/       # gráficos gerados pela EDA
├── models/        # modelo e métricas
├── notebooks/     # notebook final de entrega
├── docs/          # insights e células auxiliares
└── entrega/       # checklist de entrega
```

---

## Roteiro sugerido para explicação

1. Apresentar o problema: classificar variedades de trigo a partir de medidas geométricas das sementes.
2. Mostrar o dataset e as 7 variáveis explicativas.
3. Explicar rapidamente a EDA e as figuras geradas.
4. Mostrar os modelos treinados e a comparação de métricas.
5. Abrir o notebook final e destacar o melhor classificador.
6. Concluir com a importância do CRISP-DM para organizar análise, modelagem e avaliação.

---

## Reprodução rápida

Também existe um passo a passo resumido em [`REPRODUCE.md`](REPRODUCE.md).
