import random
def selectionSort (unsortedArray):
    for i in range(0,len(unsortedArray)):
        minNumber, minIndex = minFind(unsortedArray , (i) , len(unsortedArray))
        unsortedArray[i] , unsortedArray[minIndex] = swap(unsortedArray[i] , unsortedArray[minIndex])
    print('SELECTION  SORTED => ')
    print (unsortedArray)

def minFind(array,i,j):
    minNumber = array[i]
    minIndex = i
    if(i<j):
        for k in range(i  ,j):
            if array[k] < minNumber :
                minNumber = array[k]
                minIndex = k
    return minNumber, minIndex

def swap (one, two):
    temp = one
    one = two
    two = temp
    return one , two

def fillRand(array, number):
    for i in range(0,number):
        array.append(random.randint(1,100))
        
array = []  
fillRand(array, 20)
print(array)
selectionSort(array)
