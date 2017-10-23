import tkinter as tk
import pickle
import tkinter.messagebox


def sign_to(window, user_info):
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
            # as pwd != confirm pwd
            n_usr = user_info.get('name')
            n_p = user_info.get('pwd')
            n_pf = user_info.get('f_pwd')

            if n_p != n_pf:
                tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
            elif n_usr in exist_usr_info:
                tk.messagebox.showerror('Error', 'The user has already signed up!')
            else:
                exist_usr_info[n_usr] = n_p
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)

                tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
                window.destroy()
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb'):
            pass


def create_frm(window):
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_pwd = tk.StringVar()
    new_pwd_confirm = tk.StringVar()

    # UserName UI
    new_name.set('example@python.com')
    # UserName Label
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)
    # UserName entry
    tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)

    # Pwd UI
    # Pwd Label
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    # Pwd Entry
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)

    # Confirm Pwd UI
    # Confirm Pwd Label
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    # Confirm Pwd Entry
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)

    # Confirm Button UI
    tk.Button(window_sign_up, text='sign up', command=lambda: sign_to(window_sign_up,
                                                                      {'name': new_name.get(), 'pwd': new_pwd.get(),
                                                                       'f_pwd': new_pwd_confirm.get()})).place(x=150,
                                                                                                               y=130)
