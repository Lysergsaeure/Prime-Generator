import time
n = 1
primeArray = []
factorList = []
isPrime = None
satisfied = None
start_time = None

while satisfied != "N":
    print("How many Primes should be generated?")
    amountOfPrimes = input()
    isInt = None
    while isInt != True:
        if amountOfPrimes.isnumeric():
            isInt = True
        else:
            del(amountOfPrimes)
            print("Invalid Data Type! Please enter an Integer.")
            print("How many Primes should be generated?")
            amountOfPrimes = input()
            isInt = False
        start_time = time.time_ns()
    while len(primeArray) < int(amountOfPrimes):
        factorList.clear()
        factorList = list(range(2,int(n**(0.5))+1))
        for divisor in factorList:
            if n % divisor != 0:
                isPrime = True
            else:
                isPrime = False
                break
        if isPrime == False:
            n = n + 2
        else:
            primeArray.append(n)
            print(n)
            #time.sleep(0.1)
            n = n + 2
    print(primeArray)
    print("Generated", amountOfPrimes, "in", "%.4f seconds" % float(((time.time_ns() - start_time)/1000000000)))
    
    del start_time
    del isInt
    n = 1
    primeArray.clear()
    print("Want to go again? (Y/N)")
    satisfied = input()