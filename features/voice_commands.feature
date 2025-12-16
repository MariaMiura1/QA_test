Feature: Procesamiento de comandos de voz en español
  Como usuario
  Quiero que el asistente entienda comandos
  Para controlar el dispositivo de forma fiable

  Scenario Outline: Comandos válidos devuelven la respuesta esperada
    Given the assistant is ready
    When I say "<command>"
    Then the response should be "<response>"

    Examples:
      | command        | response               |
      | encender       | Dispositivo encendido  |
      | apagar         | Dispositivo apagado    |
      | SUBIR VOLUMEN  | Volumen aumentado      |
      | bajar volumen  | Volumen reducido       |
      | silencio       | Modo silencio activado |

  Scenario: Comando inválido
    Given the assistant is ready
    When I say "volar"
    Then the response should be "Comando no reconocido"

  Scenario: Comando parcial no debe aceptarse
    Given the assistant is ready
    When I say "subir"
    Then the response should be "Comando no reconocido"

  Scenario: Espacios extra se ignoran
    Given the assistant is ready
    When I say "  apagar  "
    Then the response should be "Dispositivo apagado"
