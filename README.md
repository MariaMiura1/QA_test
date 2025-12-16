# Voice Command QA Practice

This repository contains a simple Python project designed to practice **software testing and QA automation** using `pytest`, code quality checks, **BDD (Cucumber-style)**, and a CI pipeline with **Jenkins**.

The system under test (SUT) simulates how a virtual assistant processes **voice commands in Spanish** and returns predefined responses.

This project focuses on **test design, edge cases, automation, and CI**, rather than complex business logic.

---

## 🎯 Project Overview

The core function, `process_command`, receives a text command (simulating a voice transcription) and returns the expected device response.

### Supported commands

| Command       | Response                                  |
|--------------|--------------------------------------------|
| encender     | Dispositivo encendido                      |
| apagar       | Dispositivo apagado                        |
| subir volumen| Volumen aumentado                          |
| bajar volumen| Volumen reducido                           |
| silencio     | Modo silencio activado                     |
| ayuda        | Estos son los comandos disponibles: encender, apagar... |

Any unknown, partial, empty, or invalid input returns:



Comando no reconocido


---

## 🧪 Testing Scope

Automated tests are written with **pytest** and cover:

- Valid commands
- Case-insensitive input
- Leading and trailing spaces
- Invalid and partial commands
- Edge cases (e.g. `None` input)

Additionally, the repo includes **BDD scenarios (Cucumber-style)** using **Gherkin** + **Behave**:

- Human-readable functional scenarios (`Given / When / Then`)
- Executable requirements for the command behavior

The project follows a clear separation between:
- **Source code** (`src/`)
- **Test code** (`tests/`)
- **BDD features** (`features/`)

---
## 📂 Project Structure

.
├── src/
│ ├── init.py
│ └── voice_commands.py
├── tests/
│ └── test_voice_commands.py
├── features/
│ ├── voice_commands.feature
│ └── steps/
│ └── voice_steps.py
├── pyproject.toml
├── requirements.txt
├── Jenkinsfile
└── README.md

yaml
Copiar código

---

## ▶️ How to Run Locally (Linux / Codespaces)

### 1) Create and activate a virtual environment

```bash
python -m venv .venv
. .venv/bin/activate
2) Install dependencies and the project
bash
Copiar código
python -m pip install -U pip
python -m pip install -r requirements.txt
python -m pip install -e .
🔍 Code Quality (Lint)
bash
Copiar código
ruff check .
🧪 Run Unit Tests (pytest)
bash
Copiar código
python -m pytest -q
📊 Run Tests with Coverage
bash
Copiar código
python -m pytest --cov=src --cov-report=term-missing --cov-report=xml
This generates:

Console coverage report

coverage.xml file (used in CI)

🥒 BDD (Cucumber-style) with Behave
Run BDD scenarios:

bash
Copiar código
python -m behave
Feature files are located in features/ and step definitions in features/steps/.

✅ Run Everything (quick command)
bash
Copiar código
ruff check . && python -m pytest -q && python -m behave
🤖 Continuous Integration (Jenkins)
This repository includes a Jenkinsfile that defines a CI pipeline with the following stages:

Create virtual environment and install dependencies

Run lint checks with ruff

Execute unit tests with pytest

Generate coverage report and fail the build if coverage drops below 90%

Publish JUnit test results and archive coverage artifacts

Run BDD scenarios with Behave (Cucumber-style)

This setup reflects a realistic QA automation pipeline used in professional environments.

🧠 QA Concepts Practiced
Test case design (positive, negative, edge cases)

Input normalization and validation

Automated testing with pytest

BDD using Gherkin + Behave (Cucumber-style)

Code quality enforcement (linting)

Test coverage analysis

CI pipeline with Jenkins

Debugging Python import and environment issues

🚀 Future Improvements
Add tags for BDD (@smoke, @regression) and reporting

More input normalization (punctuation, accents)

Parametrized test data and additional edge cases

API layer for integration testing (FastAPI)

