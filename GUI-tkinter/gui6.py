import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.IntVar()
var2 = tk.IntVar()


def print_selection():
    if (var1.get() == 1) and (var2.get() == 0):
        lab.config(text='I love only Python ')
    elif (var1.get() == 0) and (var2.get() == 1):
        lab.config(text='I love only C++ ')
    elif (var1.get() == 0) and (var2.get() == 0):
        lab.config(text='I don\'t love either')
    else:
        lab.config(text='I love both')


# Label
lab = tk.Label(window, bg='yellow', width=20, text='empty')
lab.pack()

# Checkbutton
chk1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
chk2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)

chk1.pack()
chk2.pack()

# start GUI
window.mainloop()