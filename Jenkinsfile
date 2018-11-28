pipeline {
    agent { docker { image 'python:3.7.1' } }
    stages {
        stage('build') {
            steps {
                sh 'apt-get update && apt-get install python3-pip'
            }
        }
    }
}
