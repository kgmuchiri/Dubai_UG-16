# **Dubai_UG 16**
### *Machine Learning Portfolio for HW Dubai Group 16*

## Project Title: Heart Disease

## Group Members
  - Ilham Ghori
  - Juhanah Madhiyyah
  - Kanana Muchiri
  - Raiqah Shameer
  - Sherif Fares

## Project Milestones 
To meet our project goals effectively, we’ve set the following milestones with the final submission due in Week 11:

Week 3-4: Data acquisition and initial preprocessing.
Week 5-6: Feature selection and data exploration.
Week 7-8: Model selection and training.
Week 9-10: Model evaluation and tuning.
Week 11: Finalize documentation and submission.

## Dataset sources 
Dataset 1: Indicators of Heart Disease 2020 (CDC)
  - Original Source: US Centers for Disease Control and Prevention (CDC)
    - Link: https://www.cdc.gov/brfss/annual_data/annual_2020.html
  - Retrieved from: Kaggle
    - Link: https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease/data
  - License: Creative Commons (CC0) Public Domain
  - 2 specific examples from dataset presented nicely

### Sample Data
| AgeCategory | Sex   | BMI | Smoking | PhysicalActivity | HeartDisease |
|-------------|-------|-----|---------|------------------|--------------|
| 60-64       | Male  | 26  | No      | Yes             | No           |
| 18-24       | Female| 22  | Yes     | No              | Yes          |



Dataset 2:
  - Original Source: Mendeley Data
    - Link: https://data.mendeley.com/datasets/gwbz3fsgp8/2
  - License: Creative Commons Attribution 4.0
  - 2 specific examples from dataset presented nicely

### Sample Data
| AgeCategory | Sex   | BMI | PhysicalHealth | KidneyDisease | HeartDisease |
|-------------|-------|-----|---------|------------------|--------------|
| 45-49      | Female  | 28  | 7      | Yes             | No           |
| 35-39       | Male| 24  | 3     | No              | Yes          |


## Data Preparation Pipeline 
Our data preparation pipeline involves:

- Data Loading - Access and load the datasets into a usable format.
- Data Cleaning - Handle missing values and standardize formats.
- Feature Engineering - Encoding categorical variables and normalizing numerical values.
- Feature Selection - Based on correlation with the target variable, HeartDisease.
To run the pipeline, execute the script data_preparation.py in the scripts folder.

## Requirement Description
R2 - Data Analysis and Exploration
- Objective: To explore and analyze datasets, identifying relevant correlations and patterns.
- Location: R2 Data Analysis Notebook (link to be added)
- Model Outputs: Various health indicators predicting HeartDisease
- Model Inputs: 41 features reduced to 10, 20, and 41 selected features datasets.

A short description (100 words max.) of each requirements (R2–R5) and their location(s) within your 
repository using permanent links. This includes:
 - What is your model predicting? (a.k.a., the outputs)
 - What is your model using to predict from? (a.k.a., the inputs)
 - A table of results (especially for R4/R5), using Markdown tables
 - A figure showing the results, using permanent links

## Repo Structure
The main folders in this file include:
  - data - *for datasets*
  - notebooks  - *Jupyter notebooks for analysis/modelling*
  - scripts - *Python scripts for preprocessing/ML*
  - documentation - *project documents and weekly updates, organized per week*
