pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/MoMkhan1/customer-retention-mlops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t customer-retention-app .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
                    sh 'docker tag customer-retention-app $DOCKER_USER/customer-retention-app:latest'
                    sh 'docker push $DOCKER_USER/customer-retention-app:latest'
                }
            }
        }
    }
}
