from tkinter import Toplevel, Label, Button, Entry, PhotoImage, messagebox
import os
import sqlite3

path = os.getcwd()

img_icon = f'{path}/Icon/icon-user.ico'
img_logo = f'{path}/Img/img-logo.png'
img_view_password = f"{path}/Img/img-view-password.png"
img_not_view_password = f"{path}/Img/img-not-view-password.png"
databases = f'{path}/Database/users_passwords.db'


def login_function(win):
    win.destroy()
    from Log.log_in import windows, LogIn
    windows.deiconify()
    LogIn()


def register_user_password(username, password, user_entry, pass_entry, win):
    connect = sqlite3.connect(
        databases
    )

    cursor = connect.cursor()

    cursor.execute(
        'SELECT * FROM user_password WHERE Username = ? AND Password = ?', (
            username, password
        )
    )

    result = cursor.fetchall()

    if username == '':
        messagebox.showerror(
            'Error', 'The Username its incorrect'
        )

    elif password == '':
        messagebox.showerror(
            'Error', 'The Password its incorrect'
        )

    elif result:
        messagebox.showerror(
            'Error', 'You account exiting int databases. Please init session'
        )
        user_entry.delete(
            0,
            'end'
        )
        pass_entry.delete(
            0,
            "end"
        )

        login_function(win)
    else:
        messagebox.showinfo(
            'Congratulations', f"The account [{username}] create it's congratulations"
        )
        cursor.execute(
            f"INSERT INTO user_password VALUES ('{username}','{password}')"
        )
        connect.commit()
        cursor.close()
        user_entry.delete(
            0,
            'end'
        )
        pass_entry.delete(
            0,
            "end"
        )
        login_function(win)


def register(Username, Password):
    class Register:
        def __init__(self):

            self.windows = Toplevel()

            self.windows.geometry(
                '900x650+525+200'
            )
            self.windows.title(
                'Register'
            )
            self.windows.iconbitmap(
                img_icon
            )
            self.windows.resizable(
                False,
                False
            )
            self.windows.config(
                background='#252525'
            )

            right_panel = Label(
                self.windows,
                background='#294c60'
            )

            right_panel.place(
                width=350,
                height=650,
                x=550,
                y=0
            )

            logo_img = PhotoImage(
                file=img_logo
            )

            logo = Label(
                self.windows,
                image=logo_img,
                background='#294c60'
            )

            logo.place(
                x=600,
                y=70
            )

            register_txt = Label(
                self.windows,
                text='REGISTER',
                background='#252525',
                foreground='white',
                font=(
                    'Arial Black', 35
                )
            )

            register_txt.place(
                x=140,
                y=25
            )

            username_txt = Label(
                self.windows,
                text='Username',
                background='#252525',
                foreground='white',
                font=(
                    'Arial Black', 18
                )
            )

            username_txt.place(
                x=40,
                y=120
            )

            username_entry = Entry(
                self.windows,
                textvariable=Username,
                background='#6f95aa',
                font=(
                    'Arial', 16
                ),
                border=0,
                justify='center'
            )

            username_entry.place(
                width=470,
                height=40,
                x=40,
                y=190
            )

            username_entry.delete(
                0,
                'end'
            )

            password_txt = Label(
                self.windows,
                text='Password',
                background='#252525',
                foreground='white',
                font=(
                    'Arial Black', 18
                )
            )

            password_txt.place(
                x=40,
                y=260
            )

            password_label = Label(
                self.windows,
                background='#6f95aa'
            )

            password_label.place(
                width=470,
                height=40,
                x=40,
                y=330
            )

            password_entry = Entry(
                self.windows,
                textvariable=Password,
                background='#6f95aa',
                font=(
                    'Arial', 16
                ),
                border=0,
                justify='center',
                show=(
                    '*'
                )
            )

            password_entry.place(
                width=430,
                height=40,
                x=40,
                y=330
            )

            password_entry.delete(
                0,
                'end'
            )

            not_view_img = PhotoImage(
                file=img_not_view_password
            )

            not_view_password_bt = Button(
                self.windows,
                image=not_view_img,
                border=0,
                cursor='hand2',
                background='#6f95aa',
                activebackground='#6f95aa',
                command=lambda: [
                    {
                        self.view_password(
                            info_password=password_entry,
                            view_password_img=not_view_img,
                            button=not_view_password_bt
                        )
                    }
                ]
            )

            not_view_password_bt.place(
                x=473,
                y=333
            )

            button_register = Button(
                self.windows,
                text='REGISTER',
                background="grey",
                foreground='#252525',
                font=(
                    'Arial Black', 18
                ),
                border=0,
                cursor='hand2',
                activebackground='white',
                command=lambda: register_user_password(
                    Username.get(), Password.get(), user_entry=username_entry, pass_entry=password_entry, win=self.windows
                )
            )

            button_register.place(
                width=390,
                height=50,
                x=80,
                y=430
            )

            button_login = Button(
                self.windows,
                text='LOG IN',
                background="white",
                foreground='#252525',
                font=(
                    'Arial Black', 18
                ),
                border=0,
                cursor='hand2',
                activebackground='grey',
                command=lambda: [
                    {
                        login_function(win=self.windows)
                    }
                ]
            )

            button_login.place(
                width=390,
                height=50,
                x=80,
                y=540
            )
            self.windows.bind(
                '<Return>', lambda event: register_user_password(
                    Username.get(), Password.get(), user_entry=username_entry, pass_entry=password_entry, win=self.windows
                )
            )

            self.windows.mainloop()

        def view_password(self, info_password, view_password_img, button):
            info_password.config(
                show=(
                    ''
                )
            )

            view_password_img.config(
                file=img_view_password
            )

            button.config(
                command=lambda: [
                    {
                        self.not_view_password(
                            info_password_not_view=info_password, not_view_password_img=view_password_img,
                            button_not_view=button
                        )
                    }
                ]
            )

        def not_view_password(self, info_password_not_view, not_view_password_img, button_not_view):
            info_password_not_view.config(
                show=(
                    '*'
                )
            )

            not_view_password_img.config(
                file=img_not_view_password,

            )

            button_not_view.config(
                command=lambda: [
                    {
                        self.view_password(
                            info_password=info_password_not_view, view_password_img=not_view_password_img,
                            button=button_not_view
                        )
                    }
                ]
            )

    Register()
