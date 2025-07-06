---
# Anime Score Prediction

A machine learning project to predict anime scores based on metadata like type, source, status, rating, season, genres, and more.

---
## Project Structure
```
├── data
│ └── processed
│ └── clean_anime_full.csv # Cleaned dataset
├── notebooks
│ └── predict_anime_scores.ipynb # Main notebook
├── models
│ └── [Optional: save model here]
├── README.md
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
| Linear Regression        | ~0.42  | ~0.56  | ~0.75  |
| Random Forest (leakage)  | ~0.12  | ~0.19  | ~0.98  |
| Random Forest (no leak)  | ~0.26  | ~0.36  | ~0.93  |
| Tuned RF + CV (no leak)  |   —    |   —    | **~0.9807 ± 0.0026** |

Best model: Tuned Random Forest (without `scored_by`, Best until now)
Validated with 5-fold cross-validation

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
    ```bash
    notebooks/predict_anime_scores.ipynb
    ```

---
## Notes

> The dataset comes from MyAnimeList and has been pre-cleaned in a separate step.
> No leakage was allowed in the final model selection (e.g. scored_by removed).

---
## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
You are free to **use, modify, and distribute** this project for personal or commercial purposes, with **proper attribution**.
