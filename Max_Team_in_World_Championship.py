''' MAXIMUM NO OF TEAMS CAN THE HEAD TO PARTICIPATE WORLD CHAMPIONSHIP ATLEST K TIMES '''
N,K = map(int,input().split())
L = list(map(int,input().split()))[:N]
count= 0
for i in L:
    if(i+K <=5):
        count+=1
print(count//3)
