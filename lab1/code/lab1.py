import intvalpy as ip
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
# Task 1

def calculateDet(delta):
        midA = [[1, 1.05], [1, 0.95]]
        radA = [[delta, delta], [delta, delta]]
        A = ip.Interval(midA, radA, midRadQ=True)
        detA = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return detA

# Find delta that 0 is in det(A)
def task1():
    deltaArray = np.linspace(0, 1, num=10)
    detArrayHight = []
    detArrayLow = []
    for i in range(len(deltaArray)):
        delta = deltaArray[i]
        detA = calculateDet(delta)
        detArrayHight.append(detA.b)
        detArrayLow.append(detA.a)
        #print(detA)
    plt.figure()
    plt.title("Task 1")
    plt.grid()
    plt.plot(deltaArray, detArrayHight, label = "det up border")
    plt.plot(deltaArray, detArrayLow, label = "det down border")
    plt.plot(0.05, calculateDet(0.05).a, 'o', label = "delta = 0.05")
    plt.xlabel('delta')
    plt.ylabel('det(A)')
    plt.legend()
    plt.show()

# Task 2

def det(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

def check(A):
    vertexes = A.vertex
    print(vertexes)
    i = 0
    while i < len(vertexes):
        j = i + 1
        while j < len(vertexes):
            if det(vertexes[i]) * det(vertexes[j]) <= 0:
                print("Matrix is special")
                return
            j += 1
        i += 1
    print("Matrix is not special")

# check if A is special
def task2(eps):
    mid = [[1.05, 1],
          [0.95, 1]]
    rad = [[eps, 0],
          [eps, 0]]

    A = ip.Interval(mid, rad,  midRadQ = True)
    print(A)
    check(A)

# Task 3

def glob_opt(func, eps, x0):
    yList = []
    y = x0
    fY = func(x0)
    L = [(y, fY)]
    while fY.wid >= eps:
        l = 0
        for i in range(1, len(y)):
            if y[i].wid > y[l].wid:
                l = i
        y1 = deepcopy(y)
        y1[l] = ip.Interval(y[l].a, y[l].mid)
        fY1 = func(y1)
        y2 = deepcopy(y)
        y2[l] = ip.Interval(y[l].mid, y[l].b)
        fY2 = func(y2)
        L = L[1:]
        L.append((y1, fY1))
        L.append((y2, fY2))
        L.sort(key=lambda tup : tup[1].a)
        yList.append(y.mid)
        y, fY = L[0]
    yList.append(y.mid)
    return y, yList, L

# Function to calculate in interval means
def baeleInterval(x):
    return (1.5 - x[0] + x[0] * x[1]) ** 2 + (2.25 - x[0] + x[0] * x[1] * x[1]) ** 2 + (2.625 - x[0] + x[0] * x[1] * x[1] * x[1]) ** 2

def baele(x, y):
    return (1.5 - x + x * y) ** 2 + (2.25 - x + x * y * y) ** 2 + (2.625 - x + x * y * y * y) ** 2

# Function to calculate in interval means
def himmelblauInterval(x):
    return (x[0] * x[0] + x[1] - 11) * (x[0] * x[0] + x[1] - 11) + (x[0] + x[1] * x[1] - 7) * (x[0] + x[1] * x[1] - 7)

def himmelblau(x, y):
    return (x * x + y - 11) * (x * x + y - 11) + (x + y * y - 7) * (x + y * y - 7)


def plotGraph(func, x_int, y_int):
    x, y = np.mgrid[x_int[0]:x_int[1]:100j, y_int[0]:y_int[1]:100j]
    z = func(x, y)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap="viridis")
    plt.show()
    return

def task3():
    # For Baele
    mid = np.zeros(2)
    rad = np.ones(2) * 4
    yOpt, list, boxList = glob_opt(baeleInterval, 0.0001, ip.Interval(mid, rad, midRadQ=True))
    print("Opt point is", yOpt.mid)
    print("Function value", baeleInterval(yOpt))
    plotGraph(baele, [-4,4], [-4,4])

    x, y = np.mgrid[-4:4:100j, -4:4:100j]
    z = baele(x, y)
    fig, ax = plt.subplots()
    ax.contour(x, y, z, levels = 20)

    # plot boxes
    for interval in boxList:
        box = []
        box.append((interval[0].a[0], interval[0].a[1]))
        box.append((interval[0].a[0], interval[0].b[1]))
        box.append((interval[0].b[0], interval[0].b[1]))
        box.append((interval[0].b[0], interval[0].a[1]))
        box.append((interval[0].a[0], interval[0].a[1]))
        xs, ys = zip(*box)
        ax.plot(xs, ys, '-')
        intMid = interval[0].mid
        ax.plot(intMid[0], intMid[1], 'o')

    # For Himmelblau
    mid = np.zeros(2)
    rad = np.ones(2) * 4
    yOpt, list, boxList = glob_opt(himmelblauInterval, 0.0001, ip.Interval(mid, rad, midRadQ=True))
    print("Opt point is", yOpt.mid)
    print("Function value", himmelblauInterval(yOpt))
    plotGraph(himmelblau, [-4,4], [-4,4])
    x, y = np.mgrid[-4:4:100j, -4:4:100j]
    z = himmelblau(x, y)
    fig, ax = plt.subplots()
    ax.contour(x, y, z, levels = 20)

     # plot boxes
    for interval in boxList:
        box = []
        box.append((interval[0].a[0], interval[0].a[1]))
        box.append((interval[0].a[0], interval[0].b[1]))
        box.append((interval[0].b[0], interval[0].b[1]))
        box.append((interval[0].b[0], interval[0].a[1]))
        box.append((interval[0].a[0], interval[0].a[1]))
        xs, ys = zip(*box)
        ax.plot(xs, ys, '-')
        intMid = interval[0].mid
        ax.plot(intMid[0], intMid[1], 'o')

    plt.show()


if __name__ == "__main__":
    print("Task 1:")
    task1()
    print("Task 2:")
    task2(0.05)
    print("Task 3:")
    task3()
