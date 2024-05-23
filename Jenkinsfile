pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'quay.io/rh-ee-akottuva/hangman:latest'
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
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        ./venv/bin/pip install --upgrade pip
                        ./venv/bin/pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh '''
                        source venv/bin/activate
                        ./venv/bin/pytest
                    '''
                }
            }
        }

        stage('Build Container Image') {
            steps {
                script {
                    sh '''
                        podman build -t ${DOCKER_IMAGE} .
                        podman push ${DOCKER_IMAGE}
                        export IMAGE_DIGEST=$(podman inspect --format='{{index .RepoDigests 0}}' ${DOCKER_IMAGE})
                    '''
                }
            }
        }

        stage('Push to Quay') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'quay-robot-account-password', variable: 'QUAY_PASSWORD')]) {
                        sh '''
                            podman login quay.io -u rh-ee-akottuva+robot_hangman -p $QUAY_PASSWORD
                            podman push ${DOCKER_IMAGE}
                        '''
                    }
                }
            }
        }

        stage('Sign Image') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'cosign-password', variable: 'COSIGN_PASSWORD')]) {
                        sh '''
                            source tas-env-values
                            cosign initialize
                            export COSIGN_TIMEOUT=${COSIGN_TIMEOUT}
                            COSIGN_PASSWORD=$COSIGN_PASSWORD cosign sign ${IMAGE_DIGEST}
                        '''
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
