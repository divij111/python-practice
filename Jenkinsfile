pipeline {
    agent any

    stages {
        stage('Build') {
                agent{
                    docker{
                        image 'python'
                    }
                }
                steps{
                    sh 'python -m py_compile sources/wish.py'
                    stash(name: 'compiled-results', includes: 'sources/wish.py')
                }
        }
    }
}