import random
import statistics
import numpy as np

"""
def calc_mean(list):
    total = sum(list)
    mean = total / len(list)

    return mean

def calc_variance(list):
    sum_squared_difference = 0
    mean = calc_mean(list)
    var = 0.0

    for integer in list:
        sum_squared_difference += (integer - mean) ** 2

    var = sum_squared_difference/len(list)

    return var
"""

def calc(list):
    #calculate Mean
    total = sum(list)
    mean = total / len(list)

    #calculate Variance
    sum_squared_difference = 0
    var = 0.0

    for integer in list:
        sum_squared_difference += (integer - mean) ** 2

    var = sum_squared_difference/len(list)

    #calculate standard deviation
    x = 0.0
    epsilon = 0.01
    step = epsilon**2
    stdev = 0.0

    #1より小さい、大きいの2つに場合分け
    if var < 1:
    	while abs(x**2-var) >= epsilon:
    	    x += step
    else:
    	while abs(x**2-var) >= epsilon and x < var:
    	    x += step

    if abs(x**2 - var) >= epsilon:
        print("Failed on square root of ", var)
    else:
        stdev = x

    return mean, var, stdev

def main():
    n = int(input("Please input a positive integer: "))
    List = [random.randint(1, 100) for i in range(n)]
    print("List: ", List, "\n")
    mean, var , stdev = calc(List)

    print("Results using self-made functions: ")
    print("Mean:", mean)
    print("Variance:", var)
    print("Standard deviation:", stdev, "\n")

    print("Results using statistics library: ")
    print("Mean:", statistics.mean(List))
    print("Variance:", statistics.pvariance(List))
    print("Standard deviation:", statistics.stdev(List), "\n")

    print("Results using numpy library:")
    print("Mean:", np.mean(List))
    print("Variance:", np.var(List))
    print("Standard deviation:", np.std(List), "\n")

if __name__ == '__main__':
    main()
