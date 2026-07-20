# 🛡️ YouTube Trust & Safety Analytics Pipeline

An end-to-end analytics and AI moderation project inspired by real-world Trust & Safety workflows used by platforms like YouTube.

This project combines SQL, Python, Power BI, and Large Language Models (LLMs) to analyze YouTube comments, identify spam behavior, visualize moderation insights, and generate AI-assisted moderation decisions.

---

## Project Overview

The goal of this project is to simulate the workflow of a Trust & Safety Engineering Analyst.

The pipeline:

Raw Dataset
↓
PostgreSQL Database
↓
SQL Investigation
↓
Python Analysis
↓
Power BI Dashboard
↓
LLM Moderation Assistant

---

## Tech Stack

- PostgreSQL
- SQL
- Python
- Pandas
- Scikit-learn
- Power BI
- Groq API
- Llama 3.3 70B
- OpenAI SDK

---

## Dataset

YouTube Spam Collection Dataset

Features:

- comment_id
- author
- content
- video_name
- class

Target:

- 0 → Legitimate
- 1 → Spam

---

## SQL Analysis

Performed exploratory investigations including:

- Spam vs Legitimate distribution
- Most targeted videos
- Repeat spam authors
- Duplicate comments
- Longest spam comments
- Spam keyword frequency
- High-risk authors
- High-risk comments

Created reusable SQL Views for investigation.

---

## Python Analysis

Performed:

- Missing value analysis
- Comment length analysis
- Spam keyword extraction
- Data cleaning
- Feature engineering
- Exploratory Data Analysis

---

## Power BI Dashboard

Interactive dashboard including:

- Total Comments
- Spam Comments
- Legitimate Comments
- Spam Rate
- Spam Distribution
- Spam by Video
- Top Spam Authors
- Average Comment Length
- Video Filter
- Comment Type Filter
- Analyst Insights

---

## LLM Moderation Assistant

Built an AI-powered moderation assistant using Llama 3.3 via the Groq API.

The assistant reviews YouTube comments and returns:

- Classification
- Confidence
- Reason
- Recommended Action

Example:

Input:

Subscribe to my channel!!

Output:

Classification: Spam

Confidence: High

Reason:

- Promotional language
- External redirection
- Common spam pattern

Recommended Action:

Remove

---

## Evaluation

Compared LLM predictions against the dataset labels.

Calculated:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Folder Structure

project/

├── data/

├── sql/

├── notebooks/

├── dashboard/

├── llm/

├── outputs/

└── README.md

---

## Dashboard Preview

(Add screenshot here)

---

## Future Improvements

- Fine-tuned spam classifier
- Hybrid LLM + ML moderation
- RAG for moderation policy lookup
- Streamlit moderation application
- Real-time comment monitoring

---

## Author

Sayanteka Saha
