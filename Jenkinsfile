pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin/python3:/opt/homebrew/bin/pip3:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git branch: 'main', url: 'https://github.com/Akshar-code/hangman.git'
            }
        }

        stage('Build') {
            steps {
                // Install dependencies
                sh '/usr/local/bin/pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                // Run tests
                sh '/usr/local/bin/pytest'
            }
        }

        stage('Code Quality') {
            steps {
                // Run static code analysis
                sh '/usr/local/bin/pylint your_hangman_script.py'
            }
        }

        stage('Package') {
            steps {
                // Package the application
                sh '/usr/local/bin/python3 setup.py sdist'
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
            echo 'Cleaning up workspace...'
            deleteDir()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
