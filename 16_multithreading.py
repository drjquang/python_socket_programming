# Date: Wed, 23/08/22023
# Desc: Multithreading tkinter

import tkinter as tk
from tkinter import ttk
from time import sleep
from threading import Thread
from queue import Queue
from enum import Enum, auto


class TicketPurpose(Enum):
    UPDATE_PROGRESS_TEXT = auto()


class Ticket:
    def __init__(self, ticket_type: TicketPurpose, ticket_value: str):
        self.ticket_type = ticket_type
        self.ticket_value = ticket_value


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("640x240")
        self.title("Tkinter multithreading")

        self.queue_message = Queue()

        self.create_frame_buttons().pack(fill="x", expand=True)

        self.bind("<<CheckQueue>>", self.check_queue)

    def check_queue(self, event):
        """ Check queue, pull out data and set label text """
        msg: Ticket
        msg = self.queue_message.get()
        if msg.ticket_type == TicketPurpose.UPDATE_PROGRESS_TEXT:
            self.lbl_status.configure(text=msg.ticket_value)

    def create_frame_buttons(self) -> ttk.Frame:
        """ Create and return a frame that contains widgets """
        self.frame_buttons = ttk.Frame(self, height=100)
        self.btn_download = ttk.Button(self.frame_buttons, text="Download", command=self.on_download_button_clicked)
        self.btn_test = ttk.Button(self.frame_buttons, text="Test", command=self.on_test_button_clicked)
        self.lbl_status = ttk.Label(self.frame_buttons, background="white", anchor="center")

        self.btn_download.pack(fill='x', expand=True, padx=10, pady=10)
        self.btn_test.pack(fill='x', expand=True, padx=10, pady=10)
        self.lbl_status.pack(fill='x', expand=True, padx=10, pady=10)

        return self.frame_buttons

    def on_test_button_clicked(self):
        print("Test button pressed")

    def on_download_button_clicked(self):
        new_thread = Thread(target=self.download, args=("sky.jpg", ), daemon=True)
        new_thread.start()

    def download(self, file_name: str):
        """ Download is now on a separated thread """
        for progress in range(1, 21):
            print(progress)
            ticket = Ticket(ticket_type=TicketPurpose.UPDATE_PROGRESS_TEXT,
                            ticket_value=f"Downloading {file_name} ... {progress*5}%")
            self.queue_message.put(ticket)
            self.event_generate("<<CheckQueue>>")
            sleep(1)
        finished_ticket = Ticket(ticket_type=TicketPurpose.UPDATE_PROGRESS_TEXT,
                                 ticket_value="DOWNLOAD COMPLETED")
        self.queue_message.put(finished_ticket)
        self.event_generate("<<CheckQueue>>")

if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
