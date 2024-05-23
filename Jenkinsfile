pipeline {
    agent any
    environment {
        IMAGE_NAME = "quay.io/rh-ee-akottuva/hangman:latest"
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Akshar-code/hangman', branch: 'main'
            }
        }
        stage('Setup Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    source venv/bin/activate
                    export PYTHONPATH=$PYTHONPATH:$(pwd)
                    ./venv/bin/pytest
                '''
            }
        }
        stage('Build Container Image') {
            steps {
                sh '''
                    podman build -t ${IMAGE_NAME} .
                '''
            }
        }
        stage('Push to Quay') {
            steps {
                withCredentials([string(credentialsId: 'quay-io-secret', variable: 'QUAY_PASSWORD')]) {
                    sh '''
                        podman login quay.io -u rh-ee-akottuva+robot_hangman -p ${QUAY_PASSWORD}
                        podman push ${IMAGE_NAME}
                    '''
                }
            }
        }
        stage('Sign Image') {
            steps {
                withCredentials([string(credentialsId: 'cosign-password', variable: 'COSIGN_PASSWORD')]) {
                    sh '''
                        source tas-env-values
                        cosign initialize
                        cosign sign ${IMAGE_NAME} \
                            --fulcio-url=$COSIGN_FULCIO_URL \
                            --oidc-issuer=$COSIGN_OIDC_ISSUER \
                            --rekor-url=$COSIGN_REKOR_URL \
                            --upload=true \
                            --yes
                    '''
                }
            }
        }
    }
    post {
        always {
            cleanWs()
            echo "Pipeline finished"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
