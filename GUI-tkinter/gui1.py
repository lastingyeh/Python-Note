import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

var = tk.StringVar()
on_hit = False


# func
def hit_me():
    global on_hit
    if not on_hit:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')


# Label
lab = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)
lab.pack()

# Button
btn = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
btn.pack()


# start GUI
window.mainloop()