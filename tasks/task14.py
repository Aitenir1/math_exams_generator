from .defs import *

theme = "Кыскача көбөтүүнүн формулалар 9-класс"


def ques_001():
    a = generate(1, 15)
    s = generate(1, 30)
    z = {}
    z["vop"] = "Көбөйтүүчүлөргө ажыраткыла "
    z["vop"] += "$$a^{\\frac{1}{" + str(s) + "}}-{" + str(a ** 2) + "}$$"
    z["otv"] = "\\((a^{\\frac{1}{" + str(s * 2) + "}}-{" + str(a) + "})(a^{\\frac{1}{" + str(s * 2) + "}}+{" + str(
        a) + "})\\)"
    z["ball"] = 1
    return z


def ques_002():
    x1, x2 = generate2(1, 20)
    c = x1 * x2
    b = -(x1 + x2)
    z = {}
    z["vop"] = "Көбөйтүүчүлөргө ажыраткыла  <br>"
    z["vop"] += "$$x^2{}x+{}$$".format(b, c)
    z["otv"] = "$$(x-{})(x-{})$$".format(x1, x2)
    z["ball"] = 1
    return z


def ques_003():
    x = randint(2, 10)
    y = randint(2, 10)
    aplusb = x + y
    aplusb2 = x ** 2 + y ** 2
    t = """
    $$ x+y = {},\\ x^2+y^2={},\\ x^3+y^3=?$$
    """.format(aplusb, aplusb2)
    ab = (aplusb ** 2 - aplusb2) / 2
    o = "{}".format(aplusb * (aplusb2 - ab))
    o += "  {}".format(x ** 3 + y ** 3)
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


za = [ques_001, ques_002]
