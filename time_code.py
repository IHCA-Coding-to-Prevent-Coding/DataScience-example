import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# dia = pd.read_csv("physionet.org/files/mimic-iv-ed/2.2/ed/diagnosis.csv")
vit = pd.read_csv("/home/x-adewan/physionet.org/files/mimic-iv-ed/2.2/ed/vitalsign.csv")

print(vit.head())

charttimes = vit['charttime'];
stayids = vit['stay_id'];


histVals = [];

i = 0;
while ( i < 15 ): # i < len(stayids)-2
    
    curr_stay_id = stayids[i];

    # date, time = charttime.split(" ")
    # date_time = datetime.strptime(charttimes[i], '%Y-%m-%d %H:%M:%S');
    stayidsequal = stayids[i] == stayids[i+1];
    #j = 0;
    if (not stayidsequal):
        i+=1;
        continue;
    while (stayidsequal):
        #same_stay = [];

        #while (i < 10):
        
        ith_date_time = datetime.strptime(charttimes[i], '%Y-%m-%d %H:%M:%S');

        ith_date_time = datetime.strptime(charttimes[i+1], '%Y-%m-%d %H:%M:%S') - ith_date_time;

        histVals.append(abs(ith_date_time.total_seconds() / 60.0));
        print(f"Before 2nd +: %d", i);
        i+=1;
        stayidsequal = stayids[i] == stayids[i+1];
        print(f"After increment: %d", i);
        #print(same_stay);
        #histVals = same_stay;
    print(f"before 1st loop increment: %d", i);
    i+=1;
    print(f"after 1st loop increment: %d", i);
    #print(i)
        
print(histVals)
len(histVals)