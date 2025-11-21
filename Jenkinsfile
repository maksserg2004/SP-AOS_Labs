pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Test RPM on Fedora') {
            steps {
                sh '''
                    docker run --privileged -v ${WORKSPACE}:/workspace fedora:latest bash -c "
                        cd /workspace
                        dnf install -y rpm/count-etc-files-1.0-1.fc40.noarch.rpm
                        count-etc-files
                    "
                '''
            }
        }
        
        stage('Test DEB on Ubuntu') {
            steps {
                sh '''
                    docker run --privileged -v ${WORKSPACE}:/workspace ubuntu:22.04 bash -c "
                        cd /workspace
                        apt-get update
                        dpkg -i deb/count-etc-files-1.0.deb || apt-get install -f -y
                        count-etc-files
                    "
                '''
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
