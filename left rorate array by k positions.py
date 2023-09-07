arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
def leftrotate(arr,start,end):
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
leftrotate(arr,0,k-1)
leftrotate(arr,k,n-1)
leftrotate(arr,0,n-1)
print(arr)

