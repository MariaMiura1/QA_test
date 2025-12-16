pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Setup venv + deps') {
      steps {
        sh 'python3 -m venv .venv'
        sh '. .venv/bin/activate && python3 -m pip install -U pip'
        sh '. .venv/bin/activate && python3 -m pip install -r requirements.txt'
        sh '. .venv/bin/activate && python3 -m pip install -e .'
      }
    }

    stage('Lint (ruff)') {
      steps {
        sh '. .venv/bin/activate && ruff check .'
      }
    }

    stage('Tests + Coverage') {
      steps {
        sh '. .venv/bin/activate && mkdir -p reports'
        sh '. .venv/bin/activate && python3 -m pytest -q --junitxml=reports/junit.xml --cov=src --cov-report=term-missing --cov-report=xml --cov-fail-under=90'
      }
      post {
        always {
          junit 'reports/junit.xml'
          archiveArtifacts artifacts: 'coverage.xml, reports/junit.xml', fingerprint: true, allowEmptyArchive: true
        }
      }
    }

    stage('BDD (Behave)') {
      steps {
        sh '. .venv/bin/activate && python3 -m pip install -r requirements.txt'
        sh '. .venv/bin/activate && python3 -m behave'
      }
    }
  }
}
