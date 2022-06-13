pipeline {
    agent none

    stages {
        stage('BuildTestDeploy') {
            matrix {
                node {
                    label 'docker'
                    def testImage = docker.build("${DOCKER_IMAGE}", "./dockerfiles/Dockerfile.ubuntu_20")
                }

                axes {
                    axis {
                        name 'DOCKER_IMAGE'
                        values 'ubuntu_20'
                    }
                }

                 stages {
                     agent {
                         docker {
                             label 'docker'
                             image "${DOCKER_IMAGE}"
                         }
                     }

                     stage('Clone repo') {
                         steps {
                             git branch: 'master', url: 'https://github.com/Feelinglight/pyqt_calculator/'
                         }
                     }
                     stage('Build') {
                         steps {
                             echo "Do Build for ${DOCKER_IMAGE}"
                             sh 'ls -la'

                             sh 'pip install .'
                         }
                     }
//                     stage('Test') {
//                         steps {
//                             echo "Do Test for ${DOCKER_IMAGE}"
//                         }
//                     }
                 }
            }
        }
    }
} 
