"""Insert text the chat"""


from tkinter import END, messagebox

from Word.words import saludar, salir, abre_block_notas, cierra_block_notas, abre_calculadora

from Word.words import cierra_claculadora, abre_navevagor, cierra_navegador, abre_yt, abre_musica

from Word.words import cierra_musica, abre_app_musica_itunes, cierra_app_musica_itunes

from Word.words import abre_app_musica_spotify, cierra_app_musica_spotify

from Word.words import abre_explorador_archivos, abre_riot_games, cierra_riot_games

from Word.words import abre_visual_studio_code, cierra_visual_studio_code, abre_administrador_tareas

from Word.words import cierra_administrador_tareas

from Settings.System.system import terminar_app, abrir_block_notas, cerrar_block_notas, abrir_calculadora

from Settings.System.system import cerrar_calculadora, cerrar_navegador, abrir_musica, cerrar_musica

from Settings.System.system import abrir_itunes, cerrar_itunes, abrir_spotify, cerrar_spotify

from Settings.System.system import abrir_explorador_archivos, abrir_riot_games, cerrar_riot_games

from Settings.System.system import abrir_visual_studio_code, cerrar_visual_studio_code

from Settings.System.system import abrir_taskmgr, cerrar_taskmgr

from Settings.Web.web import abrir_navegador, abrir_yt


def insert_answer_greet(chat, message, message_entry, ventana, username):
    """Insert greet int Chat"""
    def answer_bot():
        bot = chat.insert(
            END,
            f'\n    BOT: Hola [ {username} ] en que te puedo ayudar el dia de hoy...?\n'
        )
        desc = chat.after(
            2100
        )
        chat.config(
            state='disable'
        )
        message_entry.config(
            state='normal'
        )
        message_entry.delete(
            0,
            END
        )
    if message in saludar:
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    else:
        insert_answer_exit(chat, message, message_entry, ventana)


def insert_answer_exit(chat, message, message_entry, ventana):
    """Insert exit int Chat"""
    def answer_bot():
        def exit():
            ventana.destroy()
            terminar_app()

        bot = chat.insert(
            END,
            f'\n    BOT: Gracias por pasar un rato conmigo!!!\n'
        )
        desc = chat.after(
            2100
        )
        exi = chat.after(
            2100, exit
        )
        chat.config(
            state='disable'
        )
        message_entry.delete(
            0,
            END
        )
    if message in salir:
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    else:
        insert_answer_open_close_block_notes(chat, message, message_entry)


def insert_answer_open_close_block_notes(chat, message, message_entry):
    """Insert open and close block notes int Chat"""
    if message in abre_block_notas:
        def answer_bot1():
            bot = chat.insert(
                END,
                f'\n    BOT: Abriendo el block de notas...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, abrir_block_notas
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )

        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot1
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    elif message in cierra_block_notas:
        def answer_bot2():
            bot = chat.insert(
                END,
                f'\n    BOT: Cerrando el block de notas...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, cerrar_block_notas
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot2
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    else:
        insert_answer_open_close_calc(chat, message, message_entry)


def insert_answer_open_close_calc(chat, message, message_entry):
    """Insert open and close calc in Chat"""
    if message in abre_calculadora:
        def answer_bot1():
            bot = chat.insert(
                END,
                f'\n    BOT: Abriendo la calculadora...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, abrir_calculadora
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot1
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )

    elif message in cierra_claculadora:
        def answer_bot2():
            bot = chat.insert(
                END,
                f'\n    BOT: Cerrando la calculadora...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, cerrar_calculadora
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot2
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    else:
        insert_answer_open_close_browser(chat, message, message_entry)


def insert_answer_open_close_browser(chat, message, message_entry):
    """Insert open and close browser int Chat"""
    if message in abre_navevagor:
        def answer_bot1():
            bot = chat.insert(
                END,
                f'\n    BOT: Abriendo el navegador...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, abrir_navegador
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot1
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    elif message in cierra_navegador:
        def answer_bot2():
            bot = chat.insert(
                END,
                f'\n    BOT: Cerrando el navegador...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, cerrar_navegador
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot2
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    else:
        insert_answer_open_youtube(chat, message, message_entry)


def insert_answer_open_youtube(chat, message, message_entry):
    """Insert open YouTube int Chat"""
    if message in abre_yt:
        def answer_bot1():
            bot = chat.insert(
                END,
                f'\n    BOT: Abriendo YouTube en el navegador...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, abrir_yt
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot1
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    else:
        insert_answer_open_close_music(chat, message, message_entry)


def insert_answer_open_close_music(chat, message, message_entry):
    """Insert open and close music int Chat"""
    if message in abre_musica:
        def answer_bot1():
            bot = chat.insert(
                END,
                f'\n    BOT: Abriendo la aplicación de musica...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, abrir_musica
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot1
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    elif message in cierra_musica:
        def answer_bot2():
            bot = chat.insert(
                END,
                f'\n    BOT: Cerrando la aplicación de musica...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, cerrar_musica
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot2
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    else:
        insert_answer_open_close_itunes(chat, message, message_entry)


def insert_answer_open_close_itunes(chat, message, message_entry):
    """Insert open and close iTunes int Chat"""
    if message in abre_app_musica_itunes:
        def answer_bot1():
            bot = chat.insert(
                END,
                f'\n    BOT: Abriendo la aplicación iTunes...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, abrir_itunes
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot1
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    elif message in cierra_app_musica_itunes:
        def answer_bot2():
            bot = chat.insert(
                END,
                f'\n    BOT: Cerrando la aplicación iTunes...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, cerrar_itunes
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot2
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    else:
        insert_answer_open_close_spotify(chat, message, message_entry)


def insert_answer_open_close_spotify(chat, message, message_entry):
    """Insert open and close Spotify int Chat"""
    if message in abre_app_musica_spotify:
        def answer_bot1():
            bot = chat.insert(
                END,
                f'\n    BOT: Abriendo la aplicación Spotify...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, abrir_spotify
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot1
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    elif message in cierra_app_musica_spotify:
        def answer_bot2():
            bot = chat.insert(
                END,
                f'\n    BOT: Cerrando la aplicación Spotify...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, cerrar_spotify
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot2
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    else:
        insert_answer_open_expl_arch(chat, message, message_entry)


def insert_answer_open_expl_arch(chat, message, message_entry):
    """Insert open Explorer Archive int Chat"""
    if message in abre_explorador_archivos:
        def answer_bot1():
            bot = chat.insert(
                END,
                f'\n    BOT: Abriendo el explorador de archivos...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, abrir_explorador_archivos
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot1
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    else:
        insert_answer_open_close_riot_games(chat, message, message_entry)


def insert_answer_open_close_riot_games(chat, message, message_entry):
    """Insert open and close RiotGames int Chat"""
    if message in abre_riot_games:
        def answer_bot1():
            bot = chat.insert(
                END,
                f'\n    BOT: Abriendo la aplicación RiotGames...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, abrir_riot_games
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot1
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    elif message in cierra_riot_games:
        def answer_bot2():
            bot = chat.insert(
                END,
                f'\n    BOT: Cerrando la aplicación RiotGames...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, cerrar_riot_games
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot2
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    else:
        insert_answer_open_close_vsc(chat, message, message_entry)


def insert_answer_open_close_vsc(chat, message, message_entry):
    """Insert open and close Visual Studio Code int Chat"""
    if message in abre_visual_studio_code:
        def answer_bot1():
            bot = chat.insert(
                END,
                f'\n    BOT: Abriendo la aplicación Visual Studio Code...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, abrir_visual_studio_code
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot1
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    elif message in cierra_visual_studio_code:
        def answer_bot2():
            bot = chat.insert(
                END,
                f'\n    BOT: Cerrando la aplicación Visual Studio Code...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, cerrar_visual_studio_code
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot2
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    else:
        insert_answer_open_close_task_manager(chat, message, message_entry)


def insert_answer_open_close_task_manager(chat, message, message_entry):
    """Insert open and close Task Manager int Chat"""
    if message in abre_administrador_tareas:
        def answer_bot1():
            bot = chat.insert(
                END,
                f'\n    BOT: Abriendo la aplicación Task Manager...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, abrir_taskmgr
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot1
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    elif message in cierra_administrador_tareas:
        def answer_bot2():
            bot = chat.insert(
                END,
                f'\n    BOT: Cerrando la aplicación Task Manager...\n'
            )
            desc = chat.after(
                2100
            )
            op = chat.after(
                200, cerrar_taskmgr
            )
            chat.config(
                state='disable'
            )
            message_entry.config(
                state='normal'
            )
            message_entry.delete(
                0,
                END
            )
            chat.config(
                state='normal'
            )
        message_entry.delete(
            0,
            END
        )
        chat.config(
            state='normal'
        )
        chat.insert(
            END,
            f'\n    YO: {message}\n'
        )
        chat.after(
            200,
            answer_bot2
        )
        message_entry.delete(
            0,
            END
        )
        message_entry.config(
            state='disable'
        )
    else:
        messagebox.showerror(
            'ERROR', f'� La palabra [{message}] no esta en mi sistema. Espera nuevas actualizaciones �'
        )
        message_entry.delete(
            0,
            END
        )


def insert_chat_message(chat, message, message_entry, ventana, username):
    """Insert Message"""

    if message == '':
        pass
    else:
        insert_answer_greet(chat, message, message_entry, ventana, username)
