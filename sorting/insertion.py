import random

def shift(array, k):
    minNumber = min(array[k:])
    ourMinIndex = array.index(minNumber,k)
    for i in range(ourMinIndex - 1, k - 1, - 1):
        array[i+1] = array[i]
    array[k] = minNumber

def insertionSort(array):
    for i in range (0, len(array)):
        shift(array,i)
    print('INSERTION SORTED => ')
    print(array)

def fillRand(array, number):
    for i in range(0, number):
        array.append(random.randint(1, 100))

array = []
fillRand(array, 20)
print(array)
insertionSort(array)

