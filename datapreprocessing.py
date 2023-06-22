from dataanalysis import data_analysis
import pandas as pd
def data_preprocessing():
    dataset = data_analysis()
    
    # Remove duplicates
    dataset.drop_duplicates(inplace=True)  # Remove duplicate rows

    # Drop columns with a high percentage of missing values
    threshold = 0.8  # Set your desired threshold
    dataset.dropna(thresh=threshold*len(dataset), inplace=True, axis=1)

    # Fill missing values in numerical columns with the mean
    dataset.fillna(dataset.mean(numeric_only=True), inplace=True)
    print(dataset.isnull().sum())
    return dataset
data_preprocessing()


