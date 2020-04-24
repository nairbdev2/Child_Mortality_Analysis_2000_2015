import pandas as pd
import numpy as np
import sys

#program thats takes in two paths, one for where the data is and the other one where the path is going to be saved.

#example running method: 
#python3 DiseaseCleaning.py 'datasets/Diseases/Injuries.csv' 'datasets/CleanedDiseases/CleanedInjuries.csv'
#this will save the Injuries.csv file to the CleanedDiseases path as CleanedInjures.csv
def cleaningDataset(directoryIn, directoryOutput):
    #read in the file
    df = pd.read_csv(str(directoryIn))

    #changes the columns to only look at the ones that have 0-4 years for those specifc years
    for col in df:
        if (col == '2015.2' or col == '2010.2' or  col == '2005.2' or col == '2000.2' or col == 'Unnamed: 0'):
            continue
        else:
            df = df.drop([str(col)], axis = 1)
    
    #list of countires that we want to look at 
    countryList = ['India', 'Philippines', 'Bangladesh', 'China', 'Saudi Arabia', 'Poland', 'Russian Federation', 'Germany', 'Ukraine', 
    'Serbia', 'Albania', 'Ecuador', 'Colombia', 'Brazil', 'Chile', 'Uganda', 'Kenya', 'Ethiopia', 'Morocco', 'South Africa', 'Nigeria', 
    'Burundi', 'United States of America', 'Canada', 'Mexico', 'Dominican Republic', 'Guatemala', 'Haiti', 'Australia', 'New Zealand', 'Solomon Islands', 'Fiji']
    countryList.sort()

    #rename the .2 for 0-4 years of death
    df = df.rename(columns = {'Unnamed: 0': 'Countries', '2015.2': '2015', '2010.2': '2010', '2005.2': '2005', '2000.2': '2000'})

    #removes the Country row that was not relevant
    index = 0
    for country in df['Countries']:
        if (country == 'Country'):
            df = df.drop(index).reset_index(drop=True)
        index = index + 1

    #drops the two nan rows that were not going to be used
    df = df.dropna().reset_index(drop=True)

    #adjusts the dataframe to only keep the data from the countries list
    index = 0
    for country in df['Countries']:
        if country == countryList[index]:
            if(index != len(countryList)-1):
                index = index + 1
        else:
            df = df[(df.Countries != country)]

    #reset the index of the rows            
    df = df.reset_index(drop=True)
    
    df.iat[24,0] = 'Russia'
    df.iat[31,0] = 'United States'
    df = df[['Countries', '2000', '2005', '2010', '2015']]
    #save the dataframe as a csv to proper directory
    df.to_csv(directoryOutput, index = False)
    
        
#call the function        
cleaningDataset(sys.argv[1], sys.argv[2])


