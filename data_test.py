import pandas as pd
import numpy as np
import math 
from extract import *

ENTRIES_PER_DATAPOINT = 20; # the number vitalsign datapoints for each stay_id we will send to the neural net
STAY_IDS_TO_OBTAIN = 1000; # the number of stayids we will grab from the dataset

CA_data = pd.read_csv("mimic-iv-ed/2.2/ed/diagnosis.csv")
def had_cardiac_arrest(stay_id, data=CA_data):
    # create a function that takes in a stay_id and returns a "1" if the stay_id had a cardiac arrest
    # and returns a "0" if the stay_id didn't

    code = data.loc[data['stay_id'] == stay_id]['icd_code'].array;
    # print(f"code: {code}")

    # use the code to determine whether that stay had cardiac arrest and return the results    
    if ('92950' in code) or ('99291' in code) or ('99292' in code) or ('I462' in code) or ('I468' in code) or ('I469'  in code) or ('4275' in code):
        return 1
    else: 
        return 0

def get_one_person_data(stay_id, data=CA_data):
    return data[data['stay_id'] == stay_id]

def get_stay_length(stay_id, data = CA_data):
    one_person_data = get_one_person_data(stay_id, data)
    return len(one_person_data);

def load_data():
    dia = pd.read_csv("mimic-iv-ed/2.2/ed/vitalsign.csv",low_memory=False);
    

    print(dia.head())

    # for stay_id in dia['stay_ids']:
    #     data_all = [stay_id, get_gender(edstays, stay_id), 
    #                 get_race(edstays, stay_id), get_temp(vit, stay_id), 
    #                 get_heartrate(vit, stay_id), get_o2(vit, stay_id),
    #                 get_respereation(vit, stay_id), get_systolic_bp(vit, stay_id),
    #                 get_dystolic_bp(vit, stay_id), get_intime(edstays, stay_id),
    #                 get_outtime(edstays, stay_id)];
    
    # return the data frame
    return dia;

def remove_excess_columns(df):
    
    print("removing excess columns \n")
    # remove columns we don't want
    global ENTRIES_PER_DATAPOINT

    # new_data = data.drop([data['stay_id'].value_counts() < ENTRIES_PER_DATAPOINT].index, inplace = True)
    
    df = df.drop('subject_id', axis=1)
    df = df.drop('charttime', axis=1)
    # df = df.drop('resprate', axis=1)
    df = df.drop('rhythm', axis=1)
    df = df.drop('pain', axis=1)
    
    df = df.drop('temperature', axis=1);
    df = df.drop('gender', axis=1)
    
    print(df.head());
    '''
    ct = 1

    for stay_id in data['stay_id']:
        next_id = 
        while stay_id == next_id:
            ct += 1;
        needed = stay_id.tail(ENTRIES_PER_DATAPOINT) '''
    # ct = 0;
    # stayids = data['stay_id'];

    # current_id = stayids[ct]
    # stayidsequal = stayids[ct] == stayids[ct+1];
    
    # while (stayidsequal):
    #     #ct += 1;
    #     #continue;
    #     if ((ct < ENTRIES_PER_DATAPOINT or ct > ENTRIES_PER_DATAPOINT) and stayidsequal == 0):
    #         data.drop([data['stay_id'] == stayids[ct]].index, inplace = True)
        
    #if (ct != 7):
        
    #for stay_id in data:
        # df is the dataframe
        #if (ct != 7)
        #data.drop([data['stay_id'] ].index, inplace = True)
    return df;

def fix_race(edstaysdata): # gloria
    # change race to a consistent labeling system
    return edstaysdata;

def split_by_stay_id(df):
    # split the data into a list of dataframes for each stay_id
    # [ stayid1 <dataframe> , stayid2 <dataframe> ]
    # stay_id = data['stay_id']
    # dict_person = {}
    # for id in stay_id:
    #     person = data[data["stay_id"] == id]
    #     dict_person[stay_id].append(person)
    
    
    
    alreadyDone = [];
    stayids = [];
    
    
    for index, row in df.iterrows():
        if (row['stay_id'] in alreadyDone): 
            continue;
        if (len(stayids) >= STAY_IDS_TO_OBTAIN ): 
            break
        alreadyDone.append(row['stay_id']);
        
        stayid_specific_df = df.loc[df.stay_id==alreadyDone[-1]];
        if (ENTRIES_PER_DATAPOINT == -1 or stayid_specific_df.shape[0] > ENTRIES_PER_DATAPOINT):
            stayids.append(stayid_specific_df.tail(ENTRIES_PER_DATAPOINT));
    
    

    # save_list_of_dataframes(stayids)
    return stayids

def get_labels_from_data(data):
    # lookup whether that stay_id had a cardiac arrest
    # call had_cardiac_arrest here with each datapoint to determine the label
    # also drops stay_id from the data
    
    labels = np.zeros(len(data)); # create an empty array for the labels
    
    for i, df in enumerate(data):
        print(f"stay_id: {df['stay_id'].values[0]}")
        labels[i] = int(had_cardiac_arrest(df['stay_id'].values[0]));
        df.drop("stay_id", axis=1); # once we get the labels we can drop stay_id from the data
    return labels;

def data_to_numpy_array(data):
    output = np.empty((len(data), data[0].shape[0], data[0].shape[1]))

    for i, df in enumerate(data):
        print(df);
        output[i] = df.to_numpy()
    return output;

def remove_nan(data_list):
    # math.isnan(data)
    for df in data_list:
        #df.dropna(axis='index', how='any')
        df.fillna(0)
    return data_list
                    
def save_list_of_dataframes(dataframes):
    # save the array to a file to ship to neural net

    print("saving dataframe");
    
    for i, df in enumerate(dataframes):
        print(df)
        stay_id = df['stay_id'].iloc[0];
        df.to_hdf('data.h5', f'stayid_{stay_id}', mode='a')

    print('data saved')
        
# save the array to a file to ship to neural net
def save_data_to_file(data_array, filename="data.csv"):
    np.save(filename, data_array)
 
if __name__ == "__main__":
    # load in the data and print the first few rows
    data = load_data();

    #change race to a consistent labeling system
    data = fix_race(data);

    # remove columns we don't want
    data = remove_excess_columns(data);

    # split the data into a list of dataframes for each stay_id
    data = split_by_stay_id(data);

    # check whether stay_id is long enough, 7 values
    # lookup whether that stay_id had a cardiac arrest
    # call had_cardiac_arrest here with each datapoint to determine the label
    labels = get_labels_from_data(data);
    
    print(labels);
    
    
    # format everything into a single numpy array
    data_array = data_to_numpy_array(data);
    
    

    

