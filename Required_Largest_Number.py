""" PROGRAM TO PRINT REQUIRED LARGEST NUMBER IN A LIST ELEMENTS """
a,b=input().split()
a=int(a)
b=int(b)
l=input().split()
l.sort()
print(l[-b])
