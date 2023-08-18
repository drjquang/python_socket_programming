# Date: Tue, 15/08/2023
# Desc: Chat server, show how many clients connected and check client alive
# Info: using ttkbootstrap for more styling

import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
# Global variable -----------------------------------------------------------------------------------------------------
connected_client = []
is_server_started = False


def item_selected(event):
    for selected_item in ConnectionTable.selection():
        item = ConnectionTable.item(selected_item)
        record = item['values']
        print(record)
# ---------------------------------------------------------------------------------------------------------------------


def run_server():
    global is_server_started
    is_server_started = not is_server_started
    if is_server_started:
        btn_start_text.set('Stop')
        lbl_status_text.set('Server is running.')
    else:
        btn_start_text.set('Start')
        lbl_status_text.set('Server is NOT running.')


window = ttk.Window(title="My Application", themename="superhero")
window.title("Chat server")
window.geometry("600x480")
colors = window.style.colors
# Declare widget variable
btn_start_text = ttk.StringVar()
lbl_status_text = ttk.StringVar()
if is_server_started:
    btn_start_text.set('Stop')
    lbl_status_text.set('Server is running.')
else:
    btn_start_text.set('Start')
    lbl_status_text.set('Server is NOT running.')

# Frame contains button and label show status
ConnectionFrame = ttk.Frame(master=window, bootstyle="info")
ConnectionFrame.pack(side='top', fill='x', expand=True, pady=10, padx=10)
start_button = ttk.Button(master=ConnectionFrame, textvariable=btn_start_text, bootstyle="success", command=run_server)
start_button.pack(side='left')
server_status = ttk.Label(master=ConnectionFrame, textvariable=lbl_status_text, anchor='center', bootstyle="danger")
server_status.pack(side='right', fill='x', expand=True, padx=10)

# Treeview
columns = ('no', 'IP', 'port')
ConnectionTable = ttk.Treeview(window, columns=columns, show='headings')
ConnectionTable.pack(fill=BOTH, expand=YES, padx=10, pady=10)
ConnectionTable.heading('no', text='no')
ConnectionTable.heading('IP', text='IP')
ConnectionTable.heading('port', text='port')
# ---------------------------------------------------------------------------------------------------------------------
ConnectionTable.insert('', ttk.END, values=('1', '127.0.0.1', '12345'))
ConnectionTable.insert('', ttk.END, values=('2', '127.0.0.1', '23456'))
ConnectionTable.insert('', ttk.END, values=('3', '127.0.0.1', '34567'))

# ---------------------------------------------------------------------------------------------------------------------
ConnectionTable.bind('<<TreeviewSelect>>', item_selected)

window.mainloop()
