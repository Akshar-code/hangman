pipeline {
    agent any

    environment {
        APP_DIR = "/Users/akottuva/Documents/Redhat work stuff/Sample Projects/hangman"
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: '*/main']],  // Ensure this matches your branch name
                        userRemoteConfigs: [[url: 'https://github.com/Akshar-code/hangman']]
                    ])
                }
            }
        }
        stage('Copy app.py') {
            steps {
                sh '''
                cp "${APP_DIR}/app.py" .
                '''
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install --upgrade pip'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh '''
                source venv/bin/activate
                export PYTHONPATH=$WORKSPACE
                pytest
                '''
            }
        }
        stage('Code Quality') {
            steps {
                sh '''
                source venv/bin/activate
                pylint app.py || true
                '''
            }
        }
        stage('Package') {
            steps {
                sh 'echo "Packaging the application..."'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying the application..."'
            }
        }
    }
    post {
        always {
            cleanWs()
            echo 'Pipeline finished!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
