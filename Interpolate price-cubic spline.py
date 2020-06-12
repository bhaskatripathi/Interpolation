# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:09:31 2018
@author: Bhaskar T
This code performs a Cubic spline interpolation of third order on missing data values in a dataframe. Using this piece of code you can take yearly/monthly/quarterly/weekly/any missing date values in a Time series and interpolate them with daily values
"""
# Before running this code Make sure the input file has manually formatted date column 
import warnings, pandas as pd, re, os, numpy as np, time, math, configparser
from scipy.interpolate import interp1d
import pandas as pd
from datetime import datetime
if os.getcwd().lower().startswith('c:'):
  os.chdir(r'C:\Users\bhask\OneDrive\Desktop\PSO-SVM\BTC_Data_Jan2020')

import pandas as pd
import os

all_csv = [file_name for file_name in os.listdir(os.getcwd()) if '.csv' in file_name]
li = []


'''-- ITERATE OVER THE FILE LIST AND INTERPOLATE ALL FILES with Cubic spline 3rd order---'''
#for i in range(len(all_csv)): 
#    #read csv file
#    file_name= all_csv[i]
#    print(file_name) 	

for i in range(len(all_csv)):
    try:
        #read csv file
        file_name= all_csv[i]
        #file_name= "median-confirmation-time.csv"
        df = pd.read_csv(file_name)
        df.head(10)
        df.tail(10)
    
    
        #Resample data to daily series and apply linear interpolation
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.set_index("Date", drop = True)
        
        
        
        df = df.iloc[:,0].resample("D").interpolate(method='spline', order=3)
        df = df.reset_index()
        df["Date"] = df["Date"].astype(str)
        
        df.head(10)
        df.tail(10)
        
        
        #Save to csv file
        OutputDataSet = df
        OutputDataSet
        output_path = "Interpolation 1"+ "\\"+ file_name
        df.to_csv(output_path, encoding='utf-8', index=False)
        print("Sucessfully interpolated file name : ", file_name)
    except:
        print("Error occured in file...")
        print(file_name)

'''- READ ALL CSV FILES FROM THE FOLDER AND CREATE A VLOOKUP ON VALUES AGAINST DATE COLUMN--'''

final_results = 0
for i in range(len(all_csv)-35):
    try:
        df_price = pd.read_csv("Interpolation 1"+ "\\"+ "market-price.csv")
        df_merge_temp= pd.read_csv("Interpolation 1"+ "\\"+ all_csv[i])
        results=df_price.merge(df_merge_temp,on='Date')
        final_results= results    
        print("Iteration : ",  i)
        print("Sucessfully interpolated file name : ",  all_csv[i])
    except:
        print("Error occured in file...")
        print(all_csv[i])

df_price = pd.read_csv("Interpolation 1"+ "\\"+ "market-price.csv")
df1= pd.read_csv("Interpolation 1"+ "\\"+ "AUD_USD.csv")
results=df_price.merge(df1,on='Date')

'''- MERGE VLOOKEDUP VALUES INTO A SINGLE DATAFRAME AND SAVE TO CSV FILE--'''
j=0
for i in range(len(all_csv)):
    try:
        i=i+1  
        j=i
        print("dataframe no : ",  j)
        if i<40 :
            j= pd.read_csv("Interpolation 1"+ "\\"+ all_csv[i])
            results=results.merge(j,on='Date')
            print("Iteration : ",  i)
            print("Sucessfully interpolated file name : ",  all_csv[i])
    except:
        print("Error occured in file...")
        #print(all_csv[i])


