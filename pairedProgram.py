from random import randint

###Level 1
##numList = []
##multipleList = []
##for x in range(100):
##    num = randint(10, 99)
##    numList.append(num)
##for num in numList:
##    if num % 5 == 0:
##        multipleList.append(num)
##print(multipleList)



###Level 2
#FUNCTIONS
def multiples5(numList):
    multipleSum2 = 0
    for num in numList:
        if num % 5 == 0:
            multipleSum2 += num
    return multipleSum2

def multiples3(numList):
    multipleSum1 = 0
    for num in numList:
        if num % 3 == 0:
            multipleSum1 += num
    return multipleSum1


#RUNNING CODE
numList = []

for x in range(100):
    num = randint(10, 99)
    numList.append(num)
    
print(numList)
multipleSum1 = multiples5(numList)
multipleSum2 = multiples3(numList)
sumAll = multipleSum1 + multipleSum2
print(sumAll) 


    
###Level 3
##
##primeSum = 0
##numList = []
##for x in range(100):
##    num = randint(10, 99)
##    numList.append(num)
##
##for num in numList:
##    prime = True
##    for x in range(2,num):
##        if num % x == 0:
##            prime = False
##    if prime == True:
##        primeSum += num
##       
##print(primeSum)
##
##    
    
