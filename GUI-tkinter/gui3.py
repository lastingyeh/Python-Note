import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x400')

var1 = tk.StringVar()
var2 = tk.StringVar()


def print_selection():
    value = listBox.get(listBox.curselection())
    var1.set(value)


# Label
lab = tk.Label(window, bg='yellow', width=4, textvariable=var1)
lab.pack()

# Button1
btn = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
btn.pack()

# ListBox
var2.set((11, 22, 33, 44))
listBox = tk.Listbox(window, listvariable=var2)

list_items = [1, 2, 3, 4]

for item in list_items:
    listBox.insert('end', item)

listBox.insert(1, 'first')
listBox.insert(2, 'second')
listBox.delete(2)

listBox.pack()

# start GUI
window.mainloop()