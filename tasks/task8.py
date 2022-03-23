from random import *
from .defs import *

theme = "Бөлчөктөр 5-класс"


def ques_001():
    b = generate(3, 30)
    a = generate(2, 30) * 100
    k = generate(2, b - 1)
    while b % k == 0 or b <= k:
        k = generate(1, 9)
    t = "$$ {}\ санынын \ \\frac {}{}{}{}{}{}\ бөлүгүн\ тапкыла$$".format(a * b, "{", k, "}", "{", b, "}")
    o = "{}".format(a * k)
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_002():
    t = "$$ "
    o = "$$ "
    for i in range(4):
        alym, bolum = generate2(2, 20)
        k = generate(2, 20)
        t += "\\frac {}{}{}{}{}{}, ".format("{", alym * k, "}", "{", bolum * k, "}")
        if alym % bolum == 0:
            o += "{}, ".format(alym // bolum)
        else:
            a, b = drob(alym, bolum)
            o += "\\frac {}{}{}{}{}{}, ".format("{", a, "}", "{", b, "}")
    t = t[:-2] + t[-1:]
    o = o[:-2] + o[-1:]
    o += " $$"
    t += " - бөлчөктөрдү\ кыскарткыла"
    t += " $$"
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_003():
    a = generate(10, 50)
    b = generate(10, 20)
    c = generate(2, 5)
    d = generate(3, 12)
    t = """Мектепте {} окуучу окуйт. {}и мектепке келген.
    Окуучулардын канча бөлүгү мектепке келген жок?""".format(a * b * c, d * b)
    x, y = drob(a * c, d)
    o = "\\( \\frac {}{}{}{}{}{}\\)".format("{", y, "}", "{", x, "}")
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


za = [ques_001, ques_002, ques_003]
