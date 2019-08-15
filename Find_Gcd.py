""" PROGRAM TO FIND GCD """
import math
import functools
inp11,inp31=map(int,input().split())
List=[int(i) for i in input().split()]
for i in range(inp31):
    n,k=map(int,input().split())
    temp=functools.reduce(math.gcd,List[n-1:k])
    print(temp)
