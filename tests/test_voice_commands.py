from voice_commands import process_command


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


def test_none_input():
    assert process_command(None) == "Comando no reconocido"
