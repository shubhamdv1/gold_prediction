from dataanalysis import data_analysis
import pandas as pd
def data_preprocessing():
    dataset = data_analysis()
    dataset['date_parsed'] = pd.to_datetime(dataset['Date'],format="%Y-%m-%d")
    dataset['day_of_month'] = (dataset['date_parsed'].dt.day).astype(int)
    dataset['month_of_year'] = (dataset['date_parsed'].dt.month).astype(int)
    dataset['year'] = (dataset['date_parsed'].dt.year).astype(int)

    # Remove duplicates
    dataset.drop_duplicates(inplace=True)  # Remove duplicate rows

    # Drop columns with a high percentage of missing values
    threshold = 0.8  # Set your desired threshold
    dataset.dropna(thresh=threshold*len(dataset), inplace=True, axis=1)
    dataset.drop(['Date'], inplace=True, axis=1)

    # Fill missing values in numerical columns with the mean
    dataset.fillna(dataset.mean(numeric_only=True), inplace=True)
    print(dataset.isnull().sum())
    return dataset
data_preprocessing()


