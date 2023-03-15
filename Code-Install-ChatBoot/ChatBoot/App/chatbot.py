"""App Chat Bot"""

from tkinter import Toplevel, Button, PhotoImage, Label, Entry, StringVar, Text, END
from tkinter import filedialog, messagebox
from Insert.inserts import insert_chat_message
import io
import os
from Log.log_in import USERNAME


path = os.getcwd()

img_icon = f'{path}/Icon/icon-app.ico'
img_clear = f"{path}/Img/img-clear.png"
img_download = f"{path}/Img/img-download.png"
img_logo_transparent = f"{path}/Img/img-logo-transparent.png"
img_logo = f"{path}/Img/img-logo.png"
img_message = f"{path}/Img/img-message.png"

windows = Toplevel()
Message = StringVar()


def send_message_button(chat, message, message_entry):
    """Insert info int Chat"""
    ventana = windows
    username = USERNAME.get()
    insert_chat_message(chat, message, message_entry, ventana, username)


def delete_chat_info(chat):
    """Delete info int Chat"""
    chat.config(
        state='normal'
    )
    chat.delete(
        1.0,
        END
    )
    chat.config(
        state='disable'
    )


def save_information(chat):
    """Save information"""

    text_content = chat.get(
        '1.0',
        END
    )
    file_path = filedialog.asksaveasfilename(
        defaultextension='.txt'
    )

    if file_path:
        with io.open(
            file_path, 'w', encoding='utf-8'
        )as file:
            file.write(
                text_content
            )
        messagebox.showinfo(
            'Congratulations', 'The file was saved successfully'
        )
    else:
        messagebox.showerror(
            'Error', 'The file is not saved'
        )


class ChatBot():
    """App general or main"""
    # APP

    def __init__(
            self
    ):

        windows.geometry(
            '1000x650+425+200'
        )

        windows.title(
            'Chat Boot'
        )

        windows.iconbitmap(
            img_icon
        )
        windows.resizable(
            False,
            False
        )

        # Panel -> Left -> Right

        panel_left = Label(
            windows,
            background='#252525'
        )

        panel_left.place(
            width=1000,
            height=650,
            x=0,
            y=0
        )

        panel_right = Label(
            windows,
            background='grey'
        )

        panel_right.place(
            width=400,
            height=650,
            x=1000,
            y=0
        )

        # Clear

        clear_img = PhotoImage(
            file=img_clear
        )

        clear = Button(
            windows,
            image=clear_img,
            background="#252525",
            activebackground='#252525',
            border=0,
            cursor="hand2",
            command=lambda: [
                {
                    delete_chat_info(chat=self.chat)
                }
            ]
        )

        clear.place(
            x=10,
            y=500
        )

        # Download Conversation

        download_conversation_img = PhotoImage(
            file=img_download
        )

        download_conversation = Button(
            windows,
            image=download_conversation_img,
            background="#252525",
            activebackground='#252525',
            border=0,
            cursor="hand2",
            command=lambda: [
                {
                    save_information(
                        chat=self.chat
                    )
                }
            ]
        )

        download_conversation.place(
            x=10,
            y=575
        )

        # Message

        self.message_entry = Entry(
            windows,
            textvariable=Message,
            foreground='white',
            background='#6F95AB',
            font=(
                'Arial', 20
            ),
            justify='center',
            selectbackground='grey',
            border=0,
            disabledbackground='#6F95AB'
        )

        self.message_entry.place(
            width=690,
            height=45,
            x=140,
            y=578
        )

        # Send Message

        send_message_img = PhotoImage(
            file=img_message
        )

        send_message = Button(
            windows,
            image=send_message_img,
            background="#252525",
            activebackground='#252525',
            border=0,
            cursor="hand2",
            command=lambda: [
                {
                    send_message_button(
                        chat=self.chat, message=Message.get(), message_entry=self.message_entry
                    )
                }
            ]
        )

        send_message.place(
            x=850,
            y=575
        )

        # Message Box or Chat

        self.chat = Text(
            windows,
            font=(
                'Arial', 16
            ),
            background='#2A4C60',
            foreground='white',
            selectbackground='grey',
            state='disabled',
            border=0
        )

        self.chat.place(
            width=800,
            height=530,
            x=120,
            y=20
        )

        # Keyboard Functions

        windows.bind(
            '<Return>', lambda event: send_message_button(
                chat=self.chat, message=Message.get(), message_entry=self.message_entry
            )
        )

        windows.mainloop()

    # Functions
