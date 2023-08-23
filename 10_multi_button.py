from tkinter import *
from tkinter import font
from functools import partial
import numpy as np

COLOR_BLACK = "#a1a09f"
COLOR_RED = "#d6380d"
COLOR_GREEN = "#0ceb6c"
# ------------------------------------------------------------
# bet_number = []
# ------------------------------------------------------------
number_of_buttons = 37
array_of_buttons = []
state_of_button = [False] * number_of_buttons # is_pressed == True
temp = np.arange(0, number_of_buttons)
text_of_buttons = [str(x) for x in temp]
color_of_buttons = [COLOR_GREEN,
                    COLOR_RED, COLOR_BLACK, COLOR_RED, COLOR_BLACK, COLOR_RED, COLOR_BLACK, COLOR_RED, COLOR_BLACK, COLOR_RED,
                    COLOR_BLACK, COLOR_BLACK, COLOR_RED, COLOR_BLACK, COLOR_RED, COLOR_BLACK, COLOR_RED, COLOR_BLACK, COLOR_RED,
                    COLOR_RED, COLOR_BLACK, COLOR_RED, COLOR_BLACK, COLOR_RED, COLOR_BLACK, COLOR_RED, COLOR_BLACK, COLOR_RED,
                    COLOR_BLACK, COLOR_BLACK, COLOR_RED, COLOR_BLACK, COLOR_RED, COLOR_BLACK, COLOR_RED, COLOR_BLACK, COLOR_RED]
button_coordinate = {0: (0, 0),
                     1: (2, 1), 2: (1, 1), 3: (0, 1), 4: (2, 2), 5: (1, 2), 6: (0, 2), 7: (2, 3), 8: (1, 3), 9: (0, 3),
                     10: (2, 5), 11: (1, 5), 12: (0, 5), 13: (2, 6), 14: (1, 6), 15: (0, 6), 16: (2, 7), 17: (1, 7), 18: (0, 7),
                     19: (2, 8), 20: (1, 8), 21: (0, 8), 22: (2, 9), 23: (1, 9), 24: (0, 9), 25: (2, 10), 26: (1, 10), 27: (0, 10),
                     28: (2, 11), 29: (1, 11), 30: (0, 11), 31: (2, 12), 32: (1, 12), 33: (0, 12), 34: (2, 13), 35: (1, 13), 36: (0, 13)
                     }
# ------------------------------------------------------------


def show(par):
    global state_of_button
    global bet_number
    state_of_button[par] = not state_of_button[par]
    if state_of_button[par]:
        array_of_buttons[par].config(relief=SUNKEN)
    else:
        array_of_buttons[par].config(relief=RAISED)

    # detect bet_number
    print(f"State of number {par} is {state_of_button[par]}")


def create_bet_buttons():
    for i in range(number_of_buttons):
        button = Button(frame, text=text_of_buttons[i], width=3, font=fontText, bg=color_of_buttons[i], fg="white", command=partial(show, i))
        if i == 0:
            button.grid(row=button_coordinate[i][0], column=button_coordinate[i][1], pady=5, padx=5, rowspan=3, sticky="nse")
        else:
            button.grid(row=button_coordinate[i][0], column=button_coordinate[i][1], pady=5, padx=5)
        array_of_buttons.append(button)


# ------------------------------------------------------------
window = Tk()
# window.attributes('-fullscreen', True)
window.geometry("{}x{}+{}+{}".format(1400, 480, 50, 50))
window.title("Station")
# ------------------------------------------------------------
fontText = font.Font(family="Arial", size=36)

frame = Frame(window, bg="#ceded2")
frame.pack(fill="x", padx=20, pady=20)
create_bet_buttons()

window.mainloop()

