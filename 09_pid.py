# Date: 30/07/2023
# PID: history, change and histogram

import matplotlib.pyplot as plt
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import font
import random
import numpy as np


def define_background_color(value):
    if value == 0:
        return "#0af043"
    elif value in red_number:
        return "#cc023b"
    else:
        return "#2e2125"


# ------------------------------------------------------------
number_of_label = 18
array_of_label = []
red_number = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
array_of_number = [None] * number_of_label
# ------------------------------------------------------------
number_count = [0] * 37
roulette_number = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23,
                   10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
roulette_label = [str(x) for x in roulette_number]
c = ['green', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black',
     'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black',
     'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black']
# ------------------------------------------------------------
barh_sample = 18
y_pos = np.arange(barh_sample)

barh_value = [0] * barh_sample
barh_stick = [roulette_number.index(x) for x in barh_value]
barh_string = [str(x) for x in barh_value]
barh_color = [define_background_color(x) for x in barh_value]
# ------------------------------------------------------------


def init_history():
    for i in range(number_of_label):
        if i == 0 or i == number_of_label-1:
            horizontal_margin = 10
        else:
            horizontal_margin = 10
        label = Label(frame, textvariable=array_of_text[i], width=2, font=fontText, bg="#0af043", fg="white")
        label.grid(row=0, column=i, pady=20, padx=horizontal_margin)
        array_of_label.append(label)


def plot_history(num):
    array_of_number.pop()
    array_of_number.insert(0, num)
    for i in range(number_of_label):
        if array_of_number[i] is not None:
            array_of_text[i].set(str(array_of_number[i]))
            array_of_label[i].config(bg=define_background_color(array_of_number[i]))
        else:
            return


def plot_change(num):
    a1.clear()
    # ----------------------------------------------------------
    barh_value.pop()
    barh_value.insert(0, num)
    barh_stick = [roulette_number.index(x) for x in barh_value]
    barh_string = [str(x) for x in barh_value]
    barh_color = [define_background_color(x) for x in barh_value]
    # ----------------------------------------------------------
    a1.barh(y_pos, barh_stick, color=barh_color)
    a1.set_yticks(y_pos, labels=barh_string)
    a1.set_xticks(np.arange(-1, 38))
    a1.invert_yaxis()
    canvas1.draw()


def plot_histogram(num):
    a2.clear()
    number_count[roulette_number.index(num)] += 1
    x = roulette_label
    y = number_count
    a2.set_xlim([-1, 37])
    a2.set_ylim([0, 12])
    a2.bar(x, y, color=c)
    canvas2.draw()


def plot():
    gen_num = random.randint(0, 36)
    plot_history(gen_num)
    plot_change(gen_num)
    plot_histogram(gen_num)
    return


# ------------------------------------------------------------
window = Tk()
window.attributes('-fullscreen', True)
# window.geometry("{}x{}+{}+{}".format(1980, 1080, 0, 0))
window.title("Roulette PID")
# ------------------------------------------------------------
fontText = font.Font(family="Arial", size=36)
array_of_text = [None] * number_of_label
for i in range(number_of_label):
    array_of_text[i] = StringVar()
    array_of_text[i].set('*')
# ------------------------------------------------------------
frame = Frame(window, bg="#ceded2")
frame.pack(fill="x", padx=20, pady=20)
init_history()
# ------------------------------------------------------------
f1 = Figure(figsize=(5, 2), dpi=100)
a1 = f1.add_subplot(111)
a1.set_xlim([-1, 37])
a1.set_ylim([0, barh_sample])
canvas1 = FigureCanvasTkAgg(f1)
canvas1.draw()
canvas1.get_tk_widget().pack(fill="both", expand=True, padx=20)


f2 = Figure(figsize=(5, 3), dpi=100)
a2 = f2.add_subplot(111)
a2.set_xlim([-1, 37])
a2.set_ylim([0, 12])
canvas2 = FigureCanvasTkAgg(f2)
canvas2.draw()
canvas2.get_tk_widget().pack(fill="both", expand=True, padx=20)

# button = Button(window, text="Generate", command=plot)
# button.pack(pady=20)

toolbar = NavigationToolbar2Tk(canvas2, window, pack_toolbar=False)
toolbar.update()
toolbar.pack(anchor="w", fill="x", padx=20)

# bind hotkey for button Generate
window.bind('<space>', lambda event: plot())
window.mainloop()
