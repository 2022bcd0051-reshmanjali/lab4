pipeline {
    agent any

    stages {

        stage('Build Image') {
            steps {
                sh 'docker build -t 2022bcd0051-model .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop ml-container || true
                docker rm ml-container || true
                docker run -d -p 8002:8000 --name ml-container 2022bcd0051-model
                '''
            }
        }

        stage('Wait for API') {
            steps {
                script {
                    sleep 10
                }
            }
        }

        stage('Valid Inference Test') {
            steps {
                script {
                    def response = sh(
                        script: '''
                        curl -s -X POST http://host.docker.internal:8002/predict \
                        -H "Content-Type: application/json" \
                        -d '{"feature1": 5, "feature2": 3}'
                        ''',
                        returnStdout: true
                    ).trim()

                    echo "Valid Response: ${response}"

                    if (!response.contains("prediction")) {
                        error("Valid input failed: prediction not found")
                    }
                }
            }
        }

        stage('Invalid Inference Test') {
            steps {
                script {
                    def response = sh(
                        script: '''
                        curl -s -X POST http://host.docker.internal:8002/predict \
                        -H "Content-Type: application/json" \
                        -d '{"wrong": "data"}'
                        ''',
                        returnStdout: true
                    ).trim()

                    echo "Invalid Response: ${response}"

                    if (!response.toLowerCase().contains("error")) {
                        error("Invalid input did not return expected error")
                    }
                }
            }
        }

        stage('Stop Container') {
            steps {
                sh '''
                docker stop ml-container || true
                docker rm ml-container || true
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline Passed ✅"
        }
        failure {
            echo "Pipeline Failed ❌"
        }
    }
}