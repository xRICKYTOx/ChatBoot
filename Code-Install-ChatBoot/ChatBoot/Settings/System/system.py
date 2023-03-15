"""Close App for system"""

from subprocess import call, Popen
from os import system


def terminar_app():
    """Terminar la ejecución de la aplicación en el sistema"""
    call(
        [
            "taskkill",
            "/f",
            "/im",
            "CHAT-BOOT.exe"
        ]
    )


def abrir_block_notas():
    """Abre la aparición de block de notas"""
    Popen(
        [
            'notepad.exe'
        ],
        start_new_session=True
    )


def cerrar_block_notas():
    """Cierra la aplicación de block de notas"""
    Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'notepad.exe'
        ]
    )


def abrir_calculadora():
    """Abre la aplicación de la calculadora"""
    system(
        'start calc'
    )


def cerrar_calculadora():
    """Cierra la aplicación de la calculadora"""
    Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'CalculatorApp.exe'
        ]
    )


def cerrar_navegador():
    """Cierra el navegador predeterminado"""
    call(
        [
            'taskkill',
            '/f',
            '/im',
            'msedge.exe'
        ]
    )
    call(
        [
            'taskkill',
            '/f',
            '/im',
            'brave.exe'
        ]
    )
    call(
        [
            'taskkill',
            '/f',
            '/im',
            'chrome.exe'
        ]
    )
    call(
        [
            'taskkill',
            '/f',
            '/im',
            'opera.exe'
        ]
    )
    call(
        [
            'taskkill',
            '/f',
            '/im',
            'firefox.exe'
        ]
    )


def abrir_musica():
    """Abrir mi aplicación de música"""
    Popen(
        [
            'iTunes.exe'
        ]
    )

    Popen(
        [
            'Spotify.exe'
        ]
    )


def cerrar_musica():
    """Cierra mi aplicación de música"""
    Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'iTunes.exe'
        ]
    )
    Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'Spotify.exe'
        ]
    )


def abrir_itunes():
    """Abrir la aplicación de iTunes"""
    Popen(
        [
            'iTunes.exe'
        ]
    )


def cerrar_itunes():
    """Cerrar la aplicación de iTunes"""
    Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'iTunes.exe'
        ]
    )


def abrir_spotify():
    """Abrir la aplicación de Spotify"""
    Popen(
        [
            'Spotify.exe'
        ]
    )


def cerrar_spotify():
    """Cerrar la aplicación de Spotify"""
    Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'Spotify.exe'
        ]
    )


def abrir_explorador_archivos():
    """Abre la aplicación Explorador de Archivos"""
    Popen(
        [
            'explorer.exe'
        ]
    )


def abrir_riot_games():
    """Abre la aplicación de Riot Games"""
    Popen(
        [
            'RiotClientServices.exe'
        ]
    )


def cerrar_riot_games():
    """Cierra la aplicación de Riot Games"""
    Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'RiotClientServices.exe'
        ]
    )


def abrir_visual_studio_code():
    """Abrir la aplicación de VSC"""
    system(
        'Code'
    )


def cerrar_visual_studio_code():
    """Cerrar la aplicación de VSC"""
    Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'Code.exe'
        ]
    )


def abrir_taskmgr():
    """Abre la aplicación Task Manager"""
    Popen(
        [
            'Taskmgr.exe'
        ]
    )


def cerrar_taskmgr():
    """Cerrar la aplicacion Task Manager"""
    Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'Taskgmr.exe'
        ]
    )