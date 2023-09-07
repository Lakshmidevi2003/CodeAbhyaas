arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
def rightrotate(arr,start,end):
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
rightrotate(arr,0,n-1)
rightrotate(arr,0,k-1)
rightrotate(arr,k,n-1)
print(arr)