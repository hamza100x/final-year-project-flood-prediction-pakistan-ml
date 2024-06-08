# Flood Prediction in Pakistan Using Machine Learning

Floods are one of the natural disasters that are frequently experienced in Pakistan. This project focuses on improving flood prediction models to reduce the risk, loss of animal and human habitats and lives, and damage inflicted on property. Over the last two decades, machine learning algorithms have contributed considerably to the evolution of prediction systems, resulting in improved performance and cost-effective solutions. Due to its multiple advantages and possibilities, machine learning has grown in popularity.

The main contribution of this project is to demonstrate how machine learning models can be used to predict floods and provide insights into the best models. The dataset was extracted from the Google Earth Engine, and various machine learning methods such as Support Vector Regression (SVR), Logistic Regression, Decision Tree Regressor, and Random Forests were used to develop predictive models for predicting floods in Pakistan.

## Platform
- Operating System: windows 11 64-bit
- Languages: HTML, CSS, JavaScript, Python
- Tools: Django, Jupyter, Visual Studio code & Google Earth Engine


## Features

- Predicts floods using machine learning algorithms
- Compares the performance of different models
- Utilizes data from the Google Earth Engine
- Provides insights into the best-performing models

## Models
- Linear Regression
- Decision Tree Regressor
- Support Vector Regression (SVR)
- Random Forest Regression



## System Architecture
![Picture](https://github.com/hamza100x/final-year-project-flood-prediction-pakistan-ml/assets/57902630/b078764d-8bbd-4ad3-b1dd-6da4fbab17d7)

## Results
![image](https://github.com/hamza100x/final-year-project-flood-prediction-pakistan-ml/assets/57902630/b7dd24cc-dfcd-4f48-9462-696dbd9aaad4)

## R-squared Scores


| Province           | Models                         | Temp. | NDSI | NDVI | Precipitation |
|--------------------|--------------------------------|-------|------|------|---------------|
| Punjab             | Random Forest Regression      | 0.94  | 0.63 | 0.89 | 0.85          |
|                    | Support Vector Regression     | -0.119| -0.011| -0.02| -0.24         |
|                    | Linear Regression             | -0.008| 0.19 | 0.29 | 0.69          |
|                    | Decision Tree Regressor       | 0.91  | 0.38 | 0.82 | 0.79          |
| Federal            | Random Forest Regression      | 0.91  | 0.62 | 0.81 | 0.83          |
|                    | Support Vector Regression     | -0.078| 0.007| -0.02| -0.15         |
|                    | Linear Regression             | -0.023| 0.16 | 0.027| 0.54          |
|                    | Decision Tree Regressor       | 0.86  | 0.30 | 0.66 | 0.53          |
| Sindh              | Random Forest Regression      | 0.92  | 0.80 | 0.89 | 0.88          |
|                    | Support Vector Regression     | -0.030| -0.11| -0.007| 0.60         |
|                    | Linear Regression             | 0.004 | -0.03| 0.26 | 0.69          |
|                    | Decision Tree Regressor       | 0.86  | 0.70 | 0.79 | -0.15         |
| Balochistan        | Random Forest Regression      | 0.94  | 0.44 | 0.70 | 0.69          |
|                    | Support Vector Regression     | -0.15 | -0.45| -0.06| -0.14         |
|                    | Linear Regression             | -0.0013| 0.21 | 0.23 | 0.73          |
|                    | Decision Tree Regressor       | 0.92  | 0.017| 0.50 | 0.30          |
| Gilgit Baltistan   | Random Forest Regression      | 0.96  | 0.95 | 0.95 | 0.55          |
|                    | Support Vector Regression     | -0.065| 0.068| -0.04| 0.070         |
|                    | Linear Regression             | 0.013 | 0.75 | 0.79 | 0.50          |
|                    | Decision Tree Regressor       | 0.94  | 0.92 | 0.94 | 0.25          |
| Khyber Pakhtunkhwa| Random Forest Regression      | 0.94  | 0.82 | 0.91 | 0.70          |
|                    | Support Vector Regression     | -0.14 | 0.046| -0.041| 0.017        |
|                    | Linear Regression             | 0.004 | 0.68 | 0.48 | 0.78          |
|                    | Decision Tree Regressor       | 0.92  | 0.67 | 0.87 | 0.58          |


## Threshold

The following Table shows the value of Threshold values that we have used in our project. Threshold values have been stetted by taking the average precipitation of the months in which flood has occurred.


Province | Temperature | Precipitation | NDSI | NDVI
--- | --- | --- | --- | ---
Punjab | 0.94 | 0.85 | 0.63 | 0.89
Sindh | 0.92 | 0.88 | 0.80 | 0.89
Balochistan | 0.94 | 0.73 | 0.44 | 0.70
Federal | 0.91 | 0.81 | 0.62 | 0.81
Gilgit Baltistan | 0.96 | 0.55 | 0.95 | 0.95
Khyber Pakhtunkhwa | 0.94 | 0.78 | 0.82 | 0.91


