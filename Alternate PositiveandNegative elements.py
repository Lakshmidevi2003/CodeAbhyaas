arr=list(map(int,input().split()))
n=len(arr)
b=[0]*n
pe=0
ne=1
for i in range(n):
    if(arr[i]>0):
        b[pe]=arr[i]
        pe+=2
    else:
        b[ne]=arr[i]
        ne+=2
print(b)
