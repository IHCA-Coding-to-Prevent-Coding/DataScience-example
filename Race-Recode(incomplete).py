#import data
import pandas as pd
import numpy as np
#checking names
admissions=pd.read_csv("physionet.org/files/Testing/edstays.csv")
print(admissions['race'].unique())

def racial_categories():
    #Feel free to take these out idk when you guys loaded in these libraries
    import pandas as pd
    import numpy as np
    #Read in the edstays dataset
    admissions=pd.read_csv("physionet.org/files/Testing/edstays.csv")
##The following block does work on its own
    #White also contains Portugese
    admissions.loc[admissions["race"].str.contains("WHITE"), "race"] = "WHITE"
    admissions.loc[admissions["race"].str.contains("PORTUGUESE"), "race"] = "WHITE"
    #Hispanic/Latino contains South American
    admissions.loc[admissions["race"].str.contains("HISPANIC"), "race"] = "HISPANIC/LATINO"
    admissions.loc[admissions["race"].str.contains("SOUTH AMERICAN"), "race"] = "HISPANIC/LATINO"
    #Black/African American
    admissions.loc[admissions["race"].str.contains("BLACK"), "race"] = "BLACK"
    #Asian
    admissions.loc[admissions["race"].str.contains("ASIAN"), "race"] = "ASIAN"
    # American Indian/Alaska Native
    admissions.loc[admissions["race"].str.contains("AMERICAN INDIAN"), "race"] = "AMERICAN INDIAN/ALASKA NATIVE"
    # Native Hawaiian/Pacific islander
    admissions.loc[admissions["race"].str.contains("NATIVE HAWAIIAN"), "race"] = "NATIVE HAWAIIAN"
    #Unknown includes patients who declined to answer, replied multiple race/ethnicity, or did not have results
    admissions.loc[admissions["race"].str.contains("OTHER"), "race"] ="UNKNOWN"
    admissions.loc[admissions["race"].str.contains("UNKNOWN"), "race"] ="UNKNOWN"
    admissions.loc[admissions["race"].str.contains("PATIENT DECLINED TO ANSWER"), "race"] ="UNKNOWN"
    admissions.loc[admissions["race"].str.contains("MULTIPLE RACE/ETHNICITY"), "race"] ="UNKNOWN"
    admissions.loc[admissions["race"].str.contains("UNABLE TO OBTAIN"), "race"] ="UNKNOWN"
#end of part that is confirmed to wo
    # Create the dictionary to recode into numbers
    race_dictionary ={'AMERICAN INDIAN/ALASKA NATIVE': 1, 'ASIAN':2 , 'BLACK':3, 'HISPANIC/LATINO':4, 'NATIVE HAWAIIAN':5 ,
                      "UNKNOWN":6, "WHITE":7}
    Race_Dataframe['race_num'] = Race_Dataframe['race'].map(race_dictionary)

    #return the completed dataframe
    print(Race_Dataframe.head())