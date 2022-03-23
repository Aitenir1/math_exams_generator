from create_html import *
from tkinter import *
from stock import allTasks
import os



def button_click():
    index_option_tuple = themes_listbox.curselection()
    c = countForm.get()
    is_count_empty = False

    if len(index_option_tuple) == 0:
        errorLabel.pack()
    else:
        index_option = index_option_tuple[0]
        options = themes[int(index_option)]
        errorLabel.pack_forget()
        is_count_empty = True
    if c.isdigit():
        c = int(c)
        checkForNum.pack_forget()
        if is_count_empty:
            create(count=c, option=options)
    else:
        checkForNum.pack()


root = Tk()

root.title("Эсептер генератору")
root.geometry('600x500')
root.resizable(width=False, height=False)
# canvas = Canvas(root, height=300, width=250)
# canvas.pack()

frame = Frame(root,
              bg='#fafafa',
              pady=15)

frame.place(relx=0.15,
            rely=0.15,
            relwidth=0.7,
            relheight=0.7)

title = Label(frame,
              text='Вариантттардын санын киргизиңиз',
              font=("Courier", 11),
              bg='#fafafa',
              )
title.pack()

countForm = Entry(frame, bg='white')
countForm.pack()

frameListBox = Frame(frame, padx=10, pady=10, bg='#fafafa')
frameListBox.pack()
scrollbar = Scrollbar(frameListBox)
scrollbar.pack(side=RIGHT, fill=Y)

themes_listbox = Listbox(frameListBox, yscrollcommand=scrollbar.set, width=50)

btn = Button(frame, text='Басып чыгаруу', command=button_click, padx=10, pady=5, font=10)
btn.pack()

errorLabel = Label(frame, pady=4,
                   text="Жогорудагы вариантттардын бирин тандаңыз",
                   font=("Courier", 11),
                   fg='red',
                   bg='#fafafa')
errorLabel.pack_forget()

checkForNum = Label(frame, pady=2,
                   text="Биринчи талаага 1ден 100гө чейинки эле сандарды киргизсе болот",
                   font=("Courier", 8),
                   fg='red',
                   bg='#fafafa')
checkForNum.pack_forget()

themes = []

for i in allTasks:
    if i['theme'] not in themes:
        themes.append(i['theme'])
        themes_listbox.insert(END, i['theme'])


themes_listbox.pack()
root.mainloop()
