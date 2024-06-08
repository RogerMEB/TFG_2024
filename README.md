# Utilizing Community Detection for Classifying Students' Responses in CSCL Activities 

## Overview

The aim of this project is to retrieve as much information as posible from the rating systems of CSCL activities in order to provide a classification of the students and their answers.
Exploring different community detection methods and displaying the relevant data in the most understandable manner.

This project involves the extraction of features from data, testing various classification methods, performing statistical analyses, and visualizing the results.
The steps and techniques include:

- **Data Processing**
- **Feature Extraction Computations**:
  - Array similarity
  - Direct similarity
  - Z-normalization
  - Min-max normalization 
- **Classification Methods Tested**:
  - Louvain
  - Label Propagation Algorithm (LPA)
  - Girvan-Newman
  - K-means
  - Hierarchical clustering
- **Evaluation Methods**:
  - Silhouette Score
  - Modularity
- **Statistical Functions**:
  - t-test
  - ANOVA
- **Visual Analysis**:
  - Histograms
  - Correlation Matrix
  - Heatmap
  - Boxplot
  - Scatter Plot
- **Results and Images**: The outputs of the above methods, including the prototype of the indicators visualizations.

## Data Gathered

The data used in this project was gathered from a Pyramid App activity provided by the TIDE research group from Universitat Pompeu Fabra. 
For the privacy of the students the original data files are not provided.

##Usage

Running the file main.py executes a sequence of functions which executes the feature extraction, the Louvain classification and displays the results.
Each function can also be executed and tested individually.(Or other calls added to the main.py)

## Libraries Used

Here is a brief descriptions of the libraries used for the project:

### NetworkX
- **Description**: NetworkX is a Python library for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
- **Official Page**: [NetworkX](https://networkx.github.io/)

### Seaborn
- **Description**: Seaborn is a Python visualization library based on matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics.
- **Official Page**: [Seaborn](https://seaborn.pydata.org/)

### Matplotlib
- **Description**: Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
- **Official Page**: [Matplotlib](https://matplotlib.org/)

### Math
- **Description**: The math module in Python provides access to mathematical functions defined by the C standard.
- **Official Page**: [Python Math Module](https://docs.python.org/3/library/math.html)

### Community
- **Description**: This library provides functions for community detection in graphs and is often used with NetworkX.
- **Official Page**: [python-louvain (Community)](https://python-louvain.readthedocs.io/en/latest/)

### Scikit-learn
- **Description**: Scikit-learn is a machine learning library for Python that provides simple and efficient tools for data mining and data analysis. It features various classification, regression, and clustering algorithms, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.
- **Official Page**: [Scikit-learn](https://scikit-learn.org/)

### Pyexcel-ODS
- **Description**: Pyexcel-ODS is a Python library that provides support for reading, writing, and manipulating OpenDocument Spreadsheet (ODS) files. It allows users to handle ODS files in a simple and intuitive way.
- **Official Page**: [Pyexcel-ODS](https://pypi.org/project/pyexcel-ods/)

To run the project, make sure you have all the required libraries installed.
