pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/Akshar-code/hangman'
        BRANCH = 'main'
        IMAGE_NAME = 'tas-registry'
        IMAGE_TAG = 'latest'
        QUAY_REGISTRY = 'quay.io'
        QUAY_NAMESPACE = 'rh-ee-akottuva'  // Replace with your Quay namespace
        CREDENTIALS_ID = 'quay-credentials'  // The ID of the credentials you added in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                git url: "${env.REPO_URL}", branch: "${env.BRANCH}"
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

        stage('Build Container Image') {
            steps {
                script {
                    sh '''
                    podman build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    podman tag ${IMAGE_NAME}:${IMAGE_TAG} ${QUAY_REGISTRY}/${QUAY_NAMESPACE}/${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }

        stage('Push to Quay') {
            steps {
                withCredentials([usernamePassword(credentialsId: env.CREDENTIALS_ID, usernameVariable: 'QUAY_USERNAME', passwordVariable: 'QUAY_PASSWORD')]) {
                    script {
                        sh '''
                        podman login ${QUAY_REGISTRY} -u ${QUAY_USERNAME} -p ${QUAY_PASSWORD}
                        podman push ${QUAY_REGISTRY}/${QUAY_NAMESPACE}/${IMAGE_NAME}:${IMAGE_TAG}
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
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
