arr = list(map(int, input().split()))
positive = []
negative = []
for i in range(len(arr)):
    if (arr[i] > 0):
        positive.append(arr[i])
    else:
        negative.append(arr[i])
i, j, k = 0, 0, 0
while (i < len(positive)):
    arr[k] = positive[i]
    k += 1
    i += 1
while (j < len(negative)):
    arr[k] = negative[j]
    k += 1
    j += 1
print(arr)

