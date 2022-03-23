# Готово

from .defs import *

theme = "Текст түрүндөгү маселелер 6-класс"


def ques_001():
    names = generateName(2)
    name = names[0]
    name2 = names[1]

    nameY, name2Y = generate2(1, 20)
    k = generate(1, 50)
    t = """{} {} жашта болгондо {} {} жашта болчу.
    Азыр  {} {}да болсо, {} канчада? """.format(name, nameY, name2, name2Y, name, nameY + k, name2)
    o = "{}".format(name2Y + k)
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_002():
    k = generate(1, 9)
    b = generate(1, 20)
    a = generate(1, 29) * 10 * b
    name = generateName(1)[0]
    while b <= k:
        b = generate(1, 20)
    t = """{} {} бет китептин \\( \\frac {}{}{}{}\\) бөлүгүн окуп бүттү. Китепти бүтүрүш
    үчүн үчүн дагы канча бет калды?""".format(name, a, k, "{", b, "}")
    o = "{}".format(a - (a // b) * k)
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_003():
    name = generateName(1)[0]
    b = generate(10, 100) * 10
    d2, d3 = generate2(1, b // 5)
    m2 = b + d2
    m3 = b - d3
    t = """{} англис тилин окуп баштады. Биринчи 3 айдын ичинде {} сөз жаттады.
    Биринчи айда экинчи айга караганда {} сөзгө аз,
    бирок үчүнчү айга караганда {} көп сөз үйрөндү. Экинчи ай {} канча сөз жаттады?""".format(name, b + m2 + m3, d2, d3,
                                                                                              name)
    print(b, m2, m3, d2, d3)
    z = {}
    z["vop"] = t
    z["otv"] = m2
    z["ball"] = 1
    return z


za = [ques_001, ques_002, ques_003]
