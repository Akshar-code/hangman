pipeline {
    agent any

    environment {
        APP_DIR = "/Users/akottuva/Documents/Redhat work stuff/Sample Projects/hangman"
        IMAGE_NAME = "hangman-app"
        TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: '*/main']],
                        userRemoteConfigs: [[url: 'https://github.com/Akshar-code/hangman']]
                    ])
                }
            }
        }
        stage('Copy app.py') {
            steps {
                sh '''
                cp "${APP_DIR}/app.py" .
                cp "${APP_DIR}/requirements.txt" .
                '''
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
                sh '''
                source venv/bin/activate
                export PYTHONPATH=$WORKSPACE
                pytest
                '''
            }
        }
        stage('Code Quality') {
            steps {
                sh '''
                source venv/bin/activate
                pylint app.py || true
                '''
            }
        }
        stage('Build with Podman') {
            steps {
                sh '''
                # Create a simple Dockerfile for the application
                cat <<EOF > Dockerfile
                FROM python:3.9-slim
                WORKDIR /app
                COPY app.py requirements.txt /app/
                RUN pip install --no-cache-dir -r requirements.txt
                CMD ["python", "app.py"]
                EOF
                
                # Build the container image using Podman
                podman build -t ${IMAGE_NAME}:${TAG} .
                '''
            }
        }
        stage('Push Image') {
            steps {
                sh '''
                # Login to container registry (if necessary)
                # podman login -u $REGISTRY_USER -p $REGISTRY_PASSWORD $REGISTRY_URL
                
                # Push the image to the container registry (if necessary)
                # podman push ${IMAGE_NAME}:${TAG}
                echo "Skipping push for this example..."
                '''
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
