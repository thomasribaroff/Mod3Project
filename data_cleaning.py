"""
This module is for your data cleaning.
It should be repeatable.

## PRECLEANING
There should be a separate script recording how you transformed the json api calls into a dataframe and csv.

## SUPPORT FUNCTIONS
There can be an unlimited amount of support functions.
Each support function should have an informative name and return the partially cleaned bit of the dataset.
"""
import pandas as pd

def vcp(borough = 'Camden', year='2011', month='01',):
    
    data = pd.read_csv('London Crime Data 2011 to 2014/{}-{}-metropolitan-street.csv'.format(year,month))
    
    data['LSOA name'].fillna('No location', inplace = True)
            
    return len(data.loc[(data['LSOA name'].str.contains("Camden")) & \
                     ((data['Crime type'] == "Violent crime")|(data['Crime type'] == "Violence and sexual offences"))])/ \
                            len(data.loc[(data['LSOA name'].str.contains("Camden"))])
            

def support_function_two(example):
    pass

def support_function_three(example):
    pass

def full_clean():
    """
    This is the one function called that will run all the support functions.
    Assumption: Your data will be saved in a data folder and named "dirty_data.csv"

    :return: cleaned dataset to be passed to hypothesis testing and visualization modules.
    """
    dirty_data = pd.read_csv("./data/dirty_data.csv")

    cleaning_data1 = support_function_one(dirty_data)
    cleaning_data2 = support_function_two(cleaning_data1)
    cleaned_data= support_function_three(cleaning_data2)
    cleaned_data.to_csv('./data/cleaned_for_testing.csv')
    
    return cleaned_data