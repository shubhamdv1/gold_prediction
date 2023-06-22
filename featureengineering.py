from sklearn import preprocessing
le = preprocessing.LabelEncoder()
import pandas as pd
from datapreprocessing import data_preprocessing

def feature_engineering():
    dataset = data_preprocessing()

    # Convert 'Date' column to datetime
    dataset['date_parsed'] = pd.to_datetime(dataset['Date'], format="%Y-%m-%d")
    
    # Extract additional features from 'date_parsed'
    dataset['day_of_month'] = dataset['date_parsed'].dt.day
    dataset['month_of_year'] = dataset['date_parsed'].dt.month
    dataset['year'] = dataset['date_parsed'].dt.year
    
    dataset.drop(['Date'], inplace=True, axis=1)
    
    dataset.to_csv("Gold_cleaned_dataset.csv", index = False)
    return dataset

feature_engineering()