""" PROGRAM TO FIND SMALLEST NUMBER AFTER DELETING K DIGIT """
from itertools import combinations
num1,num2=map(int,input().split())
g=len(str(num1))
l1=list(combinations(str(num1),g-num2))
l1=(sorted(l1))
l="".join(l1[0])
print(l)
