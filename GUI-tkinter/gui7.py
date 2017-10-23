import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')


def move_it():
    canvas.move(rect, 0, 2)


# Canvas
canvas = tk.Canvas(window, bg='blue', height=100, width=200)
# PhotoImage
image_file = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)

# draw
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180)
rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)

canvas.pack()

# Button
btn = tk.Button(window, text='move', command=move_it).pack()

# start GUI
window.mainloop()