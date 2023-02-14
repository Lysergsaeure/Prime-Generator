import time
n = 1
primeArray = []
listOfBools =[]
factorList = []

while len(primeArray) < 10000:
    listOfBools.clear()
    factorList.clear()
    factorList = list(range(2,int(n**(0.5))+1))
    for divisor in factorList:
        if n % divisor != 0:
            listOfBools.append(0)
        else:
            listOfBools.append(1)
            break
    if 1 in listOfBools:
         n = n + 2
    else:
        primeArray.append(n)
        print(n)
        time.sleep(0.2)
        n = n + 2
else:
    print(primeArray)
