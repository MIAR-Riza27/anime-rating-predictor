---
# Anime Score Prediction

A machine learning project to predict anime scores based on metadata like type, source, status, rating, season, genres, and more.

---
## Project Structure
```bash
├── .venv/                     # Virtual environment
│   └── ...
├── .vscode/                   # VSCode config
│   └── ...
├── data/
│   └── interim/                   # Intermediate dataset
│       └── ...
│   └── processed/
│       └── clean_anime_full.csv   # Cleaned dataset
│   └── raw/
│       └── top_anime_all.json     # Raw dataset
├── models/
│   └── final_model.pkl        # Saved model
├── notebooks/
│   ├── 01-eda.ipynb                      # Exploratory Data Analysis
│   ├── 02-features_engineering.ipynb     # Feature engineering
│   ├── 03-model_training.ipynb           # Model training
│   ├── 04-no_leakage_model.ipynb         # Model evaluation for no leakage
│   ├── 05-model_tuning.ipynb             # Hyperparameter tuning
│   └── 06-cross_validation.ipynb         # Cross-validation
├── src/
│   └── __pycache__/
│      └── ...
│   ├── data_loader.py
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
    ### Step-by-Step Instructions for Running the Notebooks
    You can run the notebooks sequentially by following these steps:

    * Run the `01-eda.ipynb` notebook for exploratory data analysis:
        ```bash
        jupyter notebook notebooks/01-eda.ipynb
        ```
    * Run the `02-feature_engineering.ipynb` notebook for feature engineering:
        ```bash
        jupyter notebook notebooks/02-feature_engineering.ipynb
        ```
    * Run the `03-model_training.ipynb` notebook for model training:
        ```bash
        jupyter notebook notebooks/03-model_training.ipynb
        ```
    * Run the `04-no_leakage_model.ipynb` notebook for model evaluation without leakage:
        ```bash
        jupyter notebook notebooks/04-no_leakage_model.ipynb
        ```
    * Run the `05-model_tuning.ipynb` notebook for hyperparameter tuning:
        ```bash
        jupyter notebook notebooks/05-model_tuning.ipynb
        ```
    * Run the `06-cross_validation.ipynb` notebook for cross-validation:
        ```bash
        jupyter notebook notebooks/06-cross_validation.ipynb
        ```

---
## Notes

> The dataset comes from MyAnimeList and has been pre-cleaned in a separate step.
> No leakage was allowed in the final model selection (e.g. scored_by removed).

---
## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
You are free to **use, modify, and distribute** this project for personal or commercial purposes, with **proper attribution**.

---