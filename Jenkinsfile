pipeline {
  agent any

  environment {
    VENV_DIR = 'venv'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup venv via virtualenv') {
      steps {
        sh '''
          # Install virtualenv in your user space
          python3 -m pip install --user virtualenv

          # Create a venv (bundled pip/ensurepip)
          python3 -m virtualenv ${VENV_DIR}

          # Activate and install your package
          . ${VENV_DIR}/bin/activate
          pip install --upgrade pip
          pip install -e .
        '''
      }
    }
  }
}
