from data_test import had_cardiac_arrest

testnum = 0;

def unittest(condition):
    global testnum;
    testnum += 1;
    if (condition):
        print(f"test {testnum} passed");
    else:
        print(f"test {testnum} failed");
        
        

def test_had_cardiac_arrest():
    unittest(had_cardiac_arrest(31660580) == 1); #1
    unittest(had_cardiac_arrest(35217617) == 0); #2
    unittest(had_cardiac_arrest(34547687) == 1); #3
    unittest(had_cardiac_arrest(31241097) == 0); #4
    unittest(had_cardiac_arrest(30242117) == 1); #5
    unittest(had_cardiac_arrest(31633441) == 1); #6
    
    
    
if __name__ == "__main__":
    test_had_cardiac_arrest();