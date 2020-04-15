import pandas as pd
import numpy as np
import sys


def cleaningDataset(directory):
    df = pd.read_csv(str(directory));
    for col in df:
        if (col == '2015.2' or col == '2010.2' or  col == '2005.2' or col == '2000.2' or col == 'Unnamed: 0'):
            continue;
        else:
            df = df.drop([str(col)], axis = 1)
    
    countryList = ['India', 'Philippines', 'Bangladesh', 'China', 'Saudi Arabia', 'Poland', 'Russia', 'Germany', 'Ukraine', 
    'Serbia', 'Albania', 'Ecuador', 'Colombia', 'Brazil', 'Chile', 'Uganda', 'Kenya', 'Ethiopia', 'Morocco', 'South Africa', 'Nigeria', 
    'Burundi', 'United States', 'Canada', 'Mexico', 'Dominican Republic', 'Guatemala', 'Haiti', 'Australia', 'New Zealand', 'Solomon Islands', 'Fiji']
    countryList.sort()
    print(countryList)
    df = df. rename(columns = {'Unnamed: 0': 'Countries', '2015.2': '2015', '2010.2': '2010', '2005.2': '2005', '2000.2': '2000'})

    index = 0
    for country in df['Countries']:
        if (country == 'Country'):
            df = df.drop(index).reset_index(drop=True)
        index = index + 1

    index = 0
    df = df.dropna().reset_index(drop=True)
    for country2 in countryList:
        for country in df['Countries']:
            if str(country) == str(country2):
                continue;
            else:
                df = df[(df.Countries != country)]
                
    print(df.head(10))

        
    
    


cleaningDataset(sys.argv[1])


