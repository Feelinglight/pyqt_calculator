pipeline {
    agent none

    stages {
        stage('BuildTestDeploy') {
            matrix {
                agent {
                    dockerfile {
                        filename "Dockerfile.${DOCKER_IMAGE}"
                        dir 'dockerfiles'
                        label 'docker'
                    }
                }

                axes {
                    axis {
                        name 'DOCKER_IMAGE'
                        values 'ubuntu_20'
                    }
                }

                stages {
//                     stage("Install common dependencies") {
//                         when { 
//                             anyOf {
//                                 environment name: 'DOCKER_IMAGE', value: 'ubuntu_20' 
//                             }
//                         }
//                         steps {
//                         }
//                     }
                    
//                     stage('Install custom dependencies') {
//                         when { 
//                             anyOf {
//                                 environment name: 'DOCKER_IMAGE', value: 'ubuntu_18' 
//                             }
//                         }
//                         steps {
                            
//                         }
//                     }
                    stage('Test') {
                        steps {
                            echo "Do Test for ${DOCKER_IMAGE}"
                            sh 'python3 -m pytest pyqt_dark_calculator/tests'
                        }
                    }
                    stage('Build') {
                        steps {
                            echo "Do Build for ${DOCKER_IMAGE}"
                            sh 'ls -la'
                            sh 'python3 build_deb.py'
                        }
                    }
                 }
            }
        }
    }
} 
