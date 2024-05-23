pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'quay.io/rh-ee-akottuva/tas-registry:latest'
        PYTHONPATH = "${env.WORKSPACE}"
        COSIGN_TIMEOUT = '300'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Akshar-code/hangman', branch: 'main'
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'source venv/bin/activate'
                    sh 'pytest'
                }
            }
        }

        stage('Build Container Image') {
            steps {
                script {
                    sh "podman build -t ${DOCKER_IMAGE} ."
                    sh "podman push ${DOCKER_IMAGE}"
                    env.IMAGE_DIGEST = sh(script: "podman inspect --format='{{index .RepoDigests 0}}' ${DOCKER_IMAGE}", returnStdout: true).trim()
                }
            }
        }

        stage('Sign Image') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'cosign-password', variable: 'COSIGN_PASSWORD')]) {
                        sh 'source tas-env-values'
                        sh 'cosign initialize'
                        sh "export COSIGN_TIMEOUT=${COSIGN_TIMEOUT}"
                        sh "COSIGN_PASSWORD=$COSIGN_PASSWORD cosign sign ${env.IMAGE_DIGEST}"
                    }
                }
            }
        }

        stage('Push to Quay') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'quay-robot-account-password', variable: 'QUAY_PASSWORD')]) {
                        sh "podman login quay.io -u rh-ee-akottuva+robot_hangman -p $QUAY_PASSWORD"
                        sh "podman push ${DOCKER_IMAGE}"
                    }
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
