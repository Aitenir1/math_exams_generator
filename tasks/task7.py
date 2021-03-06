from .defs import *
import matplotlib.pyplot as plt

theme = "Текст түрүндөгү маселелер 9-класс"


def ques_001():
    r1 = randint(5, 20)
    r2 = randint(1, r1 - 1)

    t = """
    N шаарынын мэри өз шаарында аянт салмай болду.
    Аянтча радиусу {}м айлана формасында болуш керек. Аянтчанын так ортосунда дагы айлана
    формасындагы фонтан болот. Эгерде аянтчанын фонтандан тышкары жерине чөп отургузуш керек болсо,
    канча \\(м^2\\) жерге топурак төгүш керек? Фонтандын радиусу {}м
    """.format(r1, r2)
    o = "{}\\(\pi\\)".format(r1 ** 2 - r2 ** 2)
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_002():
    r = randint(5, 20)
    h = randint(1, 10)
    t = randint(1, 59)
    z = {}
    z["vop"] = """
    Алыскы өлкөдө инженерлер машинанын жаңы түрүн курууга киришишти.
    Алардын оюу боюнча, ал машинанын бүт дөңгөлөктөрүнүн радиусу {}м болот.
    Эгерде бир дөңгөлөк 1 секундада {} айлануу жазаса, {} минутта ал машина
    канча метр жол басып өтөт?
    """.format(r, h, t)
    l = 2 * r
    z["otv"] = "{}\\(\pi\\)".format(l * 60 * t * h)
    z["ball"] = 1
    return z


def ques_003():
    name = generateName(1)[0]
    a, b, c = generate3(5, 15)
    a1 = randint(2, a - 1)
    b1 = randint(2, b - 1)
    c1 = randint(2, c - 1)
    z = {}
    z["vop"] = """
    {} гиганттардын дүкөнүнөн самын сатып алды.
    Ал самындын үч өлчөмү {}см, {}см жана {}см. Самынды n күн колдонгондон кийин жактары
    {}см, {}см, {}см болуп калды. Калган самын дагы бир күнгө жетет. n саны канчага барабар?
    """.format(name, a * a1, b * b1, c * c1, a1, b1, c1)
    z["otv"] = a * b * c
    z["ball"] = 1
    return z


za = [ques_001, ques_002, ques_003]
