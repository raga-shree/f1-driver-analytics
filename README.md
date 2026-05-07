# Formula 1 Driver Performance Analytics and Ranking System

## Overview

This project analyzes historical Formula 1 race data to evaluate driver performance using data analytics, machine learning, and visualization techniques.

The system:
- cleans and processes raw Formula 1 datasets,
- calculates driver performance metrics,
- ranks drivers based on efficiency and consistency,
- generates visual insights using graphs and charts.

The project also demonstrates collaborative software development using Git and GitHub.

---

# Team Members

1. Ragashree R  
2. RV Deekshitha  
3. Niteesh Balajee  
4. Tarun N Reddy  

---

# Problem Statement

Formula 1 produces a large amount of race and driver performance data every season. However, raw datasets alone do not provide meaningful insights into driver consistency, efficiency, and comparative performance.

This project aims to build a Driver Performance Analytics and Ranking System that:
- cleans and organizes Formula 1 race data,
- analyzes driver performance statistically,
- ranks drivers using performance metrics,
- visualizes trends and comparisons effectively.

---

# Technologies Used

## Programming Language
- Python

## Development Environment
- Visual Studio Code

## Libraries
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Version Control
- Git
- GitHub

---

# Project Structure

```text
f1-driver-analytics/
│
├── data/
│   ├── drivers.csv
│   ├── results.csv
│   ├── races.csv
│   ├── cleaned_f1.csv
│   ├── features.csv
│
├── src/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── main.py
│
├── performance_plot.png
├── top_drivers.png
├── requirements.txt
├── README.md
```

---

# Methodology

## 1. Data Collection

Formula 1 datasets were collected from public repositories containing:
- race results,
- driver information,
- race details,
- standings data.

Datasets used:
- drivers.csv
- results.csv
- races.csv
- constructors.csv
- driver_standings.csv
- constructor_results.csv

---

## 2. Data Cleaning and Integration

The raw datasets were cleaned and merged into a structured dataset.

Tasks performed:
- removing null values,
- selecting relevant columns,
- converting data types,
- filtering invalid race positions,
- merging datasets.

Output generated:
- `cleaned_f1.csv`

---

## 3. Feature Engineering

Performance metrics were calculated from the cleaned dataset.

Features created:
- Average Finishing Position
- Total Points
- Consistency Score
- Race Participation Statistics

Output generated:
- `features.csv`

---

## 4. Driver Ranking System

Drivers were ranked using weighted performance indicators including:
- total points,
- average finishing position,
- consistency.

This enabled comparative analysis between Formula 1 drivers.

---

## 5. Machine Learning Model

A Linear Regression model was implemented to study the relationship between performance metrics and total driver points.

### Features Used
- Average Position
- Consistency Score

### Target Variable
- Total Points

### Evaluation Metrics
- Mean Absolute Error (MAE)
- R² Score

---

## 6. Data Visualization

Visualizations were generated using Matplotlib.

Graphs created:
- Top 10 Driver Rankings
- Points vs Average Position
- Performance Relationship Graphs
- Consistency Distribution

---

# Git and GitHub Workflow

Git and GitHub were used throughout the project to demonstrate collaborative software development.

## Workflow Followed

- A central GitHub repository was created.
- Separate branches were used for different modules.
- Each team member contributed independently.
- Changes were committed with descriptive commit messages.
- Pull Requests were created for merging.
- Branches were merged into the main branch after verification.

## Branches Used

```text
main
feature/data-cleaning
feature/feature-engineering
feature/analysis
feature/visualization
```

---

# How to Run the Project

## Step 1: Clone Repository

```bash
git clone <repository-link>
```

---

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3: Run Project Files

### Data Cleaning

```bash
python src/data_cleaning.py
```

### Feature Engineering

```bash
python src/feature_engineering.py
```

### Analysis and ML

```bash
python src/analysis.py
```

### Visualization

```bash
python src/visualization.py
```

---

# Outputs

The project generates:
- cleaned datasets,
- driver rankings,
- ML evaluation metrics,
- graphical visualizations,
- performance comparison charts.

---

# Future Improvements

Possible future enhancements include:
- real-time race analysis,
- advanced machine learning models,
- interactive dashboards,
- predictive analytics,
- season-wise performance forecasting.

---

# Conclusion

The Formula 1 Driver Performance Analytics and Ranking System successfully transforms raw race datasets into meaningful analytical insights.

The project demonstrates:
- data preprocessing,
- feature engineering,
- machine learning implementation,
- data visualization,
- collaborative development using Git and GitHub.
