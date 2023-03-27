# FILTER STUFF
def FILTERS():
    quick = [1, 2, 3, 4, 5, 50, 60, 70]
    newList = []

    for number in quick:
        if (number > 10):
            newList.append(number)

    print("Using loops: ", newList)

    def gtTen(numb):
        return numb > 10

    newList = list(filter(gtTen, quick))

    print("Using filter: ", newList)

    lambdaList = list(filter(lambda numb: numb > 10, quick))

    print('Using lambda: ', lambdaList)


# MAP STUFF

def MAP():
    anotherQuick = list(range(0, 50))
    print("Regular list: ", anotherQuick)

    squares = list(map(lambda numb: numb**2, anotherQuick))
    print("Squares: ", squares)

from functools import reduce

def REDUCE():
    sumThis = list(range(0, 50))

    def mySum(x, y):
        return x + y
    
    finalSum = reduce(mySum, sumThis)
    print("Using reduce: ", finalSum)
    print("Using sum: ", sum(sumThis))
        



REDUCE()