"""
Created on Wed Jun  6 11:12:53 2018
Christopher Hall, Wellcome Sanger Institute
@author: ch15@sanger.ac.uk
"""
import os
import pandas

for filename in os.listdir():
    outfile = open('errors.txt', 'a', encoding="utf8")
    if filename.endswith(".log"):
        with open(filename, 'r') as infile:
            for line in infile:
                if 'ERROR' in line:
                    line=line.replace('[','').replace(']','')
                    outfile.write(line)
    outfile.close()
dataframe = pandas.read_csv("errors.txt",delimiter="\t",names = ["Who knows", "DateTime", "Sortware", "Location", "Catagory", "Description"])
dataframe.iloc[:,1]=pandas.to_datetime(dataframe.iloc[:,1], format='%Y/%m/%d %H:%M:%S.%f')
dataframe['Date'] = dataframe.iloc[:,1].dt.date
dataframe['Time'] = dataframe.iloc[:,1].dt.time
dataframe=dataframe.drop(columns=["DateTime"])
dataframe=dataframe[["Who knows", "Date", "Time", "Sortware", "Location", "Catagory", "Description"]]
dataframe.to_csv("errors.csv", encoding='utf-8', index=False)
