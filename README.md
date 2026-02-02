# 📉 sensor-HAR-pipeline: End-to-End Human Activity Recognition

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Data Science](https://img.shields.io/badge/Focus-Signal%20Processing-FF6F00?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> **Automated Feature Extraction Pipeline for Wearable Fall Detection Systems.**

## 📖 Introduction

In wearable AIoT applications, raw sensor data is noisy and high-dimensional. Feeding raw data directly into Machine Learning models often leads to poor performance and high latency on edge devices (ESP32/Jetson Nano).

This repository provides a robust **ETL Pipeline** designed to transform raw accelerometer/gyroscope data into meaningful statistical features, optimized for **Fall Detection Models**.

## 🚀 Key Features

*   **⚡ Automated Sliding Window:** Converts continuous time-series data into structured instances (e.g., 50 samples/window).
*   **🧮 Advanced Feature Engineering:** Automatically extracts critical features for HAR (Human Activity Recognition):
    *   **Statistical:** Mean, Max, Min, Standard Deviation.
    *   **Higher-Order Stats:** Kurtosis (Peakedness), Skewness (Asymmetry).
    *   **Physics-based:** Signal Magnitude Vector (SVM), Jerk (Derivative of Acceleration).
*   **📊 Visualization Tools:** Built-in plotting modules to visualize signal spikes during Fall events vs. ADL (Activities of Daily Living).

## 📸 Visualization Showcase

One of the key challenges is distinguishing a **Fall** from a **Sit-down** action.
As shown below, the pipeline extracts specific signal signatures:
<img width="884" height="858" alt="image" src="https://github.com/user-attachments/assets/70cc8ba9-41bc-4f3b-bc25-ccc06c811dff" />


## 🛠️ How to Use

1.  **Setup:**
    *   Download the **WEDA Dataset** from the official source.
    *   Place the csv file into `data/raw/` folder.
    *   Install dependencies: `pip install -r requirements.txt`

2.  **Run the Pipeline:**
    Execute the python script to process data:
    ```bash
    python src/pipeline.py
    ```

3.  **Result:**
    The clean dataset with extracted features will be saved at `data/processed/wada_features.csv`.

## ⚖️ Disclaimer & Acknowledgements (Data Usage Policy)

### 1. Data Ownership
This repository **does not host or distribute** the original WEDA-FALL Dataset. The code provided here is strictly a **processing pipeline** (feature extraction logic) intended for educational and research purposes.
This project uses the WEDA-FALL dataset for experimental and research purposes.

Original dataset:
WEDA-FALL – Wrist Elderly Daily Activity and Fall Dataset  
Publicly available on GitHub.

All rights of the original dataset belong to the original authors.
This repository does not redistribute the raw dataset.

### 2. How to obtain the Data
To use this pipeline, users must download the dataset directly from the official source or contact the original authors.
*   **Dataset Name:** WEDA-FALL (Wrist Elderly Daily Activity and Fall Dataset)
*   **Original Source:** https://github.com/joaojtmarques/WEDA-FALL

### 3. Citation
If you use the WEDA dataset in your work, please cite the original paper by the authors:

Paper: Marques, J. et al. "WEDA: Wrist Elderly Daily Activity and Fall Dataset." (2023)

(Please refer to the official repository for the exact BibTeX citation).

*This project respects the intellectual property rights of the dataset creators.*

## 📂 Project Structure

```text
Sensor-HAR-Pipeline/
├── data/
│   ├── raw/               
│   └── processed/         # Cleaned example CSVs ready for ML training
├── notebooks/             # Generated plots and reports
├── src/
│   ├── features.py        # Mathematical formulas for feature extraction
│   └── pipeline.py       
│   └── window.py          # Cutting window and cut around peak
│   └── main.py   
│   └── precprocessing.py        
│
├── gitinore
├── LICENSE
└── README.md              # Project Documentation


