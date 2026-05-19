pipeline {
    agent any
    stages {
        stage('Pull Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Jaafarkukhon/recommendation-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t recommendation-app /var/jenkins_home/workspace/recommendation-pipeline'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop rec-container || true'
                sh 'docker rm rec-container || true'
                sh 'docker run -d --name rec-container -p 5000:5000 -p 2222:22 recommendation-app'
            }
        }
        stage('Start SSH') {
            steps {
                sh 'docker exec rec-container bash -c "apt-get update && apt-get install -y openssh-server && echo root:1234 | chpasswd && sed -i \'s/#PermitRootLogin prohibit-password/PermitRootLogin yes/\' /etc/ssh/sshd_config && mkdir -p /run/sshd && /usr/sbin/sshd"'
            }
        }
    }
}