# Continuous Integration Pipeline mit versionierter Toolchain

## With container
Requirements:
- docker/podman
### On-target tests
```
# Build
docker build -t embedded-ci-demo .
docker run --rm -v $(pwd):/build -w /build embedded-ci-demo bash -c "mkdir -p build-target && cd build-target && cmake -G Ninja -DCMAKE_TOOLCHAIN_FILE=cmake/arm_gcc_toolchain.cmake -DBSP_DIR=target_bsp_stm32f407  .. && ninja"

# Run
docker run --rm -v $(pwd):/build -w /build embedded-ci-demo bash ./ep-cli/ep.sh build-target/src/example_gtest.bin
```

### Off-target tests
```
# Build
docker build -t embedded-ci-demo .
docker run --rm -v $(pwd):/build -w /build embedded-ci-demo bash -c "mkdir -p build-host && cd build-host && cmake -G Ninja -DBSP_DIR=target_bsp_stm32f407  .. && ninja"

# Run
docker run --rm -v $(pwd):/build -w /build embedded-ci-demo ./build-host/src/example_gtest
```

## Without container
Requirements:
- cmake >= 3.18
- ninja
- gcc
- gcc-arm-none-eabi

### On-target tests
```
# Build
mkdir -p build-target
cd build-target
cmake -G Ninja -DCMAKE_TOOLCHAIN_FILE=cmake/arm_gcc_toolchain.cmake -DBSP_DIR=target_bsp_stm32f407  ..
ninja

# Run
bash ./ep-cli/ep.sh build-target/src/example_gtest.bin
```

### Off-target tests
```
# Build
mkdir -p build-host
cd build-host
cmake -G Ninja -DBSP_DIR=target_bsp_stm32f407  ..
ninja

# Run
./build-target/src/example_gtest[.exe]
```
