## Functions

def bubbleSort(lissy):
    for index2 in range(len(lissy)-1, 0, -1):
        for index in range(index2):
            if (lissy[index] > lissy[index + 1]):
                num = lissy[index]
                lissy[index] = lissy[index + 1]
                lissy[index + 1] = num


def binSearch(lissy, num):
    first = 0
    last = len(lissy)-1
    found = False
    
    while(first <= last) and not found:
        mid = (first + last) // 2
        
        if (lissy[mid] == num):
            found = True
        else:
            if(num<lissy[mid]):
                last = mid-1
            else:
                first = mid+1
    return found

## Running Code
listA = [3, 6, 49, 11, 12, 0, 33]
bubbleSort(listA)
##print(listA)
print(binSearch(listA,14))
print(binSearch(listA,0))
##listA.sort()
##print(listA)
