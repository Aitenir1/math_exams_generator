from .defs import *

theme = "Функциянын графиктерин түзүү 9-класс"


def ques_001():
    x = generate(-100, 100)
    y = generate(-100, 100)
    r = generate(1, 11)
    t = """\\( (x-{})^2+(y-{})^2={} \\) берилген айлананын борборунун координаталарын
     жана радиусунун узундугун тапкыла""".format(x, y, r ** 2)
    z = {}
    z["vop"] = t
    z["otv"] = "$$ ({}, {}), r={} $$".format(x, y, r)
    z["ball"] = 1
    return z


def ques_002():
    x1, x2 = generate2(-10, 10)
    c = x1 * x2
    b = -(x1 + x2)
    o = "({}; {})".format(-b / 2, -(b ** 2 - 4 * c) / (4))
    b = isNeg(b)
    c = isNeg(c)
    t = """Эгерде парабола \\(f(x)=x^2{}x{}\\) функциясы менен берилсе чокусунун
            координаталарын аныктагыла""".format(b, c)

    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


za = [ques_001, ques_002]
