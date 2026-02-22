# Skill: Data Management & Analysis

**Domain:** Data Science & Intelligence
**Primary Language:** Python
**Status:** Active

---

## Overview

KENDRAH can ingest, process, transform, analyze, and visualize data from virtually any source. It applies data science principles and machine learning where appropriate to surface insights, generate predictions, and support strategic decision-making.

---

## Capabilities

### Data Ingestion & Parsing
- Load data from files: CSV, Excel, JSON, XML, Parquet, HDF5, SQLite databases.
- Connect to live databases: PostgreSQL, MySQL, MongoDB, Redis.
- Consume data from REST APIs, webhooks, and streaming sources.
- Handle messy or inconsistent data with intelligent cleaning and normalization routines.

### Data Transformation & Processing
- Filter, sort, group, merge, pivot, and reshape datasets.
- Apply formula-based transformations across rows and columns.
- Handle missing data: impute, drop, flag, or interpolate as appropriate.
- Normalize, standardize, and encode data for ML or reporting pipelines.

### Statistical Analysis
- Compute descriptive statistics: mean, median, mode, variance, standard deviation, percentiles.
- Perform correlation and regression analysis.
- Run hypothesis tests and significance testing.
- Generate distribution plots and statistical summaries.

### Predictive Modeling
- Build and train machine learning models using scikit-learn, TensorFlow, or PyTorch.
- Perform supervised learning: regression, classification.
- Perform unsupervised learning: clustering, dimensionality reduction.
- Run AI simulations to predict future outcomes and scenarios.

### Data Visualization
- Generate charts and graphs: line, bar, scatter, heatmap, pie, histogram, box plot.
- Build interactive dashboards using Plotly or Dash.
- Export visualizations as PNG, SVG, HTML, or PDF.

### Reporting
- Compile analysis results into structured reports (Markdown, HTML, PDF).
- Schedule automated data reports on a recurring basis.
- Deliver reports via email, file output, or integrated communication systems.

---

## Tools & Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn import *         # scikit-learn
import tensorflow as tf
import torch
import sqlalchemy
import openpyxl
import scipy
```

---

## Example Tasks

- "Kendrah, load the sales CSV and show me the top 10 products by revenue."
- "Kendrah, predict next month's user growth based on the last 12 months of data."
- "Kendrah, generate a heatmap of correlation between all columns in this dataset."
- "Kendrah, clean this dataset — remove duplicates and fill missing values in the `age` column with the median."
- "Kendrah, produce a weekly automated sales report and save it as a PDF."
