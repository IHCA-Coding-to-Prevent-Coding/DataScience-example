from data_test import had_cardiac_arrest
from data_test import get_stay_length

testnum = 0;

def unittest(condition, name=testnum):
    global testnum;
    testnum += 1;
    if (condition):
        print(f"test {name} passed");
    else:
        print(f"test {name} failed");
        
        

def test_had_cardiac_arrest():
    unittest(had_cardiac_arrest(31660580) == 1); #1
    unittest(had_cardiac_arrest(35217617) == 0); #2
    unittest(had_cardiac_arrest(34547687) == 1); #3
    unittest(had_cardiac_arrest(31241097) == 0); #4
    unittest(had_cardiac_arrest(30242117) == 1); #5
    unittest(had_cardiac_arrest(31633441) == 1); #6
    
def test_get_stay_length():
    # TODO answers should be the actual lengths, i can't see data now
    unittest(get_stay_length(31660580) == 0); #1
    unittest(get_stay_length(35217617) == 0); #2
    unittest(get_stay_length(34547687) == 0); #3
    unittest(get_stay_length(31241097) == 0); #4
    unittest(get_stay_length(30242117) == 0); #5
    unittest(get_stay_length(31633441) == 0); #6 
if __name__ == "__main__":
    test_had_cardiac_arrest();
    test_get_stay_length();