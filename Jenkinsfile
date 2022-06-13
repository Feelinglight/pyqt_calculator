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

                axes {
                    axis {
                        name 'DOCKER_IMAGE'
                        values 'ubuntu_20'
                    }
                }

                stages {
                    stage("Install common dependencies") {
                        when { 
                            anyOf {
                                environment name: 'DOCKER_IMAGE', value: 'ubuntu_20' 
                            }
                        }
                        steps {
//                             environment {
//                                 HOME = "${env.WORKSPACE}"
//                             }
                            
                            echo "${HOME}"
                            echo "${USER}"
                            echo "${env.WORKSPACE}"
                            
//                             withPythonEnv('python3') {
                            sh 'pip install . --user'
//                             }
                        }
                    }
                    
                    stage('Install custom dependencies') {
                        when { 
                            anyOf {
                                environment name: 'DOCKER_IMAGE', value: 'ubuntu_18' 
                            }
                        }
                        steps {
                            sh 'python3 -m venv venv'
                            sh '. ./venv/bin/activate'
                            
                            sh '''pip3 install --no-deps 
                            wheel pyinstaller==4.0 
                            pyqt-new-window-handler absresgetter 
                            pyqt-resource-helper pyqt-style-setter altgraph
                            '''
                        }
                    }
                    
                    stage('Build') {
                        steps {
                            echo "Do Build for ${DOCKER_IMAGE}"
                            sh 'ls -la'
                            sh 'ls /tmp'
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
