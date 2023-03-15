"""Main Page"""

from tkinter import Tk, PhotoImage, Label, Entry, StringVar, Button, messagebox
import os
import sqlite3

windows = Tk()
USERNAME = StringVar()
PASSWORD = StringVar()

path = os.getcwd()

img_icon = f'{path}/Icon/icon-user.ico'
img_logo = f'{path}/Img/img-logo.png'
img_view_password = f"{path}/Img/img-view-password.png"
img_not_view_password = f"{path}/Img/img-not-view-password.png"
databases = f'{path}/Database/users_passwords.db'


def register_function():
    windows.withdraw()
    from Reg.register import register
    Username = USERNAME
    Password = PASSWORD
    register(Username, Password)


def login_user_password(username, password, user_entry, pass_entry):
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

    if result:
        messagebox.showinfo(
            'Congratulations', f'You init sesion in account [{username}]'
        )
        windows.withdraw()
        from App.chatbot import ChatBot
        ChatBot()
    else:
        messagebox.showerror(
            'Error', f"Your account [{username}] it's not exist int database"
        )
        user_entry.delete(
            0,
            'end'
        )
        pass_entry.delete(
            0,
            'end'
        )


class LogIn:
    def __init__(
        self
    ):
        windows.geometry(
            '900x650+525+200'
        )
        windows.title(
            'Log In'
        )
        windows.iconbitmap(
            img_icon
        )
        windows.resizable(
            False,
            False
        )
        windows.config(
            background='#252525'
        )

        right_panel = Label(
            windows,
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
            windows,
            image=logo_img,
            background='#294c60'
        )

        logo.place(
            x=600,
            y=70
        )

        log_in_txt = Label(
            windows,
            text='LOG IN',
            background='#252525',
            foreground='white',
            font=(
                'Arial Black', 35
            )
        )

        log_in_txt.place(
            x=180,
            y=25
        )

        username_txt = Label(
            windows,
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
            windows,
            textvariable=USERNAME,
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
            windows,
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
            windows,
            background='#6f95aa'
        )

        password_label.place(
            width=470,
            height=40,
            x=40,
            y=330
        )

        password_entry = Entry(
            windows,
            textvariable=PASSWORD,
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

        self.not_view_password_bt = Button(
            windows,
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
                        button=self.not_view_password_bt
                    )
                }
            ]
        )

        self.not_view_password_bt.place(
            x=473,
            y=333
        )

        button_login = Button(
            windows,
            text='LOG IN',
            background="grey",
            foreground='#252525',
            font=(
                'Arial Black', 18
            ),
            border=0,
            cursor='hand2',
            activebackground='white',
            command=lambda: login_user_password(
                USERNAME.get(), PASSWORD.get(), user_entry=username_entry, pass_entry=password_entry
            )
        )

        button_login.place(
            width=390,
            height=50,
            x=80,
            y=430
        )

        button_register = Button(
            windows,
            text='REGISTER',
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
                    register_function()
                }
            ]
        )

        button_register.place(
            width=390,
            height=50,
            x=80,
            y=540
        )

        windows.bind(
            '<Return>', lambda event: login_user_password(
                USERNAME.get(), PASSWORD.get(), user_entry=username_entry, pass_entry=password_entry
            )
        )

        windows.mainloop()

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


if __name__ == "__main__":
    LogIn()
