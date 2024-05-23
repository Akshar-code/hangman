pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git 'https://github.com/Akshar-code/hangman.git'
            }
        }

        stage('Build') {
            steps {
                // Install dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                // Run tests
                sh 'pytest'
            }
        }

        stage('Code Quality') {
            steps {
                // Run static code analysis
                sh 'pylint your_hangman_script.py'
            }
        }

        stage('Package') {
            steps {
                // Package the application
                sh 'python setup.py sdist'
            }
        }

        stage('Deploy') {
            steps {
                // Deploy the application
                echo 'Deploying application...'
                // Example: sh 'scp dist/yourapp.tar.gz user@server:/path/to/deploy'
            }
        }

        stage('Notify') {
            steps {
                // Notify team members
                echo 'Build and deployment complete!'
            }
        }
    }

    post {
        always {
            // Clean up workspace
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
