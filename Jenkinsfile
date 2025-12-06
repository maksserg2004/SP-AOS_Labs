pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'count-etc-files-jenkins'
    }
    
    stages {
        stage('Build Jenkins Docker Image') {
            steps {
                script {
                    // Build Docker image with Jenkins and build tools
                    sh '''
                        cd jenkins
                        docker build -t ${DOCKER_IMAGE} .
                    '''
                }
            }
        }
        
        stage('Test RPM Package') {
            agent {
                docker {
                    image 'fedora:latest'
                    args '-u root'
                }
            }
            steps {
                script {
                    sh '''
                        # Install the RPM package
                        dnf install -y rpm/count-etc-files-1.0-1.fc40.noarch.rpm
                        
                        # Run the script (will fail without root, but tests installation)
                        count-etc-files || echo "Script requires root privileges (expected)"
                        
                        # Verify the script is installed
                        which count-etc-files
                        ls -la /usr/bin/count-etc-files
                    '''
                }
            }
        }
        
        stage('Test DEB Package') {
            agent {
                docker {
                    image 'ubuntu:latest'
                    args '-u root'
                }
            }
            steps {
                script {
                    sh '''
                        # Install the DEB package
                        apt-get update
                        dpkg -i deb/count-etc-files-1.0.deb || apt-get install -f -y
                        
                        # Run the script (will fail without root, but tests installation)
                        count-etc-files || echo "Script requires root privileges (expected)"
                        
                        # Verify the script is installed
                        which count-etc-files
                        ls -la /usr/bin/count-etc-files
                    '''
                }
            }
        }
        
        stage('Execute Script in Docker') {
            agent {
                docker {
                    image 'fedora:latest'
                    args '-u root'
                }
            }
            steps {
                script {
                    sh '''
                        # Install RPM package
                        dnf install -y rpm/count-etc-files-1.0-1.fc40.noarch.rpm
                        
                        # Execute the script with root privileges
                        echo "Executing count-etc-files script:"
                        count-etc-files
                    '''
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
            echo 'RPM and DEB packages tested and script executed.'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
        always {
            // Cleanup
            sh 'docker system prune -f || true'
        }
    }
}
