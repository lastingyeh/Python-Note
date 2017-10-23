import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x400')

var = tk.StringVar()


def print_selection():
    lab.config(text='you have selected ' + var.get())


# Label
lab = tk.Label(window, bg='yellow', width=20, text='empty')
lab.pack()

# RadioButton
rBtn1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
rBtn1.pack()

rBtn2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
rBtn2.pack()

rBtn3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
rBtn3.pack()

# start GUI
window.mainloop()