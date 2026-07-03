## Code Description

This project demonstrates a simple and efficient workflow for working with multiple Excel datasets in Python. The main goal is to load data, visualize important information, combine data from multiple files, and export the final processed dataset for further analysis.

The script starts by importing the required libraries, including **Pandas** for data manipulation, **Matplotlib** for visualization, and **Glob** for automatically locating multiple Excel files.

First, the `fsi-2020.xlsx` dataset is loaded, and its first column is used as the DataFrame index. A selected column is then visualized using a line chart to better understand the data and identify any trends.

Instead of loading every file manually, the script automatically searches for all Excel files inside the specified folder. Each file is read into a DataFrame and combined into a single dataset using `pandas.concat()`. This makes the workflow scalable and easy to maintain when new datasets are added.

Once all datasets are merged, the **Total** column is plotted to visualize the overall trend across all files.

Finally, the processed dataset is exported in both **Excel** and **CSV** formats, making it ready for reporting, further analysis, or use in other projects.

---

## What This Project Does

* Loads Excel datasets using **Pandas**
* Sets the first column as the DataFrame index
* Creates line charts for quick data visualization
* Automatically detects all Excel files in a directory
* Combines multiple datasets into a single DataFrame
* Visualizes the overall trend using the **Total** column
* Exports the processed dataset as **Excel** and **CSV**
* Provides a reusable workflow for handling multiple Excel files

---

## Workflow

<p align="center">
<img src="https://img.shields.io/badge/Import-Libraries-blue?style=for-the-badge"/>
&nbsp;➜&nbsp;
<img src="https://img.shields.io/badge/Load-Dataset-success?style=for-the-badge"/>
&nbsp;➜&nbsp;
<img src="https://img.shields.io/badge/Visualize-Data-orange?style=for-the-badge"/>
&nbsp;➜&nbsp;
<img src="https://img.shields.io/badge/Find-Excel%20Files-purple?style=for-the-badge"/>
&nbsp;➜&nbsp;
<img src="https://img.shields.io/badge/Merge-Datasets-red?style=for-the-badge"/>
&nbsp;➜&nbsp;
<img src="https://img.shields.io/badge/Plot-Total-green?style=for-the-badge"/>
&nbsp;➜&nbsp;
<img src="https://img.shields.io/badge/Export-Results-brightgreen?style=for-the-badge"/>
</p>

---

## Technologies Used

<p align="center">

<img src="https://skillicons.dev/icons?i=python,vscode,git" />

<br><br>

<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>

<img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Glob-00599C?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Microsoft%20Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white"/>

</p>

---

## Output

After running the script, the following files are generated:

* `visualized_data.xlsx` – Processed Excel dataset
* `visualized_data.csv` – Processed CSV dataset
* Line charts for individual and combined datasets

---

## Why This Project?

This project was created to simplify the process of working with multiple Excel files. Instead of manually loading, merging, and visualizing each dataset, the entire workflow is automated in a clean and reusable way. It can easily be adapted for larger datasets or extended for more advanced data analysis tasks.

---

## Future Improvements

* Add support for additional chart types
* Export interactive visualizations
* Generate automated reports
* Add data validation and preprocessing
* Create a simple dashboard for data exploration
