pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'quay.io/rh-ee-akottuva/tas-registry:latest'
        PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate && pip install --upgrade pip'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Akshar-code/hangman'
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'source venv/bin/activate && export PYTHONPATH=${WORKSPACE} && pytest'
                }
            }
        }

        stage('Build Container Image') {
            steps {
                script {
                    sh "podman build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Push to Quay') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'quay-robot-account-password', passwordVariable: 'QUAY_PASSWORD', usernameVariable: 'QUAY_USERNAME')]) {
                        sh "podman login quay.io -u $QUAY_USERNAME -p $QUAY_PASSWORD"
                        sh "podman push ${DOCKER_IMAGE}"
                    }
                }
            }
        }

        stage('Sign Image') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'cosign-password', variable: 'COSIGN_PASSWORD')]) {
                        sh 'source tas-env-values'
                        sh 'cosign initialize'
                        sh "COSIGN_PASSWORD=$COSIGN_PASSWORD cosign sign ${DOCKER_IMAGE}"
                    }
                }
            }
        }

        stage('Verify Image') {
            steps {
                script {
                    sh 'source tas-env-values'
                    sh "cosign verify ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
