# Task 3 · Cleaning Data

## Objective
Took a deliberately messy dataset (Titanic passenger data) and systematically 
cleaned it into an analysis-ready dataset, documenting every decision made.

## Dataset
[Titanic Dataset - Machine Learning from Disaster (Kaggle)](https://www.kaggle.com/datasets/aman9d/titanic-dataset-machine-learning-from-disaster)
— 891 rows, 12 columns of passenger data.

## Tech Stack
Python, pandas, matplotlib, Google Colab

## Data Quality Issues Found
- **Age**: 177 missing values (~20%)
- **Cabin**: 687 missing values (~77%)
- **Embarked**: 2 missing values
- 0 duplicate rows

## Cleaning Decisions
- **Age**: Filled missing values with the median (robust to outliers like infants/elderly passengers)
- **Cabin**: 77% missing was too high to impute reliably — converted to a binary `Has_Cabin` flag instead of guessing values, then dropped the original column
- **Embarked**: Filled 2 missing values with the mode (negligible impact at this scale)
- **Standardization**: Checked Sex, Embarked, and Pclass for inconsistent formatting — all were already clean, no changes needed
- **Outliers**: Detected using IQR method on Fare (116 outliers) and Age (elderly + infant extremes). Both were **retained** rather than removed, since they reflect genuine passenger diversity (fare by class, age extremes relevant to survival patterns), not data errors
- **Data types**: Corrected PassengerId to string (it's an identifier, not a numeric value)

## Before vs. After
| Metric | Before | After |
|---|---|---|
| Total Rows | 891 | 891 |
| Missing Values | 866 | 0 |
| Duplicate Rows | 0 | 0 |
| Columns | 12 | 12 |

## How to Run
1. Open `CleaningData_Titanic.ipynb` in Google Colab
2. Upload `train.csv` (Titanic dataset) when prompted
3. Run all cells
4. Cleaned output saves as `titanic_cleaned.csv`
