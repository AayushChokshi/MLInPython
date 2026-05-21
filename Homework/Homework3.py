# python3 -m pip install matplotlib

import matplotlib.pyplot as plt
#   Today we will implement linear regression on some data
data = [
    [650, 158000],
    [700, 149000],
    [750, 171000],
    [800, 182000],
    [850, 176000],
    [900, 205000],
    [950, 198000],
    [1000, 225000],
    [1050, 214000],
    [1100, 247000],
    [1150, 238000],
    [1200, 271000],
    [1250, 259000],
    [1300, 291000],
    [1350, 278000],
    [1400, 315000],
    [1450, 301000],
    [1500, 336000],
    [1550, 322000],
    [1600, 358000],
    [1650, 341000],
    [1700, 381000],
    [1750, 366000],
    [1800, 402000],
    [1850, 389000],
    [1900, 431000],
    [1950, 417000],
    [2000, 455000],
    [2100, 472000],
    [2200, 515000]
]


def computeSums(data):
    sumX = 0
    sumY = 0
    sumXY = 0
    sumX2 = 0

    for x, y in data:
        sumX += x
        sumY += y
        sumXY += x * y
        sumX2 += x * x

    return sumX, sumY, sumXY, sumX2


def computerSumX(data) :
    


# For homework, break this up into single functions


def bestFitSlope(data):
    n = len(data)
    sumX, sumY, sumXY, sumX2 = computeSums(data)

    numerator = n * sumXY - sumX * sumY
    denominator = n * sumX2 - sumX ** 2

    return numerator / denominator


def bestFitIntercept(data):
    n = len(data)
    sumX, sumY, _, _ = computeSums(data)

    m = bestFitSlope(data)

    return (sumY - m * sumX) / n


m = bestFitSlope(data)
b = bestFitIntercept(data)

print("Slope:", m)
print("Intercept:", b)

# x = []
# y = []

# for point in data:
#     x.append(point[0])
#     y.append(point[1])

# print(x)
# print(y)

# plt.scatter(x, y)

# plt.xlabel("Square Feet")
# plt.ylabel("Price")
# plt.title("House Prices vs Square Footage")

# # Domain of the line:
# x_line = [min(x), max(x)]
# # Range:
# y_line = [m * x + b for x in x_line]

# plt.plot(x_line, y_line, color='red')

# plt.show()