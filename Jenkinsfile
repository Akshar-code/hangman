pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git branch: 'main', url: 'https://github.com/Akshar-code/hangman.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create virtual environment
                sh '/opt/homebrew/bin/python3 -m venv venv'
                // Activate virtual environment and install dependencies
                sh '''
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip list
                '''
            }
        }

        stage('Test') {
            steps {
                // Activate virtual environment, set PYTHONPATH and run tests
                sh '''
                    source venv/bin/activate
                    export PYTHONPATH=$WORKSPACE
                    which python
                    which pip
                    which pytest
                    pytest
                '''
            }
        }

        stage('Code Quality') {
            steps {
                // Activate virtual environment and run static code analysis
                sh '''
                    source venv/bin/activate
                    pylint app.py
                '''
            }
        }

        stage('Package') {
            steps {
                // Activate virtual environment and package the application
                sh '''
                    source venv/bin/activate
                    python setup.py sdist
                '''
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
