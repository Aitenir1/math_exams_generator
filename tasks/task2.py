from .defs import *

theme = "Функциянын аныкталуу областын табуу 9-класс"


def ques_001():
    x1, x2 = generate2(-10, 10)
    c = x1 * x2
    b = -(x1 + x2)

    o = "$$ x \\in (-\\infty, {}) \\cup ({}, \\infty) $$".format(min(x1, x2), max(x1, x2))

    b = isNeg(b)
    c = isNeg(c)
    alym = generate(-100, 100)

    t = "\\(f(x)=\\frac {}{}{}{} \\sqrt{}x^2{}x{} {}{} \\) функциясынын аныкталуу областын тапкыла".format("{", alym,
                                                                                                           "}", "{",
                                                                                                           "{", b, c,
                                                                                                           "}", "}")

    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_002():
    a = generate(-10, 10)
    b = isNeg(generate(-100, 100))
    c = generate(1, 10)
    d = generate(-100, 100)

    t = "\\( f(x)=\\frac {}{}x{}{}{}{}x{}{}\\) функциясынын аныкталуу областын тапкыла".format("{", a, b, "}", "{", c,
                                                                                               isNeg(d), "}")

    if abs(d % c) == 0:
        o = "\\(x \\in (-\\infty, {}) \\cup ({}, \\infty) \\)".format(-d // c, -d // c)
    else:
        al, bol = drob(c, d)
        k = "frac {}{}{}{}{}{}".format("{", al, "}", "{", bol, "}")
        if -d // c > 0:
            o = "\\( x \\in (-\\infty, \\{}) \\cup (\\{}, \\infty) \\)".format(k, k)
        else:
            o = "\\( x \\in (-\\infty, -\\{}) \\cup (-\\{}, \\infty) \\)".format(k, k)
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_003():
    x1, x2 = generate2(-10, 10)
    c = -x1 * x2
    b = x1 + x2

    o = "$$ x \\in ({}, {})$$".format(min(x1, x2), max(x1, x2))

    b = isNeg(b)
    c = isNeg(c)
    alym = generate(-100, 100)

    t = "\\(f(x)=\\frac {}{}{}{} \\sqrt{}-x^2{}x{} {}{} \\) функциясынын аныкталуу областын тапкыла".format("{", alym,
                                                                                                            "}", "{",
                                                                                                            "{", b, c,
                                                                                                            "}", "}")

    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


za = [ques_001, ques_002, ques_003]
