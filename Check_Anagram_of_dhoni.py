''' CHECK WHETHER THE GIVEN STRING IS AN ANAGRAM OF STRING 'dhoni' OR NOT '''
from collections import Counter 
str=input()
if(Counter(str)==Counter("dhoni")):
    print("yes")
else:
    print("no")
