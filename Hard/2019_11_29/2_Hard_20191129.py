#2 2019/11/29 Hard

arr = [1, 2, 3, 4, 5]
result = []

for i in range(len(arr)):
    prod = 1
    for j in range(len(arr)):
        if (j != i):
            prod *= arr[j]
    result.append(prod)

print(result)