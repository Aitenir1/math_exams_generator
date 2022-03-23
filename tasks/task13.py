# Готово

from .defs import *

theme = "Санды көбөйтүүчүлөргө ажыратуу"


def ques_001():
    a, b, c = generate3(2, 5)
    t = "{} кайсы сандарга бөлүнөт?".format(a * b * c)
    o = ""
    i = 2
    x = a * b * c
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            o += "{}, ".format(i)
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_002():
    a, b = generate2(2, 6)
    c, d = generate2(2, 6)
    while a * b == c * d:
        a, b = generate2(2, 10)
        c, d = generate2(2, 10)

    t = "ЭЧЖБ({}, {})+ЭКЖБ({}, {})".format(a * c, b * d, c * b, d * a)
    o = "{}".format(nod(a * c, d * b) + nok(c * b, d * a))
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_003():
    a, b = generate2(2, 10)
    t = "ЭКЖБ({}, {})".format(a, b)
    o = "{}".format(nok(a, b))
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


za = [ques_001, ques_002, ques_003]
