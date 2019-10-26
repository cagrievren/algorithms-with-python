import random

def bubbleSort(array):
    first = 0
    while(isSorted(array) == False):
        first = 0
        for i in range(0, len(array) - 1):
            if(array[i] > array[i+1]):
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
            else:
                continue
    print('BUBBLE SORTED => ')
    print(array)

def isSorted(array):
    flag = 0
    for i in range(0, len(array) - 1):
        if(array[i] <= array[i+1]):
            flag += 1

    if(flag == len(array) - 1):
        return True
    else:
        return False

def fillRand(array, number):
    for i in range(0, number):
        array.append(random.randint(1, 100))


array = []
fillRand(array, 20)
print(array)
bubbleSort(array)