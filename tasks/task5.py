# Готово

from .defs import *

theme = "Арифметикалык мисалдар 5-класс"


def ques_001():
    z = {}
    o = ""
    t = ""
    for i in range(4):
        a = randint(100000, 10000000)
        b = randint(100000, 10000000)
        t += "$$ {} + {}=?$$".format(a, b)
        o += "$$ {} $$".format(a + b)
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_002():
    z = {}
    o = ""
    t = ""
    for i in range(4):
        a = randint(100, 10000)
        b = randint(100, 1000)
        t += "$$ {} \\div {}=?$$".format(a * b, b)
        o += "$$ {} $$".format(a)
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_003():
    z = {}
    o = ""
    t = ""
    for i in range(4):
        a = generate(1000, 10000)
        b = generate(1000, 10000)
        c = generate(100, 1000)
        t += "$$ {}*({}+{})=?$$".format(c, a, b)
        o += "$$ {} $$".format(c * (a + b))
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_004():
    z = {}
    o = ""
    t = ""
    for i in range(4):
        a = generate(1000, 10000)
        b = generate(100, 1000)
        c = a * b
        d = generate(999, a - 1)
        t += "$$ {} \\div ({}-{})=?$$".format(c, a + d, d)
        o += "$$ {} $$".format(b)
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_005():
    z = {}
    t = ""
    o = ""
    for i in range(4):
        a = generate(1000, 10000)
        b = generate(1000, 10000)
        c = generate(100, 1000)
        t += "$${}*({}+{})=?$$".format(c, a, b)
        o += "$$ {} $$".format(c * (a + b))
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


za = [ques_001, ques_002, ques_003, ques_004, ques_005]
