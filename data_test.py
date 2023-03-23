import pandas as pd
import numpy as np


# create a function that takes in a stay_id and returns a "1" if the stay_id had a cardiac arrest
# and returns a "0" if the stay_id didn't
CA_data = pd.read_csv("mimic-iv-ed/2.2/ed/diagnosis.csv");
def had_cardiac_arrest(stay_id):
    return 1;

# load in the data and print the first few rows
data = pd.read_csv("mimic-iv-ed/2.2/ed/diagnosis.csv");
print(data.head)

stay_id = ['stay id']


# remove columns we don't want


# split the data into a list of dataframes for each stay_id


# lookup whether that stay_id had a cardiac arrest


# concatinate those together into one giant numpy array


# ship to neural net!

