import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

lab = tk.Label(window, text='', bg='yellow')
lab.pack()
counter = 0


def do_job():
    global counter
    lab.config(text='do ' + str(counter))
    counter += 1


menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=do_job)
file_menu.add_command(label='Open', command=do_job)
file_menu.add_command(label='Save', command=do_job)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=window.quit)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command=do_job)
edit_menu.add_command(label='Copy', command=do_job)
edit_menu.add_command(label='Paste', command=do_job)

sub_menu = tk.Menu(file_menu)
file_menu.add_cascade(label='Import', menu=sub_menu, underline=0)
sub_menu.add_command(label="Submenu1", command=do_job)

window.config(menu=menu_bar)

window.mainloop()