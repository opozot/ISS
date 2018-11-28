pipeline {
    agent { docker { image 'python:3.7.1' } }
    stages {
        stage('build') {
            steps {
                sh 'apt-get update && apt-get install -y python3-pip'
            }
            steps {
                sh 'pip install requests'
            }
        }
    }
}
