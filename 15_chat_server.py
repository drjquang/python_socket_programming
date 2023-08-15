# Date: Tue, 15/08/2023
# Desc: Chat server, show how many clients connected and check client alive
# Info: using ttkbootstrap for more styling

import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
# Global variable -----------------------------------------------------------------------------------------------------
connected_client = []
is_server_started = False
col_data = [
    {"text": "No", "stretch": True},
    {"text": "Client", "stretch": True},
]

row_data = [
    ('1', '610'),
    ('2', '611'),
]
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

# Tableview
dt = Tableview(
    master=window,
    coldata=col_data,
    rowdata=row_data,
    paginated=True,
    searchable=True,
    bootstyle=PRIMARY,
    stripecolor=(colors.light, None),
)
dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)
window.mainloop()
