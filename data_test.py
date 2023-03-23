import pandas as pd
import numpy as np

from extract import *



# create a function that takes in a stay_id and returns a "1" if the stay_id had a cardiac arrest
# and returns a "0" if the stay_id didn't
CA_data = pd.read_csv("mimic-iv-ed/2.2/ed/diagnosis.csv")
def had_cardiac_arrest(stay_id, data=CA_data):
    '''
    CPT codes 
       92950, best to use
       99291, 
       99292
    ICD10 codes
        I462, cardiac arrest; underlying cardiac conditions
        I468, cardiac arrest; other underlying conditions 
        I469, cardiac arrest; cause unspecified
    ICD9 codes
        427.5, generic cardiac arrest (maps to I462, 8, 9 codes above)
    '''
    # figure out what the code was based on stay_id
    
    code = data.loc[data['stay_id'] == stay_id]['icd_code'].array;
    # print(f"code: {code}")

    # use the code to determine whether that stay had cardiac arrest and return the results    
    if ('92950' in code) or ('99291' in code) or ('99292' in code) or ('I462' in code) or ('I468' in code) or ('I469'  in code) or ('4275' in code):
        return 1
    else: 
        return 0

def get_one_person_data(stay_id, data=CA_data):
    
    pass;

if __name__ == "__main__":
    # load in the data and print the first few rows
    dia = pd.read_csv("mimic-iv-ed/2.2/ed/diagnosis.csv")
    print(dia.head)

    for stay_id in dia['stay_ids']:
        data_all = [stay_id, get_gender(edstays, stay_id), 
                    get_race(edstays, stay_id), get_temp(vit, stay_id), 
                    get_heartrate(vit, stay_id), get_o2(vit, stay_id),
                    get_respereation(vit, stay_id), get_systolic_bp(vit, stay_id),
                    get_dystolic_bp(vit, stay_id), get_intime(edstays, stay_id),
                    get_outtime(edstays, stay_id)];
        
    #change race to a consistent labeling system

    # remove columns we don't want
    #data.remove(columns)

    # split the data into a list of dataframes for each stay_id


    # lookup whether that stay_id had a cardiac arrest
    # call had_cardiac_arrest here with each datapoint to determine the label

    # concatinate those together into one giant numpy array


    # ship to neural net!

