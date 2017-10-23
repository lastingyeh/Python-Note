import tkinter as tk

window = tk.Tk()
window.geometry('200x200')

# tk.Label(window, text='top').pack(side='top')
# tk.Label(window, text='bottom').pack(side='bottom')
# tk.Label(window, text='left').pack(side='left')
# tk.Label(window, text='right').pack(side='right')

# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=f'{i},{j}').grid(row=i, column=j, ipadx=10, ipady=10)

tk.Label(window, text='place').place(x=10, y=100, anchor='nw')

window.mainloop()
