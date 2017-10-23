import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')


def insert_point():
    var = entry.get()
    # cursor pos insert
    # text.insert('insert', var)
    # specify pos > line1. after sec letter pos
    text.insert(1.2, var)


def insert_end():
    var = entry.get()
    # end post insert
    text.insert('end', var)


# Entry
entry = tk.Entry(window, show=None)
entry.pack()

# Button1
btn1 = tk.Button(window, text='inset point', width=15, height=2, command=insert_point)
btn1.pack()

# Button2
btn2 = tk.Button(window, text='insert end', command=insert_end)
btn2.pack()

# Text
text = tk.Text(window, height=2)
text.pack()

# start GUI
window.mainloop()