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
                sh 'docker run 2022bcd0051-model'
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