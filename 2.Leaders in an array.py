arr=list(map(int,input().split()))
n=len(arr)
max=arr[n-1]
leaders=[max]
for i in range(n-2,-1,-1):
    if(arr[i]>=max):
        max=arr[i]
        leaders.append(max)
leaders.reverse()
print(*leaders)

