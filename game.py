from tkinter import *
import random
import time


def cast():
    x = random.choice(['1.png', '2.png', '3.png',
                       '4.png', '5.png', '6.png'])
    return x


def img(event):
    global lab1_img, lab2_img
    for i in range(10):
        lab1_img = PhotoImage(file=cast())
        lab2_img = PhotoImage(file=cast())
        lab1['image'] = lab1_img
        lab2['image'] = lab2_img
        root.update()
        time.sleep(0.12)


root = Tk()
root.geometry('600x400')
root.title('Игра в кости. Сделай бросок!')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='icon2.png'))
font = PhotoImage(file='cholst.png')
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
root.bind('<1>', img)
img('event')
root.mainloop()
