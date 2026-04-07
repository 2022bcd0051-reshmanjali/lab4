pipeline {
    agent any

    stages {

        stage('Build Image') {
            steps {
                sh 'docker build -t 2022bcd0051-model .'
            }
        }

        stage('Run Model') {
            steps {
                sh 'docker run -d -p 8000:8000 --name ml-container 2022bcd0051-model'
            }
        }

        stage('Wait for API') {
            steps {
                script {
                    sleep 10
                }
            }
        }

        stage('Valid Request Test') {
            steps {
                sh '''
                curl -X POST http://localhost:8000/predict \
                -H "Content-Type: application/json" \
                -d '{"feature1": 5, "feature2": 3}'
                '''
            }
        }

        stage('Invalid Request Test') {
            steps {
                sh '''
                curl -X POST http://localhost:8000/predict \
                -H "Content-Type: application/json" \
                -d '{"wrong": "data"}'
                '''
            }
        }

        stage('Stop Container') {
            steps {
                sh 'docker stop ml-container || true'
                sh 'docker rm ml-container || true'
            }
        }

        stage('Print Details') {
            steps {
                echo "Name: Reshmanjali Maddula"
                echo "Roll No: 2022BCD0051"
            }
        }
    }
}