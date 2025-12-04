VALID_COMMANDS = {
    "encender": "Dispositivo encendido",
    "apagar": "Dispositivo apagado",
    "subir volumen": "Volumen aumentado",
    "bajar volumen": "Volumen reducido",
    "silencio": "Modo silencio activado",
    "ayuda": "Estos son los comandos disponibles: encender, apagar..."
}

def process_command(command: str) -> str:
    command = command.lower().strip()
    return VALID_COMMANDS.get(command, "Comando no reconocido")
