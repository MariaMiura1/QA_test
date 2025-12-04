# QA_test

Repositorio para practicar QA, pytest y Jenkins.
# Voice Command QA Practice

This repository contains a simple Python module that simulates how a virtual assistant processes voice commands in Spanish.  
The goal of this project is to practice software testing, test case design, error analysis, and basic automation using Python and pytest — all highly relevant skills for QA roles.

---

## 🎯 Project Overview

The system under test (SUT) is a function called `process_command`.  
It receives a user command as text (simulating a voice transcription) and returns the expected response from the device.

Example commands:
- `encender` → “Dispositivo encendido”
- `apagar` → “Dispositivo apagado”
- `subir volumen`
- `bajar volumen`
- `silencio`
- `ayuda`

If the command is not recognized, the system must return:

This behavior is covered by automated tests in the `tests` folder.

---

## 🧪 Testing Scope

The pytest suite includes the following test scenarios:

### ✔ Functional Tests
- Accept valid commands  
- Trim extra spaces  
- Handle uppercase inputs  
- Reject invalid commands  
- Reject partial or incomplete commands  

These tests simulate realistic user input variations, which are common in voice assistants and smart devices.

---

## 🛠 Technologies Used

- **Python 3**
- **pytest** (for test automation)
- Linux-based development environment (GitHub Codespaces)

---

## 📂 Project Structure

🐞 Example of Debugging (Real QA Scenario)

During development, multiple issues were intentionally introduced and diagnosed:

1. ModuleNotFoundError: No module named 'src'

Cause: Python did not recognize the src folder as a package.
Fix: Added __init__.py and updated test file to include the project root in sys.path.

2. Circular import error

Cause: The module was importing itself during initialization.
Fix: Removed unnecessary import inside voice_commands.py.

This demonstrates common debugging patterns in QA automation and Python environments.

📘 Purpose of This Project

This project was created to practice:

Requirement analysis

Manual and automated test design

Error detection and troubleshooting

Python scripting for QA

Working with test automation tools (pytest, CI-ready structure)

It serves as a hands-on example of how to approach testing functionality for virtual assistants, smart devices, or command-processing systems.

📬 Contact

If you’d like to discuss this project or QA practices, feel free to connect.