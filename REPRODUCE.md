# Reproduzir — Cap 3 Seeds

## Pré-requisitos

- Python 3.10 ou superior
- Git
- Navegador atualizado, caso queira abrir o notebook localmente

## Linux/macOS

```bash
git clone https://github.com/vinialveslopesanjos/fiap-fase4-cap3-seeds.git
cd fiap-fase4-cap3-seeds
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python scripts/run_pipeline.py
python scripts/harness_check.py
jupyter notebook notebooks/seeds_classification_RM572814.ipynb
```

## Windows PowerShell

```powershell
git clone https://github.com/vinialveslopesanjos/fiap-fase4-cap3-seeds.git
cd fiap-fase4-cap3-seeds
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

python scripts/run_pipeline.py
python scripts/harness_check.py
jupyter notebook notebooks/seeds_classification_RM572814.ipynb
```

## Entrega professor

- Notebook único: `notebooks/seeds_classification_RM572814.ipynb`
- Submissão: portal assign 614329

## Sem internet

```bash
python scripts/run_pipeline.py --offline
python scripts/harness_check.py
```

Usa dataset sintético compatível, com a mesma estrutura de 7 features e 3 classes.
