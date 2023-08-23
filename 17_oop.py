import tkinter as tk
from tkinter import ttk


class UsernameWindow(tk.Toplevel):
    def __init__(self, master, username):
        super().__init__(master)
        self.username = username

        self.geometry("400x120+100+240")
        self.title("Top Window")

        self.frame_main = ttk.Frame(self)
        self.lbl_username = ttk.Label(self.frame_main,
                                      anchor="center",
                                      background="white",
                                      text=f"Name = {self.username}")

        self.frame_main.pack(fill=tk.BOTH, expand=True)
        self.lbl_username.pack(fill='x', padx=10, pady=10)


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.username = "CoolKid"

        self.geometry("400x120+100+100")
        self.title("Object oriented")

        self.frame_main = ttk.Frame(self)
        self.btn_show_username = ttk.Button(self.frame_main, text="Show username", command=self.show_username)

        self.frame_main.pack(fill=tk.BOTH, expand=True)
        self.btn_show_username.pack(fill='x', padx=10, pady=10)

    def show_username(self):
        username_window = UsernameWindow(self, username=self.username)


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
