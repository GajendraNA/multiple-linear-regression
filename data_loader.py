import pandas as pd
import os
import math

def check_csv():
    csv_files = []
    cur_dir = os.getcwd()
    content_list = os.listdir(cur_dir)
    for x in content_list:
        if x.split('.')[-1] == 'csv':
            csv_files.append(x)
    if len(csv_files) == 0:
        return 'No csv file found in the directory'
    return csv_files

def display_and_select_csv(csv_files):
    i = 0
    for file_name in csv_files:
        print(i, '   ', file_name)
        i += 1
    return csv_files[int(input("Select file to create ML model: "))]

def load_data(csv_file):
    dataset = pd.read_csv(csv_file)
    median_bedrooms = math.floor(dataset.bedrooms.median())
    dataset.bedrooms = dataset.bedrooms.fillna(median_bedrooms)
    return dataset
