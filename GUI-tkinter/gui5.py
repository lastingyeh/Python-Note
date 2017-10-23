import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')


def print_selection(v):
    lab.config(text='you have selected ' + v)


# Label
lab = tk.Label(window, bg='yellow', width=20, text='empty')
lab.pack()

# Scale
scale = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2,
                 resolution=0.01, command=print_selection)
scale.pack()

# start GUI
window.mainloop()