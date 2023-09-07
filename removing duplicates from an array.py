arr=list(map(int,input().split()))
n=len(arr)
arr.sort()
i=0
for j in range(1,n):
    if(arr[j]!=arr[i]):
        i+=1
        arr[i]=arr[j]
print(arr[:i+1])
