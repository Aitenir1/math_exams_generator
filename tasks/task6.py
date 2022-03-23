# Готово

from .defs import *
import matplotlib.pyplot as plt

theme = "Геометриялык маселелер 9-класс"


def ques_001():
    ad, ab = generate2(5, 20)
    af = generate(1, ad - 1)
    ae = generate(1, ab - 1)
    eb = ab - ae
    fd = ad - af
    plt.plot([0, ab, ab, 0, 0], [0, 0, ad, ad, 0])
    plt.plot([0, ab, ae, 0, 0], [af, ad, 0, 0, af])
    plt.text(-0.5, -0.5, 'A', fontsize=20)
    plt.text(ae, -0.7, 'E', fontsize=20)
    plt.text(ab, 0, 'B', fontsize=20)
    plt.text(ab, ad, 'C', fontsize=20)
    plt.text(0, ad + 0.3, 'D', fontsize=20)
    plt.text(-0.5, af, 'F', fontsize=20)
    plt.axis("off")
    name = "{}{}{}{}.png".format(randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000))
    plt.savefig(name)
    plt.close()
    o = ad * ab - ad * eb / 2 - ab * fd / 2
    if int(o) == o:
        o = int(o)
    t = """\\( ABCD \\) тик бурчтук берилди.
    \\( E \\) чекити \\(AB\\) жагында, \\(F AD\\) жагында жатат.
    \\( AB={}см,\ AD={}см,\ AE={}см,\ AF={}см,\
      S_{}AECF{}=? \\) <img src=\"{}\" height=150>""".format(ab, ad, ae, af, "{", "}", name)
    z = {}
    z["vop"] = t
    z["otv"] = o
    z["ball"] = 1
    return z


def ques_002():
    x1 = generate(0, 10)
    x2 = generate(x1 + 1, 20)
    y1 = generate(0, 10)
    y2 = generate(y1 + 1, 20)
    ex = generate(x1, x2)
    fy = generate(y1, y2)
    plt.plot([x1, ex, x2, x1], [y1, y2, fy, y1])
    s = (y2 - y1) * (x2 - x1) - ((x2 - x1) * (fy - y1) / 2 + (y2 - fy) * (x2 - ex) / 2 + (ex - x1) * (y2 - y1) / 2)
    # print("x1={} x2={} y1={} y2={} ex={} fy={} s={}".format(x1,x2,y1,y2,ex,fy,s))
    # plt.axis("off")
    name = "{}{}{}{}.png".format(randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000))
    plt.savefig(name)
    plt.close()
    z = {}
    z["vop"] = """<div class=\"vop\"><span>Берилген фигуранын аянтын тапкыла</span>
   <img src=\"{}\" height=150> </div>""".format(name)
    z["otv"] = s
    z["ball"] = 1
    return z


def ques_003():
    ab = randint(5, 100)
    k = randint(5, 100)
    bc = randint(5, 100)
    z = {}
    z["vop"] = "\\(ABC \sim A'B'C',\ AB={}см,\ A'B'={}см,\ BC={}см,\ B'C'=?\\) ".format(ab, ab * k, bc)
    z["otv"] = bc * k
    z["ball"] = 1
    return z


def ques_004():
    delta = randint(2, 10)
    ab = randint(2, 10)
    cd = ab + delta * 2
    h = randint(3, 20)
    # print(h**2, d**2)
    c, k = square(h ** 2 + delta ** 2)
    name = "{}{}{}{}.png".format(randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000))
    plt.plot([0, cd, cd - delta, delta, 0], [0, 0, h, h, 0])
    plt.axis('off')
    plt.savefig(name)
    plt.close()
    sq = ""
    if c == 1:
        sq += "\\( \sqrt{}{}{} \\)".format("{", k, "}")
    elif k == 1:
        sq += "{}".format(c)
    else:
        sq += "\\( {}\sqrt{}{}{} \\)".format(c, "{", k, "}")
    z = {}
    z["vop"] = """<div class=\"vop\"><span>
  Трапециянын негиздери {} жана {}см. Капталы {}см болсо, аянты канча?
  </span> <img src=\"{}\" height=150> </div> """.format(ab, cd, sq, name)
    z["otv"] = ((ab + cd) / 2) * h
    z["ball"] = 1
    return z


za = [ques_001, ques_002, ques_003, ques_004]
