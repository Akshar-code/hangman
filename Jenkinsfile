pipeline {
    agent any

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
                sh 'source venv/bin/activate && pylint app.py || true'
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
