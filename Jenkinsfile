pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Akshar-code/hangman'
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
                sh 'source venv/bin/activate && pytest'
            }
        }
        stage('Code Quality') {
            steps {
                // Allow pylint to run and collect issues, but don't fail the pipeline if pylint fails
                sh 'source venv/bin/activate && pylint app.py || true'
            }
        }
        stage('Package') {
            steps {
                // Add packaging steps here
                sh 'echo "Packaging the application..."'
            }
        }
        stage('Deploy') {
            steps {
                // Add deployment steps here
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
