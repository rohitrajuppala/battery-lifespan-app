#  Battery Life Prediction & Performance Monitoring

A complete data science project focused on understanding, visualizing, and predicting battery performance using real-world charge and discharge cycle data. This repository combines **exploratory data analysis**, **machine learning**, and **data visualization** to offer practical insights into battery health and degradation.

---

##  Project Highlights

*  **Machine Learning Models** for battery life prediction
*  **Visualization of charge/discharge cycles** (voltage, current, temperature)
*  **Histograms, scatter plots, heatmaps** for performance interpretation
*  **Data cleaning and feature engineering** for model readiness
*  Based on **NASA's battery degradation dataset**

---

##  Methodology Overview

###  Data Source

* **Dataset**: NASA Battery Prognostics Dataset
* **Attributes**: Voltage (V), Current (A), Temperature (°C), Time (s), Capacity (Ah)

###  Data Preprocessing

* Handled missing values using interpolation and mean imputation
* Removed severe outliers using **Z-Score** and **IQR**
* Engineered features: temperature-voltage interaction, energy efficiency, etc.

###  Exploratory Data Analysis (EDA)

* Distribution analysis via **histograms and boxplots**
* Relationships visualized with **scatterplots** and **correlation heatmaps**
* Identified key variables: **voltage** (positive correlation) and **temperature** (nonlinear impact)

###  Machine Learning Models

| Model             | Description                     | Evaluation Metric (RMSE) |
| ----------------- | ------------------------------- | ------------------------ |
| Linear Regression | Baseline comparison             | 0.0421                   |
| Ridge Regression  | Regularized model (best result) | 0.0365                   |
| Lasso Regression  | Variable selection focus        | 0.0389                   |

---

##  Sample Visualizations

* Histograms of voltage, current, and temperature over cycles
* Scatterplots showing degradation trends
* Heatmaps of feature correlations

>  Visuals can be found in `Battery Performance Monitoring.docx` and `Analysis of Charge Cycles.pdf`.

---

##  How to Use

### Prerequisites

```bash
pip install numpy pandas matplotlib scikit-learn
```

### Run Scripts

```bash
# Run EDA and preprocessing
python life_span_of_battery.py

# Run battery life prediction model
python battery_life_span.py
```

---

##  Related Research Questions

* How do voltage and temperature affect battery health over time?
* Can ML models predict battery capacity with limited cycle data?
* What visualization techniques best highlight performance anomalies?

---

##  License

This project is open-sourced under the **MIT License**.
See [`LICENSE`](LICENSE) for full terms.

---

## 👨‍💻 Authors

* **Rohit Raj Uppala** – Data Scientist | [LinkedIn](Great! Since this research is not under publication and **you’re open to making it open-source**, here is a polished and **GitHub-friendly `README.md`** tailored for public sharing of your **Battery Life Prediction & Monitoring** project:

---

# 🔋 Battery Life Prediction & Performance Monitoring

A complete data science project focused on understanding, visualizing, and predicting battery performance using real-world charge and discharge cycle data. This repository combines **exploratory data analysis**, **machine learning**, and **data visualization** to offer practical insights into battery health and degradation.

---

## 📌 Project Highlights

* 🧪 **Machine Learning Models** for battery life prediction
* 📊 **Visualization of charge/discharge cycles** (voltage, current, temperature)
* 📈 **Histograms, scatter plots, heatmaps** for performance interpretation
* 🧹 **Data cleaning and feature engineering** for model readiness
* 📚 Based on **NASA's battery degradation dataset**

---

## 📂 Repository Structure

```
📦battery-life-prediction
 ┣ 📜battery_life_span.py                   # ML modeling and prediction script
 ┣ 📜life_span_of_battery.py               # Data preprocessing and EDA
 ┣ 📄Battery_Life_Prediction_APA_Report.pdf # Final research paper with results
 ┣ 📄Battery Performance Monitoring.docx    # Visual storytelling and graph analysis
 ┣ 📄Analysis of Charge Cycles.pdf          # Annotated visuals of charge/discharge patterns
 ┣ 📜README.md                              # Project documentation (this file)
 ┗ 📁plots/                                 # Optional visual output directory
```

---

## 🔬 Methodology Overview

### 🔍 Data Source

* **Dataset**: NASA Battery Prognostics Dataset
* **Attributes**: Voltage (V), Current (A), Temperature (°C), Time (s), Capacity (Ah)

### 🧹 Data Preprocessing

* Handled missing values using interpolation and mean imputation
* Removed severe outliers using **Z-Score** and **IQR**
* Engineered features: temperature-voltage interaction, energy efficiency, etc.

### 📊 Exploratory Data Analysis (EDA)

* Distribution analysis via **histograms and boxplots**
* Relationships visualized with **scatterplots** and **correlation heatmaps**
* Identified key variables: **voltage** (positive correlation) and **temperature** (nonlinear impact)

### 🤖 Machine Learning Models

| Model             | Description                     | Evaluation Metric (RMSE) |
| ----------------- | ------------------------------- | ------------------------ |
| Linear Regression | Baseline comparison             | 0.0421                   |
| Ridge Regression  | Regularized model (best result) | 0.0365                   |
| Lasso Regression  | Variable selection focus        | 0.0389                   |

---

## 📈 Sample Visualizations

* Histograms of voltage, current, and temperature over cycles
* Scatterplots showing degradation trends
* Heatmaps of feature correlations

> 📸 Visuals can be found in `Battery Performance Monitoring.docx` and `Analysis of Charge Cycles.pdf`.

---

## 🧪 How to Use

### Prerequisites

```bash
pip install numpy pandas matplotlib scikit-learn
```

### Run Scripts

```bash
# Run EDA and preprocessing
python life_span_of_battery.py

# Run battery life prediction model
python battery_life_span.py
```

---

## 📖 Related Research Questions

* How do voltage and temperature affect battery health over time?
* Can ML models predict battery capacity with limited cycle data?
* What visualization techniques best highlight performance anomalies?

---

## 📃 License

This project is open-sourced under the **MIT License**.
See [`LICENSE`](LICENSE) for full terms.

---

##  Authors

* **Rohit Raj Uppala** – Data Scientist | [LinkedIn]([https://www.linkedin.com/in/ambca-m-638k74329](https://www.linkedin.com/in/uppala-rohit-raj-68ba7b217/))



##  Contributions

Feel free to fork, contribute, or open issues. We welcome:

* Visualization improvements
* Additional battery datasets
* Model performance enhancement

