"""Installing App Panel"""

from tkinter import Tk, PhotoImage, Text, Toplevel, ttk, Label, Scrollbar, END, Entry, filedialog, messagebox, StringVar

import subprocess

import sys

import os

import shutil

import time

import win32api

windows_main = Tk()
Path = StringVar()
UserPC = win32api.GetUserName()


class FinishApp():
    def __init__(
        self
    ):

        # View ==> geometry ==> title ==> resizable ==> icon
        self.windows_finish = Toplevel()
        self.windows_finish.geometry(
            '550x420+625+325'
        )
        self.windows_finish.title(
            'Windows Install'
        )
        self.windows_finish.resizable(
            False,
            False
        )
        icon = PhotoImage(
            file=r'Images\img-install-app.png'
        )
        self.windows_finish.iconphoto(
            False,
            icon
        )
        self.windows_finish.config(
            background='white'
        )

        # Panel ==> img ==> label

        img_panel = PhotoImage(
            file=r'Images\img-panel.png'
        )

        panel = Label(
            self.windows_finish,
            image=img_panel
        )

        panel.place(
            x=-2,
            y=-2
        )

        # Panel ==> up ==> line panel

        panel_up = Label(
            self.windows_finish
        )

        panel_up.place(
            width=550,
            height=60,
            x=0,
            y=360
        )

        line_panel = Label(
            self.windows_finish,
            background='#b3b3b3'
        )

        line_panel.place(
            width=550,
            height=1,
            x=0,
            y=360
        )

        # Buttons ==> Cancel ==> Finish ==> Back

        cancel = ttk.Button(
            self.windows_finish,
            text='Cancel',
            cursor='hand2',
            state='disable'
        )

        cancel.place(
            x=450,
            y=378
        )

        exit_program = ttk.Button(
            self.windows_finish,
            text='Finish',
            cursor='hand2',
            command=lambda: [
                {
                    self.exit_program()
                }
            ]
        )

        exit_program.place(
            x=360,
            y=378
        )

        back = ttk.Button(
            self.windows_finish,
            text='< Back',
            cursor='hand2',
            state='disable'
        )

        back.place(
            x=280,
            y=378
        )

        # Information ==> tile ==> info

        information_title = Label(
            self.windows_finish,
            text='Completed Setup',
            font=(
                'Arial', 16
            ),
            background='white',
            foreground='black'
        )

        information_title.place(
            x=215,
            y=20
        )

        self.information_info = Text(
            self.windows_finish,
            font=(
                'Arial', 11
            ),
            background='white',
            foreground='black',
            border=0
        )

        self.information_info.insert(
            'end',
            'ChatBoot 1.0.0 has been installed on your computer. \n\nClick Finish to close Setup.'
        )

        self.information_info.place(
            width=320,
            height=200,
            x=215,
            y=90
        )

        self.information_info.after(
            100, self.block_text
        )

        self.windows_finish.mainloop()

    def block_text(self):
        self.information_info.config(
            state='disabled'
        )

    def exit_program(self):
        self.windows_finish.destroy()
        windows_main.destroy()
        subprocess.Popen(
            [
                'taskkill',
                '/f',
                '/im',
                'ChatBoot.exe'
            ]
        )
        sys.exit()


def verify_install(windows, entry):
    '''Verified ==> verify path install folder not exist'''
    rut_path = Path.get()

    if not os.path.exists(rut_path):
        windows.withdraw()
        Install()
    else:
        messagebox.showerror(
            'Error', 'The folder already exists in this path, please delete it.'
        )
        entry.config(
            state='normal'
        )
        entry.delete(
            0,
            END
        )
        Path.set(
            'Select Path'
        )
        entry.config(
            state='disable'
        )


class Install():
    def return_select_path(self):
        self.windows_install.withdraw()
        SelectPath()

    def exit_program(self):
        self.windows_install.destroy()
        sys.exit()

    def __init__(
        self
    ):

        # View ==> geometry ==> title ==> resizable ==> icon

        self.windows_install = Toplevel()

        self.windows_install.geometry(
            '550x420+625+325'
        )
        self.windows_install.title(
            'Windows Install'
        )
        self.windows_install.resizable(
            False,
            False
        )
        icon = PhotoImage(
            file=r'Images\img-install-app.png'
        )
        self.windows_install.iconphoto(
            False,
            icon
        )

        # Panel ==> up ==> line panel up

        panel_up = Label(
            self.windows_install,
            background='white'
        )

        panel_up.place(
            width=550,
            height=50,
            x=0,
            y=0
        )

        # Panel ==> img ==> label ==> line panel up

        img_panel = PhotoImage(
            file=r'Images\img-panel-up.png'
        )

        panel = Label(
            self.windows_install,
            image=img_panel
        )

        panel.place(
            x=-2,
            y=-2
        )

        line_panel_up = Label(
            self.windows_install,
            background='#b3b3b3'
        )

        line_panel_up.place(
            width=550,
            height=1,
            x=0,
            y=50
        )

        # Panel ==> bottom ==> line panel

        panel_bottom = Label(
            self.windows_install
        )

        panel_bottom.place(
            width=550,
            height=60,
            x=0,
            y=360
        )

        line_panel = Label(
            self.windows_install,
            background='#d2d2d2'
        )

        line_panel.place(
            width=545,
            height=1,
            x=5,
            y=360
        )

        # Text ==> information's the SelectPath

        info_the_SelectPath = Label(
            self.windows_install,
            text='Nullsoft SelectPath System v1.0.0',
            font=(
                'Arial', 10
            ),
            foreground='#a0a0a0'
        )

        info_the_SelectPath.place(
            x=5,
            y=349
        )

        # Text ==> license information ==> info installing

        license_information = Label(
            self.windows_install,
            text='Installing',
            font=(
                'Arial Black', 11
            ),
            background='white',
            foreground='black'
        )

        license_information.place(
            x=210,
            y=0
        )

        info_installing = Label(
            self.windows_install,
            text='Please wait while ChatBoot 1.0.0 is being installed.',
            font=(
                'Arial', 8
            ),
            background='white',
            foreground='black'
        )

        info_installing.place(
            x=220,
            y=25
        )

        # Buttons ==> cancel ==> back ==> select path

        cancel = ttk.Button(
            self.windows_install,
            text='Cancel',
            cursor='hand2',
            command=lambda: [
                {
                    self.exit_program()
                }
            ]
        )

        cancel.place(
            x=450,
            y=378
        )

        self.back = ttk.Button(
            self.windows_install,
            text='< Back',
            cursor='hand2',
            command=lambda: [
                {
                    self.return_select_path()
                }
            ]
        )

        self.back.place(
            x=280,
            y=378
        )

        install = ttk.Button(
            self.windows_install,
            text='Install',
            cursor='hand2',
            command=lambda: [
                {
                    self.install_app()
                }
            ]
        )

        install.place(
            x=360,
            y=378
        )

        # Install ==> Progressbar ==> txt
        styles_install = ttk.Style()
        styles_install.configure(
            'TProgressbar',
            troughcolor='green',
            background='#2b79c2',
            bordercolor='green',
        )

        self.progressbar = ttk.Progressbar(
            self.windows_install,
            style="TProgressbar",
            orient='horizontal',
            length=510
        )

        self.progressbar.place(
            height=30,
            x=20,
            y=90
        )

        self.txt_progresbar = Label(
            self.windows_install,
            text='Installing',
            font=(
                'Arial', 12
            )
        )

        self.txt_progresbar.place(
            x=20,
            y=65
        )

        self.windows_install.mainloop()

    def move_points(self):
        def move_points_2():
            self.txt_progresbar.config(
                text='Installing...'
            )
            open_finish = self.txt_progresbar.after(
                500
            )
            self.move_lnk()
        self.txt_progresbar.config(
            text='Installing..'
        )
        self.txt_progresbar.after(
            600, move_points_2
        )

    def install_app(self):

        self.back.config(
            state='disable'
        )
        task = 11
        porcentaje = 0
        while porcentaje < task:
            time.sleep(0.5)
            self.progressbar['value'] += 11
            porcentaje += 1.1
            self.windows_install.update_idletasks()
        if porcentaje > task:
            self.txt_progresbar.config(
                text='Installing.'
            )
            self.txt_progresbar.after(
                600, self.move_points
            )

    def move_lnk(self):
        path_selec = Path.get()

        # Move Folder

        folder_path = 'ChatBoot'
        move_folder_path = f'{path_selec}'

        shutil.move(folder_path, move_folder_path)

        # Lnk move desktop

        lnk_desktop = f'{path_selec}/LnkDektop/CHATBOOT.exe.lnk'
        desktop = f'C:/Users/{UserPC}/OneDrive/Escritorio/'

        shutil.move(lnk_desktop, desktop)

        # Lnk move panel apps

        lnk_panel_apps = f'{path_selec}/LnkPrograms/CHATBOOT.exe.lnk'

        panel_apps = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs'

        shutil.move(lnk_panel_apps, panel_apps)

        # Close Windows
        self.windows_install.destroy()
        FinishApp()


class SelectPath():
    def open_path(self):
        self.folder_selected = filedialog.askdirectory()

        if not os.path.exists(self.folder_selected):
            self.next.config(
                state='disabled'
            )
            messagebox.showerror(
                'Error', 'Enter a readable path'
            )
            self.path_entry.config(
                state='normal'
            )
            self.path_entry.delete(
                0,
                END
            )
            Path.set(
                'Select Path'
            )
            self.path_entry.config(
                state='disabled'
            )
        else:
            self.path_entry.config(
                state='normal'
            )
            self.path_entry.delete(
                0,
                END
            )

            Path.set(
                f'{self.folder_selected}'
            )

            if Path.get() == 'C:/':
                Path.set(
                    'C:/ChatBoot'
                )
            else:
                Path.set(
                    f'{Path.get()}/ChatBoot'
                )

            self.path_entry.config(
                state='disabled',
                disabledbackground='#f0f0f0'
            )

            self.next.config(
                state='normal'
            )

    def return_polices(self):
        self.windows_select_path.withdraw()
        Polices()

    def exit_program(self):
        self.windows_select_path.destroy()
        sys.exit()

    def __init__(
        self
    ):
        # View ==> geometry ==> title ==> resizable ==> icon

        self.windows_select_path = Toplevel()

        self.windows_select_path.geometry(
            '550x420+625+325'
        )
        self.windows_select_path.title(
            'Windows Install'
        )
        self.windows_select_path.resizable(
            False,
            False
        )
        icon = PhotoImage(
            file=r'Images\img-install-app.png'
        )
        self.windows_select_path.iconphoto(
            False,
            icon
        )

        # Panel ==> up ==> line panel up

        panel_up = Label(
            self.windows_select_path,
            background='white'
        )

        panel_up.place(
            width=550,
            height=50,
            x=0,
            y=0
        )

        # Panel ==> img ==> label ==> line panel up

        img_panel = PhotoImage(
            file=r'Images\img-panel-up.png'
        )

        panel = Label(
            self.windows_select_path,
            image=img_panel
        )

        panel.place(
            x=-2,
            y=-2
        )

        line_panel_up = Label(
            self.windows_select_path,
            background='#b3b3b3'
        )

        line_panel_up.place(
            width=550,
            height=1,
            x=0,
            y=50
        )

        # Panel ==> bottom ==> line panel

        panel_bottom = Label(
            self.windows_select_path
        )

        panel_bottom.place(
            width=550,
            height=60,
            x=0,
            y=360
        )

        line_panel = Label(
            self.windows_select_path,
            background='#d2d2d2'
        )

        line_panel.place(
            width=545,
            height=1,
            x=5,
            y=360
        )

        # Text ==> information's the SelectPath

        info_the_SelectPath = Label(
            self.windows_select_path,
            text='Nullsoft SelectPath System v1.0.0',
            font=(
                'Arial', 10
            ),
            foreground='#a0a0a0'
        )

        info_the_SelectPath.place(
            x=5,
            y=349
        )

        # Text ==> license information ==> info SelectPathing

        license_information = Label(
            self.windows_select_path,
            text='Choose SelectPath Location',
            font=(
                'Arial Black', 11
            ),
            background='white',
            foreground='black'
        )

        license_information.place(
            x=210,
            y=0
        )

        info_SelectPathing = Label(
            self.windows_select_path,
            text='Choose the folder in which to SelectPath ChatBoot 1.0.0',
            font=(
                'Arial', 8
            ),
            background='white',
            foreground='black'
        )

        info_SelectPathing.place(
            x=220,
            y=25
        )

        # Buttons ==> cancel ==> back ==> select path

        cancel = ttk.Button(
            self.windows_select_path,
            text='Cancel',
            cursor='hand2',
            command=lambda: [
                {
                    self.exit_program()
                }
            ]
        )

        cancel.place(
            x=450,
            y=378
        )

        back = ttk.Button(
            self.windows_select_path,
            text='< Back',
            cursor='hand2',
            command=lambda: [
                {
                    self.return_polices()
                }
            ]
        )

        back.place(
            x=280,
            y=378
        )

        self.next = ttk.Button(
            self.windows_select_path,
            text='Next >',
            cursor='hand2',
            state='disable',
            command=lambda: [
                {
                    self.install()
                }
            ]
        )

        self.next.place(
            x=360,
            y=378
        )

        # Info ==> txt information

        txt_information = Label(
            self.windows_select_path,
            text='Setup will install ChatBoot 1.0.0 in the following folder. To install in a different folder, \nclick Browse and select another folder. Click Next to start the installation.',
            font=(
                'Arial', 10
            ),
            foreground='black'
        )

        txt_information.place(
            x=13,
            y=80
        )

        # Select Path ==> txt ==> entry ==> button

        path_line_panel1 = Label(
            self.windows_select_path,
            background='#d2d2d2'
        )

        path_line_panel1.place(
            width=500,
            height=1,
            x=25,
            y=193
        )

        path_line_panel2 = Label(
            self.windows_select_path,
            background='#d2d2d2'
        )

        path_line_panel2.place(
            width=500,
            height=1,
            x=25,
            y=253
        )

        path_line_panel3 = Label(
            self.windows_select_path,
            background='#d2d2d2'
        )

        path_line_panel3.place(
            width=1,
            height=60,
            x=25,
            y=193
        )
        path_line_panel4 = Label(
            self.windows_select_path,
            background='#d2d2d2'
        )

        path_line_panel4.place(
            width=1,
            height=60,
            x=525,
            y=193
        )

        select_path_txt = Label(
            self.windows_select_path,
            text='Destination Folder',
            font=(
                'Arial', 11
            )
        )

        select_path_txt.place(
            x=50,
            y=182
        )

        self.path_entry = Entry(
            self.windows_select_path,
            background='#f0f0f0',
            foreground='black',
            font=(
                'Arial', 13
            ),
            disabledbackground='#f0f0f0',
            textvariable=Path
        )

        Path.set(
            'Select Path'
        )

        self.path_entry.place(
            width=450,
            height=30,
            x=50,
            y=210
        )

        self.path_entry.config(
            state='disabled'
        )

        path_button = ttk.Button(
            self.windows_select_path,
            text='       Browse...       ',
            command=lambda: [
                {
                    self.open_path()
                }
            ]
        )

        path_button.place(
            x=427,
            y=260
        )

        self.windows_select_path.mainloop()

    def install(self):
        verify_install(windows=self.windows_select_path, entry=self.path_entry)


def insert_information(info, win):
    """Insert info int information it's class"""

    # Configure ==> font ==> foreground
    info.tag_config(
        "title", font=('Arial', 20), foreground='red'
    )

    info.tag_config(
        'polices', font=('Arial', 13), foreground='blue'
    )

    info.tag_configure(
        'info_polices', font=('Arial', 11), foreground='black'
    )

    # Configure ==> insert information

    info.insert(
        END, "CHAT BOOT                              v1.0.0\n", "title"
    )

    info.insert(
        END, "\nPrivacy Policy", 'polices'
    )

    info.insert(
        END,
        "\n\nAt xRICKYTOx, we are committed to protecting your privacy and ensuring that your personal information is handled in a safe and responsible manner. This Privacy Policy outlines how we collect, use, disclose, and store your personal information,and your rights with respect to that information.\n\nInformation We Collect \n\nWe collect personal information from you when you use our website, products, or services. We may also collect non-personal information, such as your IP address and browser type, through the use of cookies and other tracking technologies.\n\nHow We Use Your Information \n\nWe may use your personal information to provide you with the products or services that you have requested, to communicate with you about our products or services, and to improve our offerings. We may also use your information for marketing purposes, such as to send you promotional emails or newsletters.\n\nHow We Share Your Information\n\nWe may share your personal information with third-party service providers who perform services on our behalf, such as payment processing, customer service, and marketing. We may also share your information with our affiliates, subsidiaries, or other third parties for their own marketing purposes. We will not sell your personal information to third parties for their marketing purposes without your consent.\n\nYour Rights\n\nYou have the right to access, correct, or delete your personal information at any time. You also have the right to object to the processing of your personal information, to restrict the processing of your personal information and to receive a copy of your personal information in a structured, machine-readable format. \n\nSecurity\n\nWe take the security of your personal information seriously and implement appropriate technical and organizational measures to protect it from unauthorized access, disclosure, alteration, or destruction. \n\nContact Us\n\nIf you have any questions or concerns about our Privacy Policy, please contact us at rikytoloser@gmail.com. We may update this Privacy Policy from time to time, and any changes will be posted on our website.\n\nCopyright\n\nCopyright ChatBoot 2023-2024©", 'info_polices'
    )

    # Configure ==> desactive widget

    info.config(
        state='disable'
    )

    win.mainloop()


class Polices():

    def exit_program(self):
        self.windows_polices.destroy()
        sys.exit()

    def return_main(self):
        self.windows_polices.withdraw()
        windows_main.deiconify()

    def select_path_app(self):
        self.windows_polices.withdraw()
        SelectPath()

    def polices_insert(self, info, win):
        insert_information(info, win)

    def __init__(
        self
    ):
        # View ==> geometry ==> title ==> resizable ==> icon

        self.windows_polices = Toplevel()

        self.windows_polices.geometry(
            '550x420+625+325'
        )
        self.windows_polices.title(
            'Windows Install'
        )
        self.windows_polices.resizable(
            False,
            False
        )
        icon = PhotoImage(
            file=r'Images\img-install-app.png'
        )
        self.windows_polices.iconphoto(
            False,
            icon
        )

        # Panel ==> up ==> line panel up

        panel_up = Label(
            self.windows_polices,
            background='white'
        )

        panel_up.place(
            width=550,
            height=50,
            x=0,
            y=0
        )

        # Panel ==> img ==> label ==> line panel up

        img_panel = PhotoImage(
            file=r'Images\img-panel-up.png'
        )

        panel = Label(
            self.windows_polices,
            image=img_panel
        )

        panel.place(
            x=-2,
            y=-2
        )

        line_panel_up = Label(
            self.windows_polices,
            background='#b3b3b3'
        )

        line_panel_up.place(
            width=550,
            height=1,
            x=0,
            y=50
        )

        # Panel ==> bottom ==> line panel

        panel_bottom = Label(
            self.windows_polices
        )

        panel_bottom.place(
            width=550,
            height=60,
            x=0,
            y=360
        )

        line_panel = Label(
            self.windows_polices,
            background='#d2d2d2'
        )

        line_panel.place(
            width=545,
            height=1,
            x=5,
            y=360
        )

        # Text ==> information's the install

        info_the_install = Label(
            self.windows_polices,
            text='Nullsoft Install System v1.0.0',
            font=(
                'Arial', 10
            ),
            foreground='#a0a0a0'
        )

        info_the_install.place(
            x=5,
            y=349
        )

        # Text ==> license information ==> info installing

        license_information = Label(
            self.windows_polices,
            text='License Information',
            font=(
                'Arial Black', 11
            ),
            background='white',
            foreground='black'
        )

        license_information.place(
            x=210,
            y=0
        )

        info_installing = Label(
            self.windows_polices,
            text='Please review the license terms before installing ChatBoot',
            font=(
                'Arial', 8
            ),
            background='white',
            foreground='black'
        )

        info_installing.place(
            x=220,
            y=25
        )

        # Buttons ==> cancel ==> back ==> next

        cancel = ttk.Button(
            self.windows_polices,
            text='Cancel',
            cursor='hand2',
            command=lambda: [
                {
                    self.exit_program()
                }
            ]
        )

        cancel.place(
            x=450,
            y=378
        )

        back = ttk.Button(
            self.windows_polices,
            text='< Back',
            cursor='hand2',
            command=lambda: [
                {
                    self.return_main()
                }
            ]
        )

        back.place(
            x=280,
            y=378
        )

        next = ttk.Button(
            self.windows_polices,
            text='Next >',
            cursor='hand2',
            command=lambda: [
                {
                    self.select_path_app()
                }
            ]
        )

        next.place(
            x=360,
            y=378
        )

        # Polices ==> text ==> scrollbar

        self.polices = Text(
            self.windows_polices,
            background='white',
            foreground='black',
            font=(
                'Arial', 13
            ),
            state='normal'
        )

        scrollbar = Scrollbar(
            self.windows_polices,
            command=self.polices.yview,
            cursor='hand2',
            border=0
        )

        scrollbar.place(
            width=20,
            height=273,
            x=504,
            y=64
        )

        self.polices.place(
            width=481,
            height=275,
            x=23,
            y=63
        )

        self.polices.config(
            yscrollcommand=scrollbar.set
        )

        self.polices.after(
            100, self.polices_insert(
                info=self.polices, win=self.windows_polices
            )
        )
        self.windows_polices.mainloop()


class MainApp():
    def __init__(
        self
    ):

        # View ==> geometry ==> title ==> resizable ==> icon

        windows_main.geometry(
            '550x420+625+325'
        )
        windows_main.title(
            'Windows Install'
        )
        windows_main.resizable(
            False,
            False
        )
        icon = PhotoImage(
            file=r'Images\img-install-app.png'
        )
        windows_main.iconphoto(
            False,
            icon
        )
        windows_main.config(
            background='white'
        )

        # Panel ==> img ==> label

        img_panel = PhotoImage(
            file=r'Images\img-panel.png'
        )

        panel = Label(
            windows_main,
            image=img_panel
        )

        panel.place(
            x=-2,
            y=-2
        )

        # Panel ==> up ==> line panel

        panel_up = Label(
            windows_main
        )

        panel_up.place(
            width=550,
            height=60,
            x=0,
            y=360
        )

        line_panel = Label(
            windows_main,
            background='#b3b3b3'
        )

        line_panel.place(
            width=550,
            height=1,
            x=0,
            y=360
        )

        # Buttons ==> Cancel ==> Next

        cancel = ttk.Button(
            windows_main,
            text='Cancel',
            cursor='hand2',
            command=lambda: [
                {
                    self.exit_program()
                }
            ]
        )

        cancel.place(
            x=450,
            y=378
        )

        next = ttk.Button(
            windows_main,
            text='Next >',
            cursor='hand2',
            command=lambda: [
                {
                    self.open_polices()
                }
            ]
        )

        next.place(
            x=360,
            y=378
        )

        # Information ==> tile ==> info

        information_title = Label(
            windows_main,
            text='Welcome to ChatBoot 1.0.0\nSetup',
            font=(
                'Arial', 16
            ),
            background='white',
            foreground='black'
        )

        information_title.place(
            x=235,
            y=20
        )

        self.information_info = Text(
            windows_main,
            font=(
                'Arial', 11
            ),
            background='white',
            foreground='black',
            border=0
        )

        self.information_info.insert(
            'end',
            'This setup will guide you through install Chat        Boot.\n\nIt is recommended that you close all other applications before starting, including Chat Boot. This will make it possible to update relevant files without having to reboot you computer. \n\nClick Next to continue.'
        )

        self.information_info.place(
            width=320,
            height=200,
            x=215,
            y=90
        )

        self.information_info.after(
            100, self.block_text
        )

        windows_main.mainloop()

    def open_polices(self):
        windows_main.withdraw()
        Polices()

    def block_text(self):
        self.information_info.config(
            state='disabled'
        )

    def exit_program(self):
        windows_main.destroy()
        sys.exit()


MainApp()
