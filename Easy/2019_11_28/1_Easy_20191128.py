#1 2019/11/28 Easy

array = [5, 4, 3, 5, 8]
k = 10

length = len(array)
result = []

for i in range(length):
    for j in range(length):
        if(i != j and array[i] + array[j] == k):
            tuple = (array[i], array[j])
            if tuple not in result:
                result.append(tuple)

print(result)