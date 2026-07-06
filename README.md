## Code Description

This project focuses on **intermediate-level data visualization and preprocessing** using Python. It demonstrates how to read multiple Excel datasets, extract useful information, preprocess the data, save reusable datasets, and create clean visualizations for analysis.

This repository is a continuation of my **Low Level Data Visualization** project, where I covered the fundamentals of data visualization. Here, I build upon those concepts by introducing data preprocessing, combining datasets, exporting processed files, and creating publication-ready visualizations. In the future, I will also add a **High Level Data Visualization** project to complete the learning journey.

### Overview

The workflow begins by importing the required libraries, including **Pandas** for data manipulation, **Matplotlib** for visualization, **Pathlib** for file management, and a custom plotting utility for consistent figure styling.

Two Excel datasets (`fsi-2020.xlsx` and `fsi-2021.xlsx`) are loaded from the raw data directory. Instead of using the complete datasets, only the required columns are selected to reduce unnecessary information and make the data easier to work with.

For the **2020** dataset, the script extracts the **Change from Previous Year** column, while for the **2021** dataset, it extracts the **X1: External Intervention** column. These columns are merged with the selected base data and then renamed to maintain a consistent structure across both datasets.

The processed datasets are saved as **Pickle** files, making them faster to reload during future analysis without repeatedly processing the original Excel files.

Next, both processed datasets are loaded back into memory and combined into a single DataFrame. This combined dataset is then visualized using a customized line chart that highlights the **Improvement** values.

The visualization includes customized axis labels, grid lines, legends, figure size adjustments, and predefined y-axis limits for better readability. Finally, the generated figure is automatically exported with sequential filenames, making it easy to manage multiple plots without overwriting previous results.

---

## Key Features

* Reads multiple Excel datasets using **Pandas**
* Extracts only the required columns from each dataset
* Merges additional analytical columns into the selected data
* Standardizes column names across different datasets
* Saves processed datasets as **Pickle** files
* Reloads processed data for efficient analysis
* Combines multiple processed datasets into a single DataFrame
* Creates customized line charts using **Matplotlib**
* Automatically exports figures with sequential filenames
* Organized and reusable workflow for intermediate-level data visualization

---

## my Workflow

<p align="center">
  <img src="https://img.shields.io/badge/1-Import%20Libraries-4CAF50?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/2-Load%20Excel%20Datasets-2196F3?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/3-Select%20Required%20Columns-FF9800?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/4-Merge%20Additional%20Data-E91E63?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/5-Rename%20Columns-9C27B0?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/6-Save%20Processed%20Data-00BCD4?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/7-Load%20Processed%20Data-795548?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/8-Combine%20Datasets-607D8B?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/9-Create%20Visualization-3F51B5?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/10-Automatically%20Export%20Figure-4CAF50?style=for-the-badge"/>
</p>

---

## Technologies Used

<p align="center">
  <img src="https://skillicons.dev/icons?i=python" alt="Python"/>
  <img src="https://skillicons.dev/icons?i=vscode" alt="VS Code"/>
  <img src="https://skillicons.dev/icons?i=git" alt="Git"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Pathlib-0A66C2?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Pickle-FFCA28?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Microsoft%20Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white"/>
</p>

---

## Output

After successful execution, the script generates:

* **processed_data_2020.pkl** – Processed dataset for 2020
* **processed_data_2021.pkl** – Processed dataset for 2021
* Automatically exported figures (`figure_1.png`, `figure_2.png`, ...)
* A customized line chart showing **Improvement** values
* Reusable processed datasets for further analysis and visualization

This project represents the **Intermediate Level** stage of my Data Visualization learning series. It extends the concepts introduced in my **Low Level Data Visualization** project by adding data preprocessing, dataset transformation, reusable storage using Pickle, automated figure exporting, and cleaner visualization techniques.

The next step in this series will be **High Level Data Visualization**, where I will explore advanced visualization techniques, interactive dashboards, statistical graphics, and more sophisticated analytical workflows.
