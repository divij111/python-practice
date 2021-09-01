pipeline {
    agent none
    
    stages {
//          stage('Initialize'){
//         def dockerHome = tool 'myDocker'
//         env.PATH = "${dockerHome}/bin:${env.PATH}"
//             }
        stage('Build') {
                agent{
                    docker{
                        image 'python:2-alpine'
                    }
                }
                steps{
                    sh 'python -m py_compile sources/wish.py'
                    stash(name: 'compiled-results', includes: 'sources/wish.py')
                }
        }
    }
}
