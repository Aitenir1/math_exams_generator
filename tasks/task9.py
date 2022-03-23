from .defs import *

theme = "Теңдемелерди чыгаруу 9-класс"


def ques_001():
    x, y = generate2(-20, 20)

    z = {}
    z["vop"] = """$$
    \\begin{}cases{}
    x-y={} \\\\
    xy={}
    \\end{}cases{}
    $$ теңдемелер системасын чыгаргыла""".format("{", "}", x - y, x * y, "{", "}")
    z["otv"] = "{} <br> {}".format(x, y)
    z["ball"] = 1
    return z


def ques_002():
    x = randint(2, 10)
    y = randint(2, 10)
    aplusb = x + y
    aplusb2 = x ** 2 + y ** 2
    t = """
    $$ x+y = {},\\ x^2+y^2={},\\ x^3+y^3=?$$
    """.format(aplusb, aplusb2)
    ab = (aplusb ** 2 - aplusb2) / 2
    o = "  {}".format(x ** 3 + y ** 3)
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_003():
    x1, x2 = generate2(2, 20)
    c = x1 * x2
    b = -(x1 + x2)
    z = {}
    z["vop"] = "$$x{}\\sqrt x+{}=0$$".format(b, c)
    z["otv"] = "$$({}, {})$$".format(x1 ** 2, x2 ** 2)
    z["ball"] = 1
    return z


def ques_004():
    x1, x2 = generate2(-10, 10)
    c = x1 * x2
    b = -(x1 + x2)
    b = isNeg(b)
    c = isNeg(c)
    d = generate(-10, 10)
    o = "$$({}, {})$$".format(x1 - d, x2 - d)
    d = isNeg(d)
    z = {}
    z["vop"] = "$$(x{})^2{}(x{}){}=0$$".format(d, b, d, c)
    z["otv"] = o
    z["ball"] = 1
    return z


za = [ques_001, ques_002, ques_003, ques_004]
