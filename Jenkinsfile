pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm 
            }
        }
        stage('Build') {
            steps {
                sh 'make'  // Replace with your actual build command
            }
        }
        stage('Test') {
            steps {
                sh 'make test' // Replace with your test command
            }
        }
        stage('Deploy') {
            steps {
                // Add your deployment steps here
            }
        }
    }
}
