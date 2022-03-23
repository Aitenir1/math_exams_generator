from math import *
from random import randint
import sys


def generate(n, k):
    listik = [i for i in range(n, k + 1) if i != 0]
    # result = []
    # for i in range()
    return listik[randint(0, len(listik) - 1)]


def generateWZ(n, k):
    listik = [i for i in range(n, k + 1) if i != 0]
    # result = []
    # for i in range()
    return listik[randint(0, len(listik) - 1)]


def generate3(n, k):
    r1, r2, r3 = 0, 0, 0
    listik = [i for i in range(n, k + 1) if i != 0]
    while r1 == r2 or r2 == r3 or r3 == r1:
        r1 = listik[randint(0, len(listik) - 1)]
        r2 = listik[randint(0, len(listik) - 1)]
        r3 = listik[randint(0, len(listik) - 1)]
    return r1, r2, r3


def generate2(n, k):
    r1, r2 = 0, 0
    listik = [i for i in range(n, k + 1) if i != 0]
    while abs(r1) == abs(r2):
        r1 = listik[randint(0, len(listik) - 1)]
        r2 = listik[randint(0, len(listik) - 1)]
    return r1, r2


def isNeg(k):
    if k > 0:
        k = '+{}'.format(k)
    return k


def square(a):
    result = ''

    sq = []

    nums = {}

    c = 1

    i = 2
    while a != 1:
        if a % i == 0:
            if i in nums:
                nums[i] += 1
                if nums[i] == 2:
                    c *= i
                    nums[i] = 0
            else:
                nums[i] = 1
            a /= i
        else:
            i += 1
    r2 = 1
    for i, j in nums.items():
        if j != 0:
            r2 *= i
    return c, r2


def drob(x, y):
    x = abs(x)
    y = abs(y)
    a = []
    b = []

    i = 2
    while x != 1:
        if x % i == 0:
            a.append(i)
            x /= i
        else:
            i += 1

    i = 2
    while y != 1:
        if y % i == 0:
            b.append(i)
            y /= i
        else:
            i += 1

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] != 0 and b[j] != 0:
                if a[i] == b[j]:
                    a[i] = 0
                    b[j] = 0

    r1 = 1
    r2 = 1
    for i in a:
        if i != 0:
            r1 *= i
    for j in b:
        if j != 0:
            r2 *= j
    return r1, r2


# print(drob(15, 25))

def nod(x, y):
    a = []
    b = []

    i = 2
    while x != 1:
        if x % i == 0:
            a.append(i)
            x /= i
        else:
            i += 1

    i = 2
    while y != 1:
        if y % i == 0:
            b.append(i)
            y /= i
        else:
            i += 1
    res = 1
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] != 0 and b[j] != 0:
                if a[i] == b[j]:
                    res *= a[i]
                    a[i] = 0
                    b[j] = 0

    return res


def nok(x, y):
    a = []
    b = []

    i = 2
    while x != 1:
        if x % i == 0:
            a.append(i)
            x /= i
        else:
            i += 1

    i = 2
    while y != 1:
        if y % i == 0:
            b.append(i)
            y /= i
        else:
            i += 1
    res = 1
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] != 0 and b[j] != 0:
                if a[i] == b[j]:
                    res *= a[i]
                    a[i] = 0
                    b[j] = 0

    for i in a:
        if i != 0:
            res *= i
    for j in b:
        if j != 0:
            res *= j
    return res


def generateName(c):
    names = ["Амир", "Осман", "Эрмек", "Абай", "Эрбол", "Искендер", "Аман", "Улук", "Арсен", "Абдрахман", "Мунара",
             "Саадат", "Айгерим", "Айпери", "Бермет", "Аяна", "Асель", "Бегимай", "Айбике", "Мээрим"]
    r = []
    for i in range(c):
        indexx = randint(0, 19)
        if names[indexx]:
            r.append(names[indexx])
            names[indexx] = False
    return r
