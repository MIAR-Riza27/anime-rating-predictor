---
# Anime Score Prediction

A machine learning project to predict anime scores based on metadata like type, source, status, rating, season, genres, and more.

---
## Project Structure
```bash
├── .venv/                     # Virtual environment
├── .vscode/                   # VSCode config
├── data/
│   └── processed/
│       └── clean_anime_full.csv   # Cleaned dataset
│   └── raw/
│       └── top_anime_all.json     # Raw dataset
├── models/
│   └── best_random_forest_model.pkl   # Saved model
├── notebooks/
│   ├── 01-eda.ipynb           # Exploratory Data Analysis
│   └── 02-modeling.ipynb      # Feature engineering + Model training
├── src/
│   ├── data_loader.py         # Dataset loading functions
│   └── preprocessing.py       # Preprocessing utilities
├── tests/                     # (Optional) Unit tests
├── .gitignore
├── LICENSE
├── main.py                    # (Optional) Script for running full pipeline
├── README.md
├── requirements.txt
```

---
## Objective

This project aims to:

- Predict anime `score` using regression models.
- Compare baseline models like Linear Regression and Random Forest.
- Evaluate models with metrics: MAE, RMSE, and R².
- Avoid data leakage by removing leakage-prone features like `scored_by`.
- Tune and validate the best model with cross-validation.

---

## Models and Results

| Model                     | MAE    | RMSE   | R²     |
|--------------------------|--------|--------|--------|
| Linear Regression        | 1.5734 | 2.1717 | 0.6375 |
| Random Forest (leakage)  | 0.0549 | 0.1844 | 0.9974 |
| Random Forest (no leak)  | 0.1120 | 0.5235 | 0.9789 |
| Tuned RF + CV (no leak)  |   —    |   —    | **~0.9807 ± 0.0026** |

**Best model:** Tuned Random Forest (with `scored_by` removed)  
Validated with 5-fold cross-validation, achieving **R² ≈ 0.9807 ± 0.0026**

---
## Preprocessing

- Removed unused columns: `title`, `favorites`, `has_year`, `has_season`
- Encoded categorical columns using `OrdinalEncoder`
- Imputed missing values (`mean` for numeric, `most_frequent` for categorical)
- Scaled numeric features using `StandardScaler`

---
## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/MIAR-Riza27/anime-rating-predictor.git
    cd anime-rating-predictor
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the notebook:
    - You can start with the exploratory analysis:
        ```bash
        jupyter notebook notebooks/01-eda.ipynb
        ```

    - Then proceed to model training:
        ```bash
        jupyter notebook notebooks/02-modeling.ipynb
        ```

---
## Notes

> The dataset comes from MyAnimeList and has been pre-cleaned in a separate step.
> No leakage was allowed in the final model selection (e.g. scored_by removed).

---
## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
You are free to **use, modify, and distribute** this project for personal or commercial purposes, with **proper attribution**.
