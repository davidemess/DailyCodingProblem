#4 Hard 2019/12/02

array = [3, 4, -1, 1]

def main():
    array.sort()
    print(func())

def func():
    for i in range(len(array)):
        if (len(array) > i+1):
          if (array[i] > 0 and array[i] != array[i+1] and array[i] + 1 != array[i+1]):
                return(array[i]+1)
        else:
            return(array[i]+1)


main()