# Task 4: Sentiment Analysis — Amazon Fine Food Reviews

## Overview
This project evaluates how well **VADER**, a lexicon-based sentiment analysis tool, predicts 
customer sentiment compared to actual star ratings on Amazon food reviews. Rather than just 
running a sentiment model and reporting scores, the goal was to identify *where and why* the 
model's predictions diverge from real customer sentiment — and what that reveals about the 
limits of word-level sentiment scoring.

## Dataset
- **Source:** [Amazon Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews) (Stanford SNAP)
- **Size:** 568,454 reviews; a random sample of 15,000 (seed=42) was used for sentiment scoring
- **Key columns used:** `Score` (1–5 star rating), `Text` (review body)

## Methodology
1. **Ground truth label:** Star ratings mapped to sentiment — 1–2★ = negative, 3★ = neutral, 4–5★ = positive
2. **Predicted label:** VADER's compound score run on raw, unprocessed review text (VADER is designed for natural text and doesn't require preprocessing)
3. **Evaluation:** Confusion matrix, precision/recall/F1 per class, and manual inspection of mismatched cases

## Results

| Class    | Precision | Recall | F1   |
|----------|-----------|--------|------|
| Negative | 0.60      | 0.41   | 0.49 |
| Neutral  | 0.13      | 0.03   | 0.05 |
| Positive | 0.84      | 0.95   | 0.90 |

**Overall accuracy: 81%** — but this is misleading, driven almost entirely by the majority positive class.

## Key Finding
VADER systematically misclassifies negative reviews that **open with praise before delivering 
a negative verdict**. Of 15,000 reviews, 1,170 genuinely negative (1–2★) reviews were scored 
positive. Manual review of these cases showed a consistent pattern: reviewers often compliment 
a specific aspect (aroma, packaging, brand reputation) before their actual complaint — since 
VADER aggregates polarity across the full text, a short negative conclusion gets outweighed by 
a longer positive build-up. This is a structural limitation of lexicon-based, word-level 
scoring, not a data quality issue.

## Business Implication
For use cases requiring accurate negative-sentiment flagging (e.g., escalating customer 
complaints), VADER alone would miss ~6 in 10 genuinely negative reviews — a meaningful 
blind spot for any team relying on it for triage.

## Visuals
- `sentiment_comparison.png` — sentiment distribution + confusion matrix
- `wordclouds.png` — most common words in positive vs. negative reviews

## Tools
Python, pandas, VADER (vaderSentiment), scikit-learn, matplotlib, seaborn, wordcloud — Google Colab
