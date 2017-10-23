import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')


def hit_me():
    tk.messagebox.showinfo(title='Hi', message='info')
    tk.messagebox.showwarning(title='Hi', message='warning')
    tk.messagebox.showerror(title='Hi', message='error')

    print(tk.messagebox.askquestion(title='Hi', message='ask-question'))
    print(tk.messagebox.askyesno(title='Hi', message='ask-yesno'))

    print(tk.messagebox.askretrycancel(title='Hi',message='ask-retrycancel'))
    print(tk.messagebox.askokcancel(title='Hi',message='ask-ok/c'))
    print(tk.messagebox.askyesnocancel(title='Hi',message='ask-yesnocancel'))

    window.quit()


tk.Button(window, text='hit me', command=hit_me).pack()

window.mainloop()
