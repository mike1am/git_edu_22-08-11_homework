from math import factorial

def combNum (totalNum, selNum):
    return factorial(totalNum) / factorial(selNum) / factorial(totalNum - selNum)

