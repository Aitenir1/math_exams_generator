#from less_set import *

# from tasks.queq import *
from stock import *
import webbrowser
import os

def create(count, option):
    for j in allTasks:
        themeCreate = j['theme']
        if themeCreate == option:
            zadan = j['content']
            break
    s0 = """ <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <script type="text/javascript"
        src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
        </script>
        <link rel="stylesheet" href="style.css">
        <title>Test</title>

    </head>
    <body>
    """
    s2 = """</body>
    </html> """
    def teg(a,b,c=""):
        t = "<{aa} {cc} {dd}> {bb} </{aa}>".format(aa=a, bb=b, cc=c, dd="width=\"max\"")
        return t

    def tega(a,c,b):
        t = "<{aa} {cc} > {bb} </{aa}>".format(aa=a,bb=b,cc=c)
        return t


    f = open("index.html", "w", encoding="utf-8")
    f.write(s0)

    k = []
    for i in range(count):
        k.append(list())
        k[i].append(str(i+1))
        f.write("<center>Алыкул Осмонов атындагы №68 МГОТК</center>\
        <center><B>Сабак:</B> Математика</center>\
        <center><B>Мугалим:</B> ___________ </center>")
        f.write("<center><B>Тема:</B> Функциялар </center>")
        f.write("<br>")
        f.write("<B>Вариант №{}</B>".format(i+1))
        f.write("<br><B>Класс ______</B>")
        f.write("<br><b>ФИО: ____________________________________________</b>")
        f.write("<br>")
        f.write("<table border=\"1px\" border-collapse=\"collapse\">")
        for j in range(len(zadan)):
            z = zadan[j]()
            f.write("<tr height=\"150px\" valign=\"top\">")
            f.write("<td align=\"center\" width=\"800px\" class=\"z\">{}</td>".format(z["vop"]))
            f.write(tega("td","width=\"300px\"",""))
            k[i].append(z["otv"])
    #        f.write(tega("td","width=\"300px\"  align=\"right\"",z["otv"]))
            f.write("</tr>")
        f.write("</table>")
        f.write("<div style=\"page-break-before:always;\"></div>")
    answers = []
    if count%5 == 0:
        g = count//5
    else:
        g = count//5+1
    for i in range(g):
        f.write("<table border=\"1px\" border-collapse=\"collapse\">")
        if i != count//5:
            f.write("<tr height=\"150px\" valign=\"top\">")
            for j in range(5):
                f.write("<td width=\"300px\" class=\"z\" align=\"center\">{}</td>".format(i*5+j+1))
                # f.write("")
            f.write("<tr/>")
            for j in range(1, len(zadan)+1):
                f.write("<tr height=\"150px\" valign=\"top\">")
                for n in range(5):
                    f.write("<td width=\"300px\" class=\"z\" align=\"center\">{}</td>".format(k[i*5+n][j]))
                f.write("</tr>")
        else:
            f.write("<tr height=\"150px\" valign=\"top\">")
            for j in range(count%5):
                f.write("<td width=\"300px\" class=\"z\" align=\"center\">{}</td>".format(i*5+j+1))
                f.write("")
            f.write("<tr/>")

            for j in range(1, len(zadan)+1):
                f.write("<tr height=\"150px\" valign=\"top\">")
                for n in range(count%5):
                    f.write("<td width=\"300px\" class=\"z\" align=\"center\">{}</td>".format(k[i*5+n][j]))
                f.write("</tr>")

        # for j in range()
        f.write("</table>")
        f.write("<div style=\"page-break-before:always;\"></div>")
    f.write(s2)
    f.close()

    path = os.path.dirname(os.path.abspath(__file__))

    url = f'file://{path}/index.html'
    print(url)
    webbrowser.open(url)
    # webbrowser.get("chrome").open("")
