''' PROGRAM TO CHECK A CHARACTER IS VOWEL OR CONSONANT '''
import re
a=input()
sr=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if(sr.search(a) == None):
  if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
