from .defs import *

theme = "Ылдамдыкты табуу маселелери 5-класс"


def ques_001():
    v = generate(1, 100)
    t = generate(1, 10)

    z = {}
    z["vop"] = """Эгерде страус {}км/c ылдамдык менен {} саат чуркаса, анда ал
    кандай аралыкты басып өткөн болот?""".format(v, t)
    z["otv"] = v * t
    z["ball"] = 1

    return z


def ques_002():
    v = generate(10, 200)
    t = generate(1, 20)
    s = v * t
    t = "Машина {} саатта {}км жол басып өттү. Машинанын ылдамдыгы канча?".format(t, s)
    o = "{}".format(v)
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


za = [ques_001, ques_002]
