pipeline {
    agent any

    parameters {
        booleanParam(name: 'DRY_RUN', 
                defaultValue: false,
                description: 'Run the main.py of False only')
    }    

    stages {
        stage('Git checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Dima-Go/JenkinsTest1.git'
            }
        }
        stage('Run Python Program') {
            when {
                expression { return !params.DRY_RUN }
            }
            steps {
               sh 'python3 main.py >> output.txt'
            }
        }
        stage('Report') {
            steps {
                echo "This stage generates a report"
                sh 'cat output.txt'
                archiveArtifacts allowEmptyArchive: true,
                    artifacts: '*.txt',
                    fingerprint: true,
                    followSymlinks: false,
                    onlyIfSuccessful: true
            }
        }
        
    }
}
