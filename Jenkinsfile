pipeline {
    agent any

    environment {
        // Використовуємо DEB-пакет, оскільки він більш поширений у базових образах
        DEB_PACKAGE = 'deb/count-etc-files-1.0.deb'
        SCRIPT_NAME = 'count-etc-files'
    }

    stages {
        stage('Build Jenkins Docker Image') {
            steps {
                script {
                    // Цей етап потрібен, якщо Jenkins Master не має необхідних інструментів
                    // Але для фінального завдання ми можемо його пропустити, якщо використовуємо agent { docker { ... } }
                    // Залишаємо для повноти, якщо користувач хоче його зберегти
                    sh '''
                        cd jenkins
                        docker build -t count-etc-files-jenkins .
                    '''
                }
            }
        }

        stage('Install and Execute DEB Package') {
            agent {
                // Використовуємо образ Debian-based, оскільки DEB-пакет для нього
                docker {
                    image 'debian:stable-slim'
                    // Запускаємо як root, щоб мати доступ до /etc та можливість встановлювати пакети
                    args '-u root'
                }
            }
            steps {
                script {
                    sh '''
                        echo "--- Updating package list and installing dependencies ---"
                        apt-get update -y
                        apt-get install -y wget sudo dpkg

                        echo "--- Installing DEB package ---"
                        # Встановлюємо пакет. dpkg -i може вимагати залежностей,
                        # тому використовуємо apt-get install -f -y для їх встановлення.
                        dpkg -i ${DEB_PACKAGE} || apt-get install -f -y

                        echo "--- Verifying script installation ---"
                        which ${SCRIPT_NAME}
                        ls -la /usr/bin/${SCRIPT_NAME}

                        echo "--- Executing the script from step 2 ---"
                        # Виконуємо встановлений скрипт.
                        # Він повинен вивести кількість файлів у /etc.
                        /usr/bin/${SCRIPT_NAME}
                    '''
                }
            }
        }
    }
}
