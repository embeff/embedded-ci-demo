pipeline {
    agent { label 'amd64' }
    stages {
        stage("Compile") {
            parallel {
                stage('STM32F407'){
                    steps {
                        echo 'Compiling for STM32F407'
                        sh 'docker build -t embedded-ci-demo:${GIT_COMMIT} .'
                        sh 'docker run --rm embedded-ci-demo:${GIT_COMMIT} bash -c "cmake --version && gcc --version && arm-none-eabi-gcc --version"'
                        sh 'docker run --rm -v $(pwd):/build -w /build embedded-ci-demo:${GIT_COMMIT} bash -c "mkdir -p build && cd build && cmake -G Ninja -DCMAKE_TOOLCHAIN_FILE:FILEPATH=cmake/arm_gcc_toolchain.cmake -DTargetPlatform:STRING=STM32F4 -DBSP_DIR:STRING=target_bsp_stm32f407  .. && ninja"'
                    }
                }
            }
        }

        stage("Unit tests") {
            parallel {
                stage('x86') {
                    steps {
                        echo 'Compiling UnitTests for x86'
                        sh 'docker run --rm -v $(pwd):/build -w /build embedded-ci-demo:${GIT_COMMIT} bash -c "mkdir -p build-ut-x86 && cd build-ut-x86 && cmake -G Ninja -DBSP_DIR:STRING=target_bsp_stm32f407  .. && ninja"'
                        echo 'Running unit tests on x86'
                        sh 'docker run --rm -v $(pwd):/build -w /build embedded-ci-demo:${GIT_COMMIT} ./build-ut-x86/src/example_gtest'
                        
                    }
                }
                stage('STM32F407') {
                    steps {
                        echo 'Compiling UnitTests for STM32F407'
                        sh 'docker run --rm -v $(pwd):/build -w /build embedded-ci-demo:${GIT_COMMIT} bash -c "mkdir -p build-ut && cd build-ut && cmake -G Ninja -DCMAKE_TOOLCHAIN_FILE:FILEPATH=cmake/arm_gcc_toolchain.cmake -DTargetPlatform:STRING=STM32F4 -DBSP_DIR:STRING=target_bsp_stm32f407  .. && ninja"'
                        echo 'Running unit tests on STM32F407'
                        sh 'docker run --rm -v $(pwd):/build -w /build embedded-ci-demo:${GIT_COMMIT} bash ./ep-cli/ep.sh build-ut/src/example_gtest.bin'
                    }
                }
            }
        }

        stage("Code analysis") {
            parallel {
                stage('Style check') {
                    steps {
                        echo 'Running clang-format'
                    }
                }
                stage('Static analysis') {
                    steps {
                        echo 'Running cppcheck'
                    }
                }
            }
        }
      
        stage('HW-SW Integration'){
            steps {
                echo 'Running HW-SW Integrations tests'
            }
        }

        stage('System Tests'){
            steps {
                echo 'Running system tests'
            }
        }
    }
}