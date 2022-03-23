# Готово

from math import *
from random import randint
from .defs import *

theme = "Квадраттык теңдемелер 9-класс"


def ques_001():
    a = generate(-10, 10)
    s = generate(2, 3)
    c = generate(0, 198)
    o1, o2, o3 = generate3(-10, 10)

    o = "{}<br> {}<br> {}".format((o1 ** s) * a + c, (o2 ** s) * a + c, (o3 ** s) * a + c)
    c = isNeg(c)

    t = "\\(f(x)={}x^{}{}\\) функциясынын \\(f({}),\ f({}),\ f({})\\) маанилерин тапкыла".format(a, s, c, o1, o2, o3)
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_002():
    x1, x2 = generate2(-10, 10)
    c = x1 * x2
    b = -(x1 + x2)
    b = isNeg(b)
    c = isNeg(c)
    t = "\\(f(x)=x^2{}x{}\\) функциясында \\(f(x)=0,\\) шарты аткарылгандагыдай \\(x\\)тин маанилерин тапкыла".format(b,
                                                                                                                      c)
    z = {}
    z["vop"] = t
    z["otv"] = "{} <br> {}".format(x1, x2)
    z["ball"] = 1
    return z


def ques_003():
    x1, x2 = generate2(1, 20)
    c = x1 * x2
    b = -(x1 + x2)
    b = isNeg(b)
    c = isNeg(c)
    z = {}
    t = "\\(f(x)=x^4{}x^2{}\\) функциясынын нөлдөрүн тапкыла".format(b, c)
    z["vop"] = t
    o = ""
    squares = [square(x1), square(x2)]
    for i in squares:
        p, k = i
        if p == 1 and k != 1:
            o += "\\(\sqrt{} {} {}\\) <br>".format('{', k, '}')
            o += "\\(-\sqrt{} {} {}\\) <br>".format('{', k, '}')
        elif p != 1 and k == 1:
            o += "{} <br>".format(p)
            o += "-{} <br>".format(p)
        elif p == 1 and k == 1:
            o += "1 <br>"
            o += "-1 <br>"
        else:
            o += "\\( {}\sqrt{} {} {} \\) <br>".format(p, '{', k, '}')
            o += "\\( -{}\sqrt{} {} {} \\) <br>".format(p, '{', k, '}')
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_004():
    x1, x2 = generate2(-10, 10)
    c = x1 * x2
    b = -(x1 + x2)
    b = isNeg(b)
    if c > 0:
        znak = "+"
    else:
        c = str(c)
        c = c.replace("-", "")
        znak = "-"
    t = "\\(f(x)=x{}{}\\frac {}{}{}{}\\) функциясында \\(f(x)=0,\\) шарты аткарылгандагыдай \\(x\\)тин маанилерин тапкыла".format(
        b, znak, "{", c, "}", 'x')
    z = {}
    z["vop"] = t
    z["otv"] = "{} <br> {}".format(x1, x2)
    z["ball"] = 1
    return z


def ques_005():
    x1, x2 = generate2(-20, 20)
    b = isNeg(-(x2 + x1))
    c = isNeg(x1 * x2)
    t = "Эгерде квадраттык теңдеменин тамырлары {} менен {}ке барабар болсо, ал теңдемени жаз".format(x1, x2)
    z = {}
    z["vop"] = t
    z["otv"] = "\\( x^2{}x{}=0\\)".format(b, c)
    z["ball"] = 1
    return z


za = [ques_001, ques_002, ques_003, ques_004, ques_005]
