pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'quay.io/rh-ee-akottuva/tas-registry:latest'
        COSIGN_PASSWORD = credentials('cosign_password')
        ROOT_DIR = '/Users/akottuva/.jenkins/workspace/Hangman Python Application'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Akshar-code/hangman'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    source venv/bin/activate
                    export PYTHONPATH=${ROOT_DIR}
                    pytest
                '''
            }
        }

        stage('Build Container Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }

        stage('Push to Quay') {
            steps {
                script {
                    docker.withRegistry('https://quay.io', 'quay_credentials') {
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }

        stage('Sign Image') {
            steps {
                sh '''
                    source tas-env-values
                    cosign sign --key env://COSIGN_PASSWORD ${DOCKER_IMAGE}:latest
                '''
            }
        }

        stage('Verify Image') {
            steps {
                sh '''
                    source tas-env-values
                    cosign verify ${DOCKER_IMAGE}:latest
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
