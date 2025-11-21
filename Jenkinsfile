pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Test RPM on Fedora') {
            agent {
                docker {
                    image 'fedora:latest'
                    args '--privileged'
                }
            }
            steps {
                sh '''
                    echo "Installing RPM package..."
                    dnf install -y rpm/count-etc-files-1.0-1.fc40.noarch.rpm
                    
                    echo "Running the script..."
                    count-etc-files
                '''
            }
        }
        
        stage('Test DEB on Ubuntu') {
            agent {
                docker {
                    image 'ubuntu:22.04'
                    args '--privileged'
                }
            }
            steps {
                sh '''
                    echo "Installing DEB package..."
                    apt-get update
                    dpkg -i deb/count-etc-files-1.0.deb || apt-get install -f -y
                    
                    echo "Running the script..."
                    count-etc-files
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
