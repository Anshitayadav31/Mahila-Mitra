
# Mahila-Mitra

Mahila-Mitra is an educational research project exploring AI methods and datasets related to polycystic ovary syndrome (PCOS), including clinical data analysis and ovarian ultrasound research.

## Objectives

- Study three existing datasets and their associated research papers.
- Reproduce documented preprocessing and feature-extraction methods where the data and documentation permit.
- Evaluate selected machine-learning methods using appropriate experimental procedures.
- Compare project-generated results with published findings while clearly distinguishing their sources.
- Investigate how research findings could inform a future health-support platform.

## Current Progress

### Clinical/tabular data analysis

- Loaded and inspected the clinical PCOS dataset.
- Created a cleaning script and a cleaned dataset for analysis.
- Performed exploratory data analysis and generated visualizations.
- Compared two Random Forest feature sets: clinical/symptom features and all available predictors.
- Evaluated the models using a held-out test set and five-fold cross-validation.
- Examined confusion matrices, prediction errors, and feature importance.
- Saved the experimental model and analysis outputs locally.

The current experiments use a dataset containing 541 records. The reported test-set results are preliminary and have not been externally validated.

## Project Structure

- `configs/` — configuration files
- `data/` — dataset storage
- `notebooks/` — exploratory analysis and experiments
- `outputs/` — generated plots, metrics, and local model artifacts
- `reports/` — research summaries and analysis documentation
- `scripts/` — data-processing scripts
- `src/` — application and reusable source code
- `tests/` — project tests
- `requirements.txt` — Python dependencies

## Setup

Use Python 3.11 in a virtual environment.

```bash
python -m venv .venv
```

Activate the environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Open the notebooks using VS Code or Jupyter and select the project's virtual-environment kernel.

## Reproducibility

- The clinical cleaning script is located at `scripts/clean_clinical.py`.
- The exploratory analysis and experiments are documented in `notebooks/clinical_eda.ipynb`.
- Dataset and experiment details are documented in `reports/clinical_pipeline.md`.
- The research-paper summary is documented in `reports/clinical_paper_summary.md`.

The original datasets must be obtained from their respective sources and placed in the expected local data directories. Raw datasets, processed data, and generated model artifacts are intended to remain outside version control.

## Research Integrity and Limitations

This project is for educational and research purposes, not clinical diagnosis.

Experimental metrics reflect the available dataset and evaluation design. They do not establish clinical validity or generalizability. Potential label-definition overlap, dataset size, data quality, and the need for independent external validation must be considered when interpreting results.

Published results will be distinguished from results obtained in this project.
