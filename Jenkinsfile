pipeline{
    agent any

    stages{
        stage('Cloning Github Repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github Repo to Jenkins..................'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/varmatilak22/Hotel_Reservation_Prediction.git']])
                }
            }
        }
    }
}