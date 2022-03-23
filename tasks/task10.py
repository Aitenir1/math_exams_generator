from .defs import *

theme = "Прогрессиялар 9-класс"


def ques_001():
    a = generate(0, 20)
    an = generate(1, 9)
    d = generate(-20, 20)
    n = generate(10, 100)
    a1 = a - (an - 1) * d
    t = "Арифметикалык прогрессияда \\( a_{}={}, d={}\\) болсо $$ a_{}{}{}=?$$".format(an, a, d, "{", n, "}")
    o = "{}".format(a1 + (n - 1) * d)
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_002():
    a = generate(5, 59)

    t = "Биринчи {} натуралдык сандардын суммасын тапкыла ({} дагы кошулганда)".format(a, a)
    o = ((1 + a) * (a / 2))
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_003():
    a1 = generate(-10, 10)
    d = generate(-10, 10)
    c = generate(4, 50)
    t = "\\( a_{}={}, a_{}={}, a_{}{}{}=?\\)".format(1, a1, 2, a1 + d, "{", c, "}")
    for i in range(c - 1):
        a1 += d
    z = {}
    z["vop"] = t
    z["otv"] = a1
    z["ball"] = 1
    return z


def ques_004():
    b1 = generate(1, 10)
    q = generate(2, 10)
    c = generate(2, 10)
    t = "\\(b_{}={}, q={}, b_{}=?\\)".format(1, b1, q, c)
    o = b1 * (q ** (c - 1))
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


za = [ques_001, ques_002, ques_003, ques_004]
