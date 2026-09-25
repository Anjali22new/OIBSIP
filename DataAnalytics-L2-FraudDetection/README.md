# Credit Card Fraud Detection

## Overview
This project builds a fraud classification model and demonstrates why accuracy is a poor 
metric on severely imbalanced data (0.17% fraud rate). Three modeling approaches are 
compared to find one with a deployable precision-recall tradeoff.

## Dataset
- **Source:** [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud) (ULB Machine Learning Group)
- **Size:** 284,807 transactions, 492 fraudulent (0.17%)
- **Features:** V1–V28 (PCA-anonymized), Time, Amount, Class (target)

## Methodology
1. Stratified train/test split (preserves the 0.17% fraud ratio in both sets)
2. **Baseline:** Logistic Regression on raw imbalanced data
3. **Class-weighted:** `class_weight='balanced'` to penalize minority-class errors more heavily
4. **Threshold tuning:** Precision-recall curve analysis to find a balanced decision threshold, rather than the default 0.5 cutoff

## Results

| Approach | Recall | Precision | F1 | False Alarms |
|---|---|---|---|---|
| Baseline | 0.64 | 0.83 | 0.72 | 13 |
| Class-weighted (default threshold) | 0.92 | 0.06 | 0.11 | 1,389 |
| **Class-weighted + tuned threshold** | **0.82** | **0.82** | **0.82** | **18** |

## Key Finding
The baseline model achieved 99.9% accuracy while missing over a third of actual fraud cases — 
a textbook example of why accuracy is misleading on imbalanced data. Class-weighting alone 
fixed recall but created an unworkable 1,389 false alarms. Tuning the decision threshold 
(rather than relying on the default 0.5 cutoff) found a deployable middle ground: 82% fraud 
recall at only 18 false alarms.

## Visuals
- `fraud_model_comparison.png` — performance comparison across all three approaches + final confusion matrix
- `precision_recall_curve.png` — precision-recall tradeoff across all thresholds

## Tools
Python, pandas, scikit-learn (LogisticRegression, StandardScaler, precision_recall_curve), matplotlib, seaborn — Google Colab
