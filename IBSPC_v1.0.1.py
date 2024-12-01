import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import tkinter.messagebox

root = tk.Tk()
root.title("IBSPC")
root.geometry("270x450")

ttl = tk.Label(root, text="IBSPC: IB Score & Proportion Calculator")
ttl.pack(pady=20)

def create_input_field(y_position, label_text, is_percentage=False):
    label = tk.Label(root, text=label_text)
    label.place(x=10, y=y_position)

    entry = tk.Entry(root, width=10)
    if is_percentage:
        entry.place(x=170, y=y_position)
    else:
        entry.place(x=113, y=y_position)

    total_label = "/100(%)" if is_percentage else "/100"
    total_label_widget = tk.Label(root, text=total_label)
    total_label_widget.place(x=200, y=y_position)

    return entry

mononesc = create_input_field(50, "Monthly 1")
midtsc = create_input_field(80, "Mid-term")
monthreesc = create_input_field(110, "Monthly 3")
otfsc = create_input_field(140, "Other Factors")

mononepsc = create_input_field(170, "Monthly 1 Proportion", is_percentage=True)
midtpsc = create_input_field(200, "Mid-term Proportion", is_percentage=True)
monthreepsc = create_input_field(230, "Monthly 3 Proportion", is_percentage=True)
otfpsc = create_input_field(260, "Other Factors Proportion", is_percentage=True)

exp_y = 290
expla = tk.Label(root, text="IB Score")
expla.place(x=10, y=exp_y)
exp = ttk.Combobox(root, width=8, textvariable=tk.StringVar())
exp.place(x=100, y=exp_y)
exp['value'] = ('4', '5', '6', '7')[::-1]
exp.current(0)

bdy_y = 320
bdysc = tk.Entry(root, width=10)
bdysc.place(x=113, y=bdy_y)
bdyla = tk.Label(root, text="Boundary")
bdyla.place(x=10, y=bdy_y)
totalbdy = tk.Label(root, text="/100")
totalbdy.place(x=160, y=bdy_y)

def calculate():
    try:
        score1 = float(mononesc.get())
        score2 = float(midtsc.get())
        score3 = float(monthreesc.get())
        score4 = float(otfsc.get())
        proportion1 = float(mononepsc.get()) / 100
        proportion2 = float(midtpsc.get()) / 100
        proportion3 = float(monthreepsc.get()) / 100
        proportion4 = float(otfpsc.get()) / 100
        bdy = float(bdysc.get())
        exps = exp.get()
    except ValueError as e:
        tkinter.messagebox.showerror("TypeError", f"Error occurs while calculating, quit with: {e}")
        return

    minimum = (bdy - score1 * proportion1 - score2 * proportion2 - score3 * proportion3 - score4 * proportion4) / (1 - proportion1 - proportion2 - proportion3 - proportion4)
    minimum = int(minimum) + 1
    maximum = 100 * (1 - proportion1 - proportion2 - proportion3 - proportion4) + score1 * proportion1 + score2 * proportion2 + score3 * proportion3 + score4 * proportion4
    maximum = int(maximum) + 1
    younb = score1 * proportion1 + score2 * proportion2 + score3 * proportion3 + score4 * proportion4
    younb = int(younb) + 1

    if minimum <= 100 and minimum >= 0:
        tkinter.messagebox.showinfo("Result", f"To reach IB Score {exps}, the score of the final exam must at least reach \n {minimum}")
    elif minimum >= 100:
        tkinter.messagebox.showerror("Result", f"You have no chance to reach {exps}, the maximum score you can reach is {maximum}!")
    else:
        tkinter.messagebox.showinfo("Result", f"Even if you get 0/100, your score is {younb}. ")

conf = tk.Button(root, text="Calculate the Range for Final exam", command=calculate)
conf.place(x=30, y=370)

auth = tk.Label(root, text="@0x14C6")
auth.place(x=210,y=420)
root.mainloop()