import math

def mean(data, n): 
    total = sum(data) 
    return total / n

def median(data, n): 
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2 
    else:
        return sorted_data[mid]


def mode(data):
     occ = {}
     for i in data:
        if i not in occ: 
             occ[i] = 1
        else:
            occ[i] += 1
     max_occ = max(occ.values())
     return [k for k, v in occ.items() if v == max_occ]


def range(data):
    return max(data) - min(data)


def var_sd(data, n):
     mean_val = mean(data, n)
 
     s1 = sum((x - mean_val) ** 2 for x in data) 
     variance = s1 / n
     sd = math.sqrt(variance)
     print("Variance of given data set is:", format(variance,".2f")) 
     print("Standard Deviation of given data set is:", format(sd, ".2f"))

data = list(map(int, input().split()))
n = len(data)
print("Mean of given data set is:", format(mean(data, n), ".2f")) 
print("Median of given data set is:", format(median(data, n), ".2f"))
print("Mode of given data set is:",*mode(data))
print("Range of given data set is:", format(range(data), ".2f"))
var_sd(data, n)
