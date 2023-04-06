import pandas as pd
import numpy as np

vit = pd.read_csv("mimic-iv-ed/2.2/ed/vitalsign.csv",low_memory=False)
edstays = pd.read_csv("mimic-iv-ed/2.2/ed/edstays.csv",low_memory=False)

def get_heartrate(vit, stay_id):
    hr = vit.loc[vit['stay_id'] == stay_id]['heartrate'];
    return hr

def get_respereation(vit, stay_id):    
    res = vit.loc[vit['stay_id'] == stay_id]['resperate'];
    return res

def get_o2(vit, stay_id):    
    o2 = vit.loc[vit['stay_id'] == stay_id]['o2sat'];
    return o2

def get_systolic_bp(vit, stay_id):    
    sbp = vit.loc[vit['stay_id'] == stay_id]['sbp'];
    return sbp

def get_dystolic_bp(vit, stay_id):    
    dbp = vit.loc[vit['stay_id'] == stay_id]['dbp'];
    return dbp

def get_temp(vit, stay_id):    
    temp = vit.loc[vit['stay_id'] == stay_id]['temperature'];
    return temp

def get_gender(edstays, stay_id):    
    gender = edstays.loc[edstays['stay_id'] == stay_id]['gender'];
    return gender

def get_intime(edstays, stay_id):    
    in_t = edstays.loc[edstays['stay_id'] == stay_id]['intime'];
    return in_t

def get_outtime(edstays, stay_id):    
    out = edstays.loc[edstays['stay_id'] == stay_id]['outtime'];
    return out

def get_race(edstays, stay_id):    
    race = edstays.loc[edstays['stay_id'] == stay_id]['race'];
    return race
