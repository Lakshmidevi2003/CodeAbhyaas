arr=list(map(int,input().split()))
temp=arr[0]
n=len(arr)
for i in range(n-1):
    arr[i]=arr[i+1]
arr[n-1]=temp
print(arr)