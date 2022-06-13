pipeline {
    agent none

    stages {
        stage('BuildTestDeploy') {
            matrix {
                agent {
                    // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
                    dockerfile {
                        filename "Dockerfile.${DOCKER_IMAGE}"
                        dir 'dockerfiles'
                        label 'docker'
//                         additionalBuildArgs  "-t ${DOCKER_IMAGE}"
//                         args '-v /tmp:/tmp'
                    }
                }

//                     agent {
//                         docker {
//                             label 'docker'
//                             image "${DOCKER_IMAGE}"
//                         }
//                     }

                axes {
                    axis {
                        name 'DOCKER_IMAGE'
                        values 'ubuntu_20'
                    }
                }

                stages {


                    stage('Clone repo') {
                        steps {
                            git branch: 'master', url: 'https://github.com/Feelinglight/pyqt_calculator/'
                        }
                    }
                    stage('Build') {
                        steps {
                            echo "Do Build for ${DOCKER_IMAGE}"
                            sh 'ls -la'
//                             sh 'pip install .'
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
