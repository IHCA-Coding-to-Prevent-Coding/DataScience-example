import pandas as pd
import numpy as np
Demographics_data = pd.read_csv("mimic-iv-ed/2.2/ed/edstays.csv")
#excluding anyone who just said Portugese;
#South America as Hispanic;
#Other, Unknown, and declined to answer is all clumped into one;


