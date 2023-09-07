arr=list(map(int,input().split()))
n=len(arr)
max=-100
smax=-100
min=1000
smin=1000
"""for i in range(n):
    if(arr[i]>max):
        max=arr[i]
    if(arr[i]<min):
        min=arr[i]
for i in range(n):
    if(arr[i]>smax and arr[i]!=max):
        smax=arr[i]
    if(arr[i]<smin and arr[i]!=min):
        smin=arr[i]
print(smax,smin)"""
for i in range(n):
    if(arr[i]>max):
        smax=max
        max=arr[i]
    if(arr[i]>smax and arr[i]!=max):
        smax=arr[i]
    if(arr[i]<min):
        smin=min
        min=arr[i]
    if(arr[i]<smin and arr[i]!=min):
        smin=arr[i]
print(smax,smin)
