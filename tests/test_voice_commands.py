import os
import sys

# Añado la carpeta raíz del proyecto al sys.path para que Python encuentre 'src'
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.voice_commands import process_command


def test_valid_command():
    assert process_command("encender") == "Dispositivo encendido"


def test_valid_command_with_spaces():
    assert process_command("  apagar  ") == "Dispositivo apagado"


def test_valid_command_uppercase():
    assert process_command("SUBIR VOLUMEN") == "Volumen aumentado"


def test_invalid_command():
    assert process_command("volar") == "Comando no reconocido"


def test_partial_command():
    assert process_command("subir") == "Comando no reconocido"
